import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data, view_service_type_data, view_invoice_data, view_sys_data


def read():
    # st.write(result)
    menu = ["customer", "services", "service_type", "invoice", "sys_info"]
    choice = st.selectbox("Choose a table to view", menu)
    if choice == "customer":
        result = view_all_data(choice)
        df = pd.DataFrame(result, columns=[
            'customer_id', 'Name', 'email', 'phone', 'city', 'state'])
        with st.expander("View all Customers"):
            st.dataframe(df)
    elif choice == "services":
        result = view_all_data(choice)
        df = pd.DataFrame(result, columns=[
            'user_id', 'username', 'password', 'timer'])
        with st.expander("View all services"):
            st.dataframe(df)
    elif choice == "service_type":
        result = view_service_type_data()
        df = pd.DataFrame(result, columns=[
            'service_id', 'customer_id', 'refreshment', 'printing', 'scanning', 'pc_usage'])
        with st.expander("View all service_types"):
            st.dataframe(df)
    elif choice == "invoice":
        result = view_invoice_data()
        df = pd.DataFrame(result, columns=[
            'invoice_id', 'user_id', 'date', 'price'])
        with st.expander("View all invoices"):
            st.dataframe(df)
    elif choice == "sys_info":
        result = view_sys_data()
        df = pd.DataFrame(result, columns=[
            'sys_num', 'user_id', 'build'])
        with st.expander("View all Sys_info"):
            st.dataframe(df)
