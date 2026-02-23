*** Settings ***
Library   SeleniumLibrary

*** Keywords ***
Add Product To Cart
    Click Button    xpath:(//input[@value='Add to cart'])[1]
    Page Should Contain    Shopping cart

Remove Product From Cart
     Click Link    Shopping cart

     Select Checkbox    name:removefromcart
     Click Button    name:updatecart