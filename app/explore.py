
import pandas as pd
import numpy as np
import streamlit as stl
import matplotlib.pyplot as plt

@stl.cache
def load_data():
    df= pd.read_csv("D:/Knowledge 4 in 1/Deploying ML/First_Project_MLE_Predict_Mark/DataSet/data.csv" ,encoding='unicode_escape')  
    return df

df = load_data()

def show_explore():
    stl.title(" Explore more about The DataSet and our Mark")

    stl.header(""" ------------- - - - - Created By Tran Phi Hung - - - - ----------------""")

    fig1 , ax1 = plt.subplots(figsize = (16 , 10))
    cols = df.columns
    ax1.barh(df[cols[1]].values , df["mean_subject"].sort_values().values , color = "cyan"   )
    ax1.set_title("Mark average of one of student")
    ax1.set_xlabel("Full Name")
    ax1.set_ylabel("Mark")
    ax1.legend()
    
    stl.subheader("Total of The Student's Mark")
    stl.pyplot(fig1)

    cols = df.columns
    fig2 , ax2 = plt.subplots(figsize = (20, 15))
    ax2.plot(df["mean_subject"].sort_values().values , df[cols[1]].values ,color = "pink" , marker = "*" , ms = 10 , mfc = "y"  )
    ax2.set_title("Mark average of one of student")
    ax2.set_xlabel("Full Name")
    ax2.set_ylabel("Mark")
    ax2.legend()

    stl.subheader("PLot is impressing Average of The Student's Mark")
    stl.pyplot(fig2)

    x_num = len(df[df["mean_subject"] <= 3.5])
    y_num = len(df[df["mean_subject"] > 3.5])
    fig3 , (ax3 , ax4) = plt.subplots(1 , 2 , figsize = (16 , 6))
    ax3.hist(df[df["mean_subject"] <= 3.5]["mean_subject"] , label="mean_subject <= 3.5"  , color = "hotpink" , density = True , alpha = 0.7)
    ax3.set_xlabel("Mean_subject")
    ax3.set_ylabel("Count_mean_subject")
    ax3.legend()


    ax4.hist(df[df["mean_subject"] > 3.5]["mean_subject"] , label="mean_subject > 3.5"  , color = "blue" , density = True , alpha = 0.7)
    ax4.set_xlabel("Mean_subject")
    ax4.set_ylabel("Count_mean_subject")
    ax4.legend()

    stl.subheader("Total Number of student have their's mark between 0 --> 3.5 and 3.5 --> 5")
    stl.pyplot(fig3)