import pandas as pd
import numpy as np
import pickle

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
path = "D:/Knowledge 4 in 1/Deploying ML/model2.pkl" 
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
    data = [float(x) for x in request.form.values()]
    final_input = coder.transform(np.array(data).reshape(-1 , 1))
    print(final_input)
    output = model.predict(final_input[0])
    return render_template("index.html" , prediction_text = "Your mark is {}" .format(output))

if __name__ == "__main__":
    app.run(debug=True)

