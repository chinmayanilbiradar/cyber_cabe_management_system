import pandas as pd
import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="PES1UG20CS114_PROJECT"
)
c = mydb.cursor()


def sql_func():
    st.title("Here")
    query = st.text_input("Type your query here: ")
    if (query != ""):
        c.execute(query)
        data = c.fetchall()
        mydb.commit()
        return data
    else:
        return 0
