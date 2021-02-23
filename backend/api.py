import os
from flask import Flask, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from python.get_freq import get_freq
from python.read_csv import read_freq
from python.spleeter import run_spleeter

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'wav', 'mp3'}

app = Flask(__name__)
app.secret_key = 'the random string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def main(music_file): 
    print("running.")
    run_spleeter(music_file)
    print("spleeter done.")
    get_freq("spleeter-output")
    return read_freq()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/run', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("http://localhost:3000/")

if __name__ == "__main__":
    app.run(debug=True)
