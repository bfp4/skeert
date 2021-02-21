import time
from flask import Flask, render_template
from python.get_freq import get_freq
from python.read_csv import read_freq
from python.spleeter import run_spleeter

def main(music_file): 
    print("running.")
    run_spleeter(music_file)
    print("spleeter done.")
    get_freq("spleeter-output")
    read_freq()
    print("done")

app = Flask(__name__)

@app.route("/time")
def index():
    main("Purim-drip.mp3")
    return {"time": time.time()}

if __name__ == "__main__":
    app.run(debug=True)
