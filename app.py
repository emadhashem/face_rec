
from crypt import methods
from pickle import GET
from typing import List
from flask import Flask, jsonify, request
import face_rec 
import os
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def index():
    return "Hello From Attendance App."

@app.route('/addimg', methods = ['POST'])
def addimg():
    imgs = request.json['imgs']
    faces = request.json["faces"]
    results = []
    for img in imgs:
        resFaces = face_rec.classify_face(img, faces)
        for res in resFaces:
            if res == 'Unknown':
                continue
            results.append(res[2:])
    ret = []
    [ret.append(x) for x in results if x not in ret]
    return jsonify({'resFaces' : ret})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)