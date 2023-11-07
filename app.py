from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/audio', methods=['POST'])
def save_audio():
    try:
        file = request.files['file']
        filename = file.filename
        print("Current Working Directory: ", os.getcwd())
        filepath = os.path.join("C:/Users/Areeb/python/ova", filename) # Modify this path as necessary
        file.save(filepath)
        return {"status": "success", "message": "File saved successfully."}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=7001)