from app import app

from flask import render_template, request, abort, Flask
from yeelight import *
import json
from collections import namedtuple
import json

#bulbs = [Bulb('192.168.1.100'), Bulb('192.168.1.101'), Bulb('192.168.1.102')]

DAYLIGHT_CT=5000
EVENING_CT=2000

bulb_dictionary = discover_bulbs()
print("discovered bulbs: " + str(bulb_dictionary))

bulbs = []
for bulb in bulb_dictionary:
    bulbs.append(Bulb(bulb['ip']))
    print(hex(int(bulb['capabilities']['rgb'])))
# ROUTING/VIEW FUNCTIONS


@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    # bulb_values = {}
    # it = 0
    # for bulb in bulbs:
    #     try:
    #         data = bulb.get_properties()
    #         bulb_values[str(it)] = data
    #         it = it + 1
    #     except Exception:
    #         bulb_values[str(it)] = {'connected': None}+
    #         it = it + 1

    return render_template('index.html', bulbs=bulb_dictionary)


@app.route('/f/<lampID>', methods=['POST'])
def flashLight(lampID):
    try:
        bulbs[int(lampID)].toggle()
        return "OK"
    except Exception as e:
        return e.args.__str__()


@app.route('/toggleWB/<lampID>', methods=['POST'])
def toggleWB(lampID):
    try:
        bulbs[int(lampID)].set_color_temp(int(request.form.get('temp')))
    except Exception as e:
        return e.args.__str__()
    return "OK"


@app.route('/color/<lampID>', methods=['POST'])
def color(lampID):
    try:
        colors = request.form
        print("setting color :" + colors.get('r')+colors.get('g')+colors.get('b'))
        bulbs[int(lampID)].set_rgb(int(colors.get('r')), int(colors.get('g')), int(colors.get('b')), 0)
        # bulbs[int(lampID)].set_color_temp(DAYLIGHT_CT)
        return "OK"
    except Exception as e:
        return e.args.__str__()


@app.route('/changeIntensity/<lampID>', methods=['POST'])
def changeIntensity(lampID):
    try:
        bulbs[int(lampID)].set_brightness(int(request.form.get('intensity')))
    except Exception as e:
        return e.args.__str__()
    return "OK"
