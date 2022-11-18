# Importing pakages
import streamlit as st
import mysql.connector
from create import create
from delete import delete
from read import read
from update import update
from sql import sql_func
import pandas as pd


mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)
c = mydb.cursor()


def main():
    st.title("Cyber Cafe Management System")
    menu = ["Add", "View", "Edit", "Remove", "SQL Query"]
    table_names = ["customer", "services",
                   "service_type", "invoice", "sys_info"]
    choice = st.sidebar.selectbox("action", menu)
    table = st.sidebar.selectbox("table", table_names)

    if choice == "Add":
        if table == 'customer':
            st.subheader("Enter customer Details:")
            create(table)
        elif table == 'services':
            st.subheader("Enter services Details:")
            create(table)
        elif table == 'service_type':
            st.subheader("Enter service_type Details:")
            create(table)
        elif table == 'invoice':
            st.subheader("Enter invoice Details:")
            create(table)
        elif table == 'sys_info':
            st.subheader("Enter sys_info Details:")
            create(table)

    elif choice == "View":
        if table == 'customer':
            read()
        elif table == 'services':
            read()
        elif table == 'service_type':
            read()
        elif table == 'invoice':
            read()
        elif table == 'sys_info':
            read()

    elif choice == "Remove":
        if table == 'customer':
            delete(table)
        elif table == 'services':
            delete(table)
        elif table == 'service_type':
            delete(table)
        elif table == 'invoice':
            delete(table)
        elif table == 'sys_info':
            delete(table)

    elif choice == "Edit":
        if table == 'customer':
            update(table)
        elif table == 'services':
            update(table)
        elif table == 'service_type':
            update(table)
        elif table == 'invoice':
            update(table)
        elif table == 'sys_info':
            update(table)

    elif choice == "SQL Query":
        st.subheader("Type in your Query")
        ans = sql_func()
        if (ans != 0):
            df = pd.DataFrame(ans)
            st.dataframe(df)
        else:
            st.subheader("No query given")


if __name__ == '__main__':
    main()
