from flask import Flask
from flask import make_response, request, jsonify
import paths
import sys

app = Flask(__name__)

# Global object stores path data retrieved from each request
my_paths = paths.Path()

# Added to help test connectivitity. Visit http://localhost:3000/ to test
@app.route('/')
def index():
    return 'Hello world'

# Request to instantiate a map on the server.
@app.route('/api/maps/', methods = ['POST'])
def create_map():
    json_content = request.get_json()
    my_paths.set_plane(json_content['row'], json_content['col'])
    return make_response(jsonify(json_content), 201)

# Request to create a start position on the map,
# i.e. where Wall-E currently is.
@app.route('/api/paths/start', methods = ['POST'])
def create_start():
    json_content = request.get_json()
    my_paths.set_walle(json_content['i'], json_content['j'])
    return make_response(jsonify(json_content), 201)

# Request to create a goal position on the map,
# i.e. where Eve currently is.
@app.route('/api/paths/goal/', methods = ['POST'])
def create_goal():
    json_content = request.get_json()
    my_paths.set_eve(json_content['i'], json_content['j'])
    return make_response(jsonify(json_content), 201)

# Request to create a list of cost values on the map,
# i.e. where the obstacles are.
@app.route('/api/costs', methods = ['POST'])
def create_heuristic_cost():
    json_content = request.get_json()
    my_paths.set_obstacles(json_content)
    return make_response(jsonify(json_content), 201)

# Request to find the optimal path to reach goal (Eve).
@app.route('/api/paths', methods = ['GET'])
def find_path():
    json_content = request.get_json()
    x=my_paths.find_path()
    return make_response(jsonify(x), 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3000) #TODO change to localhost
