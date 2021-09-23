import random
import os
from flask import Flask, render_template, request, redirect, jsonify
from effnet import model

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print('Audio Received')

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == "":
            return redirect(request.url)
    return  render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():

    # get audiofile and save it
    audiofile= request.files['file']
    file_name = str(random.randint(0, 100938))
    audiofile.save(file_name)
    # invoke deepfake prediction
    model = model()
    #make a prediction
    audio_prediction = model.predict(file_name)
    # remove audiofile
    os.remove(file_name)
    # send the prediction in json
    data = {"Prediction_Class" : audio_prediction}
    return jsonify(data)

if __name__  == "__main__":
    app.run(debug=True, threaded=True)