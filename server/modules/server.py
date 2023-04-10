from logging import error
from flask import Flask, render_template, request
import json
import modules.member
import os
import random

app = Flask(__name__)

def setupServer():
    @app.route("/")
    def index():
        return render_template("index.html")
    @app.route("/api/", methods = ["GET", "POST"])
    def api():
        if request.method == "GET":
            with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
                data = json.load(f)
                return data
        if request.method == "POST":
            pass

    @app.route("/api/<string:room>/", methods = ["GET", "POST"])
    def apiRoom(room):
        if request.method == "GET":
            with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
                data = json.load(f)
                for i in range(0, len(data['rooms'])):
                    if data['rooms'][i]['id'] == room:
                        return str(data['rooms'][i])
        if request.method == "POST":
            pass

    @app.route("/api/<string:room>/<string:objs>/", methods = ["GET", "POST"])
    def apiList(room,objs):
        if request.method == "GET":
            with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
                data = json.load(f)
                for i in range(0, len(data['rooms'])):
                    if data['rooms'][i]['id'] == room:
                        return str(data['rooms'][i][objs])
        if request.method == "POST":
            pass
        
    @app.route("/api/<string:room>/<string:objs>/<string:obj>/", methods = ["GET", "POST"])
    def apiObj(room,objs,obj):
        if request.method == "GET":
            with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
                data = json.load(f)
                for i in range(0, len(data['rooms'])):
                    if data['rooms'][i]['id'] == room:
                        return str(data['rooms'][i][objs][obj])
        if request.method == "POST":
            pass

    @app.route("/api/<string:room>/<string:objs>/<string:obj>/<string:pos>", methods = ["GET", "POST"])
    def apiObjPos(room,objs,obj,pos):
        if request.method == "GET":
            with open(os.path.dirname(__file__) + "/data/data.json", "r+") as f:
                data = json.load(f)
                for i in range(0, len(data['rooms'])):
                    if data['rooms'][i]['id'] == room:
                        return str(data['rooms'][i][objs][obj][pos])
        if request.method == "POST":
            pass

def startServer():
    app.run(debug = True)
