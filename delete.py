import pandas as pd
import streamlit as st
from database import view_customer_data, view_services_data, view_service_type_data, view_invoice_data, view_sys_data

from database import view_cusid_data, view_userid_data, view_servid_data, view_invid_data, view_sysnum_data


from database import delete_data1, delete_data2, delete_data3, delete_data4, delete_data5


def delete(table):
    if table == 'customer':
        result = view_customer_data()
        df = pd.DataFrame(
            result, columns=['customer_id', 'Name', 'email', 'phone', 'city', 'state'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_cusid_data()]
        selected_dealer = st.selectbox("Customer to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data1(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_customer_data()
        df2 = pd.DataFrame(new_result, columns=[
                           'customer_id', 'Name', 'email', 'phone', 'city', 'state'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'services':
        result = view_services_data()
        df = pd.DataFrame(
            result, columns=['user_id', 'username', 'password', 'timer'])
        with st.expander("Current data"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_userid_data()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data2(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_services_data()
        df2 = pd.DataFrame(new_result, columns=[
                           'user_id', 'username', 'password', 'timer'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'service_type':
        result = view_service_type_data()
        df = pd.DataFrame(result, columns=[
                          'service_id', 'customer_id', 'refreshment', 'printing', 'scanning', 'pc_usage'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_servid_data()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data3(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_service_type_data()
        df2 = pd.DataFrame(new_result, columns=[
                           'service_id', 'customer_id', 'refreshment', 'printing', 'scanning', 'pc_usage'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'invoice':
        result = view_invoice_data()
        df = pd.DataFrame(
            result, columns=['invoice_id', 'user_id', 'date', 'price'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_invid_data()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data4(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_invoice_data()
        df2 = pd.DataFrame(new_result, columns=[
                           'invoice_id', 'user_id', 'date', 'price'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table == 'sys_info':
        result = view_sys_data()
        df = pd.DataFrame(result, columns=['sys_num', 'user_id', 'build'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealers = [i[0] for i in view_sysnum_data()]
        selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete user"):
            delete_data5(selected_dealer)
            st.success("user has been deleted successfully")
        new_result = view_sys_data()
        df2 = pd.DataFrame(new_result, columns=['sys_num', 'user_id', 'build'])
        with st.expander("Updated data"):
            st.dataframe(df2)
