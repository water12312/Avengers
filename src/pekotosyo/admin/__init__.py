from flask import Flask

app = Flask(__name__)

app.config.from_object('practice.config')

import admin.views