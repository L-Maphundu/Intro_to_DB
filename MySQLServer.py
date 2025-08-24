import mysql.connector

def login():
    try:
        mydb = mysql.connector.connect(
            host = input("Enter host: ").strip().lower(),
            user = input("Enter user: ").strip().lower(),
            password = input("Enter password: ").strip().lower(),
            database = input("Enter database: ").strip().lower()
        )
    except:
        print("Please try again and make sure all details are correct.")
