#!flask/bin/python

# Code based on lecture DR8.2 REST

# Building a simple rest server


from flask import Flask, jsonify,  request, abort, make_response
import json

# from flask_cors import CORS # review if this is necessary

app = Flask(__name__, static_url_path='',static_folder = '.')

# create python list of JSON objects 

leaders = [
    {"id":1,"name":"Jeremy Corbyn","party":"Labour","votes":0},
    {"id":2,"name":"Johnson","party":"Conservative","votes":0},
    {"id":3,"name":"Swinson","party":"Liberal Democrats","votes":0},
    {"id":4,"name":"Sturgeon","party":"SNP","votes":0},
    {"id":5,"name":"ONeill","party":"Sinn Fein","votes":0},
    {"id":6,"name":"Foster","party":"DUP","votes":0},
    {"id":7,"name":"Long","party":"Alliance NI","votes":0}
] 

# ID to keep track of leaders. Will be incremented when leaders items are added
nextID  = 8

@app.route('/')
def index():
    return "<i>Hello, Voters!</i>"


# CRUD Methods

# READ with ['GET']
@app.route('/leaders', methods=['GET'])
def getAll():
    return jsonify(leaders) #jsonify comes from flask. compare with week 5, w
# curl -i http://localhost:5000/leaders


# Find leaders item by ID
@app.route('/leaders/<int:id>')
def findByName(id):
    foundLeader = list(filter(lambda s : s['id'] == id , leaders))
    if len(foundLeader) == 0:
        return jsonify( {} ),204 
    return jsonify( foundLeader[0])
#    curl -i http://127.0.0.1:5000/leaders/5
    


# CREATE with ['POST']
@app.route('/leaders', methods = ['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
    newLeader = {
        "id":nextID,
        "name": request.json['name'],
        "party": request.json['party'],
        "votes": 0
        }
    leaders.append(newLeader)
    nextID += 1
    return jsonify(newLeader),201
       # curl -i -H  "Content-Type:application/json" -X POST -d '{"name":"Alan Price","party":"Plaid Cymru"}' http://127.0.0.1:5000/leaders

# DELETE with ['DELETE']
@app.route('/leaders/<int:id>', methods = ['DELETE'])
def delete(id):
    foundLeader = list(filter(lambda s : s['id'] == id , leaders))
    if len(foundLeader) == 0:
        abort(404)
    leaders.remove(foundLeader[0])
    return jsonify( {'result':'true'})


@app.route('/votes/<int:id>', methods = ['POST'])
def addVote(id):
    foundLeader = list(filter(lambda s : s['id'] == id , leaders))
    if len(foundLeader) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if not'votes' in request.json or type(request.json['votes']) is not int:
        abort(401)
    newVotes = request.json['votes']
    foundLeader[0]['votes']  += newVotes
    return jsonify(foundLeader[0])



@app.route('/votes/leaderboard')
def getLeaderBoard():
    leaders.sort(key = lambda x: x['votes'], reverse = True)
    return jsonify(leaders)


if __name__ == '__main__' :
    app.run(debug= True)