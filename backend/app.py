import cv2
import os
from flask import Flask, flash, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename

import src.config as config
import src.model as model

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER
app.secret_key = os.urandom(24)


@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            params = model.load_params(os.path.join(config.DIR_BIN, "parameters.json"))
            image = [cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))]
            result = model.classify(image, params["mean"], params["cov"], params["threshold"])[0]
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result_fname = "_res.".join(filename.rsplit("."))
            cv2.imwrite(os.path.join(app.config["RESULT_FOLDER"], result_fname), result)
            return redirect(url_for('download_file', name=result_fname))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/upload/<name>')
def download_file(name):
    return send_from_directory(app.config["RESULT_FOLDER"], name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
