from flask import Flask, render_template, url_for, request
import pandas as pd

import pickle

## Load the model from disk.
loaded_model= pickle.load(open('Air Quality Index/Deployment/random_forest_model.pkl', 'rb'))
app = Flask(__name__) 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods= ['POST'])
def predict():
    df = pd.read_csv('Air Quality Index/Deployment/Test_Combine.csv')
    my_predictions = loaded_model.predict(df.iloc[:,:-1].values)
    my_predictions = my_predictions.tolist()
    return render_template('result.html', prediction = my_predictions)


if __name__ == "__main__":
    app.run(host= '127.0.0.1', port= 8000, debug = True) 
