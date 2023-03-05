# Little Lemon Web Application

## Introduction 
This is the final project for Meta Back-End Developer Capstone course (https://www.coursera.org/learn/back-end-developer-capstone/)

This web application utilizes Django + DRF + djoser + MySql
There is a simple static page with url: http://localhost:8000/restaurant/

## APIs
```restaurant/api/menu```
Allow all authenticated users to view the menu items
Only admin user could post new item

Fields needed to post:
>**title**: str

>**price**: decimal

>**featured**: (opt.) boolean, default = 0

```restaurant/api/menu/<int:pk>```
Allow all authenticated users to view single menu item
Only admin user could update or delete single item

```restaurant/api/book```
Allow authenticated users to post new book, please use the same username of the user as the name of book

User could obtain all the books that has the same book name with the current username

Fields needed to post:
>**name**: str, the same as username

>**guest_number**: (opt.) int, default = 1

>**date**: date, in the form of "YYYY-MM-DD"

>**comment**: (opt.) text

```restaurant/api/book/<int:pk>```
Only admin user could view or delete single book

### Current users
Superuser/admin:
>**Username**: admin
>**Password**: 123

Customer:
>**Username**: customer1
>**Password**: lemon@123!

>**Username**: customer2
>**Password**: lemon@123!