import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

from flask import Flask , render_template , url_for , request , app , jsonify

app = Flask(__name__)

## Load Data

def load_model(path , way = 1):
    if way == 1:
        total = pickle.load(open(path, "rb"))
    ## Or way two:
    elif way == 2:
        with open(path, "rb") as f:
            total = pickle.load(f)
    
    model = total["model"]
    coder = total["coder"]

    return model , coder

# print(model1 , model)
path = "D:/Knowledge 4 in 1/Deploying ML/First_Project_MLE_Predict_Mark/model2.pkl" 
model , coder = load_model(path  , 1)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api' , methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(-1 , 1))
    new_data = coder.transform(np.array(list(data.values())).reshape(-1 , 1))

    output = model.predict(new_data)

    return jsonify(output[0])

@app.route('/predict' , methods = ['POST'])
def predict():
    data = [[]]
    for x in request.form.values():
        if x.isdigit() == False:
            c = LabelEncoder().fit_transform(np.array(x).reshape(-1  , 1))
            data[0].append(float(c))
        else:
            data[0].append(float(x))

    # print(data[0])
    output = model.predict(data)
    return render_template("predict.html" , prediction_text = "Your mark is {}" .format(output[0]))

if __name__ == "__main__":
    app.run(debug=True)

