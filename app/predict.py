import streamlit as stl
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

def load_model():
    with open("D:/Knowledge 4 in 1/Deploying ML/First_Project_MLE_Predict_Mark/model2.pkl" , "rb") as f:
        model_1 = pickle.load(f)
    model1 = model_1["model"]
    coder = model_1["coder"]
    return model1 , coder

model1 , coder = load_model()


def show_predict():
    stl.title("Predict Mark of student at the primary school.")
    stl.write(""" ### Some of the infomation That need check on the our system `!!` """)


    full_names = {
        "Thai Phuc An" ,  "Nguyen Thanh Sang" , "Pham Chi Thanh" ,
        "Nguyen Gia Bao" , "Luong Nguyen Quynh Phat" ,  "Le Minh Sang" ,
        "Nguyen Hoang Phuc Thinh",    "Hoan Ngoc Nhu Y" ,    "Tran Ha Tuan Kiet" ,
        "Bui Nhan Nghia",    "Bui Ngoc Thanh Ha" ,
        "Võ Cao Thang" ,    "Ngo Minh Tu" ,
        "Nguyen Thi Tram Anh",
        "Vo Van Chanh" ,    "Pham Le Khuc Duy" ,
        "Mai Rang Dong" ,    "Huynh Gia Hao",
        "Nguyen An Khang" ,    "Hao Phuong Khoi" ,
        "Le Thien Phat" ,    "Phung Thanh Vinh",
        "Phan Phan" ,    "Tu Anh Dat" ,    "Phan Phuc Khao" ,
        "Tran An Nhien" ,    "Tran Canh",    "Tran Tu Tai" ,
        "Nguyen Le" ,    "Anh Hung"
        }

    claass = {
        45078, 45079, 45086, 45087, 45149
    }

    Id = {
        1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
        11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30
    }

    full_names_box = stl.selectbox("Full Name Or Name" , full_names)

    claass_box = stl.selectbox("Class" , claass)

    id_box = stl.slider("STT" , 1 , 30 , 1)

    ok = stl.button("Predict YOur  Mark")
    if ok:
        X = np.array([[id_box , full_names_box , claass_box]])
        X[: , 1] = LabelEncoder().fit_transform(X[: , 1])
        X = X.astype(float)

        mark = model1.predict(X)[0]
        stl.subheader(f"The your mark is  {mark} marks")