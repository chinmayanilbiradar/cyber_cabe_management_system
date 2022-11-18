import pandas as pd
import streamlit as st
from database import view_all_data, view_only_Table_names, get_Table, edit_customer_data, edit_services_data, edit_service_type_data, edit_invoice_data, edit_system_info_data
from database import view_customer_data, view_services_data, view_service_type_data, view_invoice_data, view_sys_data
from database import get_customer_id, get_user_id, get_service_id, get_invoice_id, get_sys_num

from database import view_customer_data, view_services_data, view_service_type_data, view_invoice_data, view_sys_data
from database import view_cusid_data, view_userid_data, view_servid_data, view_invid_data, view_sysnum_data


def update(table):
    if table == 'customer':
        result = view_customer_data()
        # st.write(result)
        df = pd.DataFrame(
            result, columns=['customer_id', 'Name', 'email', 'phone', 'city', 'state'])
        with st.expander("Current Customers"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_cusid_data()]
        selected_dealer = st.selectbox("Customer to Edit", list_of_dealers)
        selected_result = get_customer_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            customer_id = selected_result[0][0]
            Name = selected_result[0][1]
            email = selected_result[0][2]
            phone = selected_result[0][3]
            city = selected_result[0][4]
            state = selected_result[0][5]
            # Layout of Create

            col1, col2, col3 = st.columns(3)
            with col1:
                new_Name = st.text_input("Name:")
                new_email = st.text_input("Email:")
                new_phone = st.text_input("Phone")
            with col2:
                new_city = st.text_input("City:")
                new_state = st.text_input("State:")
            if st.button("Update book"):
                edit_customer_data(new_Name, new_email, new_phone,
                                   new_city, new_state, customer_id)
                st.success(
                    "Successfully updated:: {} to ::{}".format(Name, new_Name))

        result2 = view_customer_data()
        df2 = pd.DataFrame(result2, columns=[
                           'customer_id', 'Name', 'email', 'phone', 'city', 'state'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'services':
        result = view_services_data()
        # st.write(result)
        df = pd.DataFrame(
            result, columns=['user_id', 'username', 'password', 'timer'])
        with st.expander("Current Services"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_userid_data()]
        selected_dealer = st.selectbox("Customer to Edit", list_of_dealers)
        selected_result = get_user_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            user_id = selected_result[0][0]
            username = selected_result[0][1]
            password = selected_result[0][2]
            timer = selected_result[0][3]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_username = st.text_input("UserName:")
                new_password = st.text_input("Password")
            with col2:
                new_timer = st.text_input("Timer:")
            if st.button("Update Services"):
                edit_services_data(new_username, new_password,
                                   new_timer, user_id)
                st.success("Successfully updated:: {} to ::{}".format(
                    username, new_username))

        result2 = view_services_data()
        df2 = pd.DataFrame(result2, columns=[
                           'user_id', 'username', 'password', 'timer'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'service_type':
        result = view_service_type_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=[
                          'service_id', 'customer_id', 'refreshment', 'printing', 'scanning', 'pc_usage'])
        with st.expander("Current Service type"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_servid_data()]
        selected_dealer = st.selectbox("Service type to Edit", list_of_dealers)
        selected_result = get_service_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            service_id = selected_result[0][0]
            refreshment = selected_result[0][1]
            printing = selected_result[0][2]
            scanning = selected_result[0][3]
            pc_usage = selected_result[0][4]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_refreshment = st.text_input("Refreshment:")
                new_printing = st.text_input("Printing")

            with col2:
                new_scanning = st.text_input("Scanning:")
                new_pc_usage = st.text_input("Pc usage:")

            if st.button("Update service_type"):
                edit_service_type_data(new_refreshment, new_printing, new_scanning,
                                       new_pc_usage, service_id)
                st.success("Successfully updated:: {} to ::{}".format(
                    service_id, service_id))

        result2 = view_service_type_data()
        df2 = pd.DataFrame(result2, columns=[
                           'service_id', 'customer_id', 'refreshment', 'printing', 'scanning', 'pc_usage'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'invoice':
        result = view_invoice_data()
        # st.write(result)
        df = pd.DataFrame(
            result, columns=['invoice_id', 'user_id', 'date', 'price'])
        with st.expander("Current Invoices"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_invid_data()]
        selected_dealer = st.selectbox("Invoice to Edit", list_of_dealers)
        selected_result = get_invoice_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            invoice_id = selected_result[0][0]
            date = selected_result[0][1]
            price = selected_result[0][2]

            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_date = st.text_input("Date")
            with col2:

                new_price = st.text_input("Price:")

            if st.button("Update Invoice"):
                edit_invoice_data(new_date, new_price, invoice_id)
                st.success("Successfully updated:: {} to ::{}".format(
                    invoice_id, invoice_id))

        result2 = view_invoice_data()
        df2 = pd.DataFrame(result2, columns=[
                           'invoice_id', 'user_id', 'date', 'price'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'sys_info':
        result = view_sys_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=['sys_num', 'user_id', 'build'])
        with st.expander("Current sys_info"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_sysnum_data()]
        selected_dealer = st.selectbox("System_info to Edit", list_of_dealers)
        selected_result = get_sys_num(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            sys_num = selected_result[0][0]
            user_id = selected_result[0][1]
            build = selected_result[0][2]
            # Layout of Create
            col1, col2 = st.columns(2)
            with col1:
                new_sys_num = st.text_input("System Number:")
                new_user_id = st.text_input("User ID:")
            with col2:
                new_build = st.text_input("Build:")

            if st.button("Update System_info"):
                edit_system_info_data(
                    new_sys_num, new_user_id, new_build, sys_num, user_id, build)
                st.success("Successfully updated:: {} to ::{}".format(
                    user_id, new_user_id))

        result2 = view_sys_data()
        df2 = pd.DataFrame(result2, columns=['sys_num', 'user_id', 'build'])
        with st.expander("Updated data"):
            st.dataframe(df2)
