# app.py                # Flask API


from flask import Flask, request, jsonify, send_file
from clip_cleaner import process_uploaded_video
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    clean_video_path = process_uploaded_video(file_path)
    return jsonify({
        "message": "Processing complete",
        "cleanVideo": clean_video_path
    })

@app.route("/download", methods=["GET"])
def download():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        return "File not found", 404
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
