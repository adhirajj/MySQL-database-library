'''
DESCRIPTION:

This is a menu driven program using MySQL Database Connectivity to create a database that acts like an online book store/ library.
The Database created is called BOOKDB, and the table in the database where all the information is stored is called BOOK. 
This program is used to form a connection between MySQL database and python, and perform operations such as:
1. Inserting new records 
2. Displaying all records 
3. Searching and display 
4. Counting records based on a category 
5. Counting records more than a user given price
6. Deleting records matching with a user given bookno 
7. Deleting records matching with user given bookname 
8. Editing/ Updating price of a record for a user given bookno

'''

import mysql.connector as sc
mydb=sc.connect(host= 'localhost', user='student', passwd='root')
mycur= mydb.cursor()
if mydb.isconnected()==True:
    print("connection successfully established")
else:
    print("connection not made")

mycur.execute("create database BOOKDB")
mycur.execute("use BOOKDB")
mycur.execute("create table BOOK (bookno integer primary key, bookname varchar(20), category char(20) price decimal )")
def insert():
    n=int(input("enter the number of records you wish to input"))
    for i in n:
        bkno=input("enter the book number")
        bknm= input("enter the book name")
        cat=input("enter the category")
        pr=input("enter the price of the book")
        mycur.execute("insert into BOOK values("+bkno+",'"+bknm+"','"+cat+"',"+pr+")")
    mycur.commit()

def disp():
    mycur.execute("select * from BOOK")
    a=mycur.fetchall()
    for i in a:
        print(i[0],i[1],i[2],i[3],i[4], sep='\t')

def search():
    a=input("enter the choice number of what you wish to search on- \n 1.Bookno \n 2.Bookname \n 3.Category \n 4.Price")
    ans=input("enter the value-")
    if a==1:
        mycur.execute("select * from BOOK where bookno="+ans+"")
    elif a==2:
        mycur.execute("select * from BOOK where bookname='"+ans+"'")
    elif a==3:
        mycur.execute("select * from BOOK where category='"+ans+"'")
    elif a==4:
        mycur.execute("select * from BOOK where price="+ans+"")
    b=mycur.fetchall()
    print(b)

def count():
    categ=input("enter the choice number of that you wish to count- \n 1.Bookno \n 2.Bookname \n 3.Category \n 4.Price")
    if categ==1:
        mycur.execute("select count(bookno) as count from BOOK")
    elif categ==2:
        mycur.execute("select count(bookname) as count from BOOK")
    elif categ==3:
        mycur.execute("select count(category) as count from BOOK")
    elif categ==4:
        mycur.execute("select count(price) as count from BOOK")

    b=mycur.fetchall()
    print(b)

def price():
    pr=input("enter the minimum pirce on the basis of which you wish to filter the records")
    mycur.execute("select count(Price) as Count Price from BOOK where price>"+pr+"")
    a=mycur.fetchone()
    print(a)

def del_bkno():
    bkno=input("enter the book number of the record you wish to delete")
    mycur.execute("select * from BOOK where bookno="+bkno+"")
    a=mycur.fetchone()
    if a==():
        print("no such record found")
    else:
        print(a)
        ans=input("do you wish to delete this record? y/n")
        if ans in ('Y','y'):
            mycur.execute("delete from BOOK where bookno="+bkno+"")
            mycur.commit()

def del_bknm():
    bknm=input("enter the name of the book you wish to delete")
    mycur.execute("select * from BOOK where bookname='"+bknm+"'")
    a=mycur.fetchall()
    if a==():
        print("no such record exists")
    else:
        for i in a:
            print(i)
        ans=input("do you wish to delete this reocrd? y/n")
        if ans in ('Y','y'):
            mycur.execute("delete form BOOK where bookname='"+bknm+"'")
            mycur.commit()

def edit_price():
    bkno=input("enter the book number")
    mycur.execute("select * from BOOK where bookno="+bkno+"")
    a=mycur.fetchone()
    print(a)
    ans=input("do you wish to make changes in this record? y/n")
    if ans in ('Y','y'):
        pr=input("enter the new price")
        mycur.execute("update BOOK set price="+pr+" where bookno="+bkno+"")
        mycur.commit()

print("enter the choice you wish to perform")
while True:
    ch=input("1. Insert new records \n 2.Display all records \n 3. Search and Display \n 4.Count records on category \n 5.Count records on price \n 6. Delete using book number \n 7. Delete using book name \n 8. Edit price")
    if ch==1:
        insert()
    elif ch==2:
        disp()
    elif ch==3:
        search()
    elif ch==4:
        count()
    elif ch==5:
        price()
    elif ch==6:
        del_bkno()
    elif ch==7:
        del_bknm()
    elif ch==8:
        edit_price()
    else:
        print("invalid entry")
    ans=input("do you wish to conitune? y/n")
    if ans in ('n','N'):
        break