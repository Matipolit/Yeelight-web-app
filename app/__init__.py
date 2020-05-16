from flask import Flask

app = Flask(__name__)

app.add_template_global(hex, name='hex')
app.add_template_global(int, name='int')

from app import routes
