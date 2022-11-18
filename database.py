import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="PES1UG20CS114_PROJECT"
)
c = mydb.cursor()


def add_data1(customer_id, Name, email, phone, city, state):
    c.execute('INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s)',
              (customer_id, Name, email, phone, city, state))
    mydb.commit()


def add_data2(user_id, username, password, timer):
    c.execute('INSERT INTO services VALUES (%s,%s,%s,%s)',
              (user_id, username, password, timer))
    mydb.commit()


def add_data3(service_id, customer_id, refreshment, printing, scanning, usage):
    c.execute('INSERT INTO service_type VALUES (%s,%s,%s,%s,%s,%s)',
              (service_id, customer_id, refreshment, printing, scanning, usage))
    c.execute('CALL DISCOUNT("{}","{}")'.format(customer_id, service_id))
    mydb.commit()


def add_data4(invoice_id, user_id, date, price):
    c.execute('INSERT INTO invoice VALUES (%s,%s,%s,%s)',
              (invoice_id, user_id, date, price))
    mydb.commit()


def add_data5(sys_num, user_id, build):
    c.execute('INSERT INTO sys_info VALUES (%s,%s,%s)',
              (sys_num, user_id, build))
    mydb.commit()


def view_all_data(choice):
    if choice == "customer":
        c.execute('SELECT * FROM customer')

    elif choice == "services":
        c.execute('SELECT * FROM services')

    elif choice == "service_type":
        c.execute('SELECT * FROM service_type')

    elif choice == "invoice":
        c.execute('SELECT * FROM invoice')

    elif choice == "sys_info":
        c.execute('SELECT * FROM sys_info')

    data = c.fetchall()
    return data


def view_customer_data():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data


def view_services_data():
    c.execute('SELECT * FROM services')
    data = c.fetchall()
    return data


def view_service_type_data():
    c.execute('SELECT * FROM service_type')
    data = c.fetchall()
    return data


def view_invoice_data():
    c.execute('SELECT * FROM invoice')
    data = c.fetchall()
    return data


def view_sys_data():
    c.execute('SELECT * FROM sys_info')
    data = c.fetchall()
    return data


def view_cusid_data():
    c.execute('Select customer_id from customer')
    data = c.fetchall()
    return data


def view_userid_data():
    c.execute('Select username from services')
    data = c.fetchall()
    return data


def view_servid_data():
    c.execute('Select service_id from service_type')
    data = c.fetchall()
    return data


def view_invid_data():
    c.execute('Select invoice_id from invoice')
    data = c.fetchall()
    return data


def view_sysnum_data():
    c.execute('Select sys_num from sys_info')
    data = c.fetchall()
    return data


def view_only_Table_names(choice):
    if choice == "customer":
        c.execute('SELECT Name FROM customer')
    elif choice == "services":
        c.execute('SELECT username FROM services')
    elif choice == "service_type":
        c.execute('SELECT customer_id FROM service_type')
    elif choice == "invoice":
        c.execute('SELECT user_id FROM invoice')
    elif choice == "sys_info":
        c.execute('SELECT sys_num FROM sys_info')
    data = c.fetchall()
    return data


def get_Table(choice):
    if choice == "customer":
        c.execute('SELECT * FROM customer')
    elif choice == "services":
        c.execute('SELECT * FROM services')
    elif choice == "service_type":
        c.execute('SELECT * FROM service_type')
    elif choice == "invoice":
        c.execute('SELECT * FROM invoice')
    elif choice == "sys_info":
        c.execute('SELECT * FROM sys_info')

    data = c.fetchall()
    return data


def edit_customer_data(new_Name, new_email, new_phone, new_city, new_state, customer_id):
    c.execute("UPDATE customer SET Name=%s, email=%s, phone=%s, city=%s, state=%s WHERE customer_id=%s",
              (new_Name, new_email, new_phone, new_city, new_state, customer_id))
    mydb.commit()
    c.execute("Select * from customer")

    data = c.fetchall()
    return data


def edit_services_data(new_username, new_password, new_timer, user_id):
    c.execute("UPDATE services SET username=%s, password=%s, timer=%s WHERE user_id=%s",
              (new_username, new_password, new_timer, user_id))
    mydb.commit()
    c.execute("Select * from services")
    data = c.fetchall()
    return data


def edit_service_type_data(new_refreshment, new_printing, new_scanning,
                           new_pc_usage, service_id):
    c.execute("UPDATE service_type SET refreshment=%s, printing=%s, scanning=%s, pc_usage=%s WHERE service_id=%s",
              (new_refreshment, new_printing, new_scanning,
               new_pc_usage, service_id,))
    mydb.commit()
    c.execute("Select * from service_type")

    data = c.fetchall()
    return data


def edit_invoice_data(new_date, new_price, invoice_id,):
    c.execute("UPDATE invoice SET date=%s, price=%s WHERE invoice_id=%s",
              (new_date, new_price, invoice_id))
    mydb.commit()
    c.execute("Select * from invoice")

    data = c.fetchall()
    return data


def edit_system_info_data(new_sys_num, new_user_id, new_build, sys_num, user_id, build):
    c.execute('UPDATE sys_info SET sys_num=%s, user_id=%s, build=%s WHERE sys_num=%s and user_id=%s and build=%s',
              (new_sys_num, new_user_id, new_build, sys_num, user_id, build))
    mydb.commit()
    c.execute("Select * from sys_info")

    data = c.fetchall()
    return data


def get_customer_id(customer_id):
    c.execute('SELECT * FROM customer WHERE customer_id="{}"'.format(customer_id))
    data = c.fetchall()
    return data


def get_user_id(username):
    c.execute('SELECT * FROM services WHERE username="{}"'.format(username))
    data = c.fetchall()
    return data


def get_service_id(service_id):
    c.execute('SELECT * FROM service_type WHERE service_id="{}"'.format(service_id))
    data = c.fetchall()
    return data


def get_invoice_id(invoice_id):
    c.execute('SELECT * FROM invoice WHERE invoice_id="{}"'.format(invoice_id))
    data = c.fetchall()
    return data


def get_sys_num(sys_num):
    c.execute('SELECT * FROM sys_info WHERE sys_num="{}"'.format(sys_num))
    data = c.fetchall()
    return data


def delete_data1(customer_id):
    c.execute('DELETE FROM service_type WHERE customer_id="{}"'.format(customer_id))
    mydb.commit()
    c.execute('DELETE FROM invoice WHERE user_id="{}"'.format(customer_id))
    mydb.commit()
    c.execute('DELETE FROM services WHERE user_id="{}"'.format(customer_id))
    mydb.commit()
    c.execute('DELETE FROM customer WHERE customer_id="{}"'.format(customer_id))
    mydb.commit()


def delete_data2(user_id):
    c.execute('DELETE FROM services WHERE user_id="{}"'.format(user_id))
    mydb.commit()


def delete_data3(service_id):
    c.execute('DELETE FROM service_type WHERE service_id="{}"'.format(service_id))
    mydb.commit()


def delete_data4(invoice_id):
    c.execute('DELETE FROM invoice WHERE invoice_id="{}"'.format(invoice_id))
    mydb.commit()


def delete_data5(sys_num):
    c.execute('DELETE FROM sys_info WHERE sys_num="{}"'.format(sys_num))
    mydb.commit()
