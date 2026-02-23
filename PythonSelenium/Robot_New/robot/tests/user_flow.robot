*** Settings ***
Resource    ../resources/common.resource
Resource    ../keywords/login_keywords.robot
Resource    ../keywords/search_keywords.robot
Resource    ../keywords/cart_keywords.robot
Resource    ../keywords/register_keywords.robot
Test Setup    Open Browser To Application
Task Teardown    Close Application

*** Test Cases ***
User Registration
    Register New User

Login
    Login To Application

Product Search & Details
    Login To Application
    Search Product    Laptop

Add To Cart
    Login To Application
    Search Product    Laptop
    Add Product To Cart

Update Cart & Remove Item
    Login To Application
    Search Product    Laptop
    Add Product To Cart
    Remove Product From Cart

Logout & Session Validation
    Login To Application
    Logout From Application