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

def database_creation():
    """
    CREATE DATABASE IF NOT EXISTS alx_book_store;
    USE alx_book_store;

    CREATE TABLE Authors (
        author_id INT PRIMARY KEY,
        author_name VARCHAR(215)
    );

    CREATE TABLE Books (
        book_id INT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id),
        price DOUBLE,
        publication_date DATE
    );

    CREATE TABLE Customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(215),
        email VARCHAR(215),
        address TEXT
    );

    CREATE TABLE Orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
        order_date DATE
    );
    """
mydb = login()
mycursor = mydb.cursor()

mycursor.execute(database_creation)