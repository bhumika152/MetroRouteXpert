# from flask import Flask,request
# from path_algorithm import getPath,getPathFull
# from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# @app.route("/getPath",methods=["POST"])
# def getPost():
#     body= request.get_json()
#     print(body)
#     source:str = body["source"]
#     dest:str = body["destination"]
#     if("nodes" in body):
#         nodes = body["nodes"]
#         return {"path":getPathFull(source,nodes,dest)}
#     else:
#         return {"path":getPath(source,dest)}
# if __name__ == "__main__":
#     cross_origin(getPost)
#     app.run(port=5000)
from flask import Flask, request, send_from_directory
from path_algorithm import getPath, getPathFull
from flask_cors import CORS
import os

# Serve React frontend from build folder
app = Flask(__name__, static_folder="static/build", static_url_path="")
CORS(app)  # Only needed if frontend is on another domain

# ----------------------------
# API Endpoint
# ----------------------------
@app.route("/getPath", methods=["POST"])
def get_post():
    body = request.get_json()
    print("Received:", body)

    source: str = body["source"]
    dest: str = body["destination"]

    if "nodes" in body:
        nodes = body["nodes"]
        return {"path": getPathFull(source, nodes, dest)}
    else:
        return {"path": getPath(source, dest)}

# ----------------------------
# React Frontend Routing
# ----------------------------
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_react(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")  # For React Router fallback

# ----------------------------
# Run Locally
# ----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
