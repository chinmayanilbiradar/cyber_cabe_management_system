import pandas as pd
import streamlit as st
from database import add_data1, add_data2, add_data3, add_data4, add_data5, view_all_data


def create(table):
    if table == 'customer':
        col1, col2 = st.columns(2)
        with col1:
            customer_id = st.text_input("Customer ID:")
            Name = st.text_input("Name:")
            email = st.text_input("Email:")
        with col2:
            phone = st.text_input("Phone")
            city = st.text_input("City:")
            state = st.text_input("State:")
        if st.button("Add data"):
            add_data1(customer_id, Name, email, phone, city, state)
            st.success("Successfully added customer : {}".format(Name))

    elif table == 'services':
        col1, col2 = st.columns(2)
        with col1:
            user_id = st.text_input("User ID:")
            username = st.text_input("UserName:")

        with col2:
            password = st.text_input("Password")
            timer = st.text_input("Timer:")

        if st.button("Add data"):
            add_data2(user_id, username, password, timer)
            st.success("Successfully added service : {}".format(user_id))

    elif table == 'service_type':
        col1, col2 = st.columns(2)
        with col1:
            service_id = st.text_input("Service ID:")
            customer_id = st.text_input("Customer ID:")
            refreshment = st.text_input("Refreshment(Yes or No):")

        with col2:
            printing = st.text_input("Printing")
            scanning = st.text_input("Scanning:")
            pc_usage = st.text_input("Pc usage:")

        if st.button("Add data"):
            add_data3(service_id, customer_id, refreshment,
                      printing, scanning, pc_usage)
            result = view_all_data("invoice")
            df = pd.DataFrame(result, columns=[
                'invoice_id', 'user_id', 'date', 'price'])
            with st.expander("View all invoices"):
                st.dataframe(df)
            st.success(
                "Successfully added service_type : {}".format(customer_id))

    elif table == 'invoice':
        col1, col2 = st.columns(2)
        with col1:
            invoice_id = st.text_input("Invoice ID:")
            user_id = st.text_input("User ID:")

        with col2:
            date = st.text_input("Date")
            price = st.text_input("Price:")

        if st.button("Add data"):
            add_data4(invoice_id, user_id, date, price)
            st.success("Successfully added invoice : {}".format(user_id))

    elif table == 'sys_info':
        col1, col2 = st.columns(2)
        with col1:
            sys_num = st.text_input("System Number:")
            user_id = st.text_input("User ID:")
        with col2:
            build = st.text_input("Build:")

        if st.button("Add data"):
            add_data5(sys_num, user_id, build)
            st.success("Successfully added sys_info : {}".format(user_id))
