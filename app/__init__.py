from flask import Flask
#from flask_socketio import SocketIO, emit

app = Flask(__name__)
#socketio = SocketIO(app)

app.add_template_global(hex, name='hex')
app.add_template_global(int, name='int')

from app import routes
