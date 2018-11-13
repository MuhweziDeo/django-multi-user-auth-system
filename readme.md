## A Simple multi-user login system

# Features

- Two different types of users can be logged in and redirect basing on thier type
- It overwrites default django user model and users a custom user model

# Weakness 

- Views for separate user types are not protected

# Fix

- Write decorators to protect the views