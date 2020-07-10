from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('RandomForest.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

##'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
     ##  'LOR', 'CGPA', 'Research'

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        HSP = float(request.form['HSP'])
        SSP = float(request.form['SSP'])
        DP = float(request.form['DP'])
        ETS = float(request.form['ETS'])
        MBAP = float(request.form['MBAP'])
        DS=request.form['DSub']
        if(DS=='Commerce'):
            DS=1
        else:
            DS=0
        MBAS=request.form['MBAS']
        if(MBAS=='Market&Finance'):
            MBAS=1
        else:
            MBAS=0
        WE=request.form['WE']
        if(WE=='Yes'):
            WE=1
        else:
            WE=0
        if(SSP>79):
            SSGN=1
        else:
            SSGN=0
        prediction=model.predict([[SSP,HSP,DP,WE,ETS,MBAS,MBAP,DS,SSGN]])
        if(prediction==1):
            return render_template('index.html',prediction_text="You will get a Job")
        else:
            return render_template('index.html',prediction_text="You are not getting a Job")

if __name__=="__main__":
    app.run(debug=True)