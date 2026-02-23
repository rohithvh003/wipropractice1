*** Settings ***
Library   SeleniumLibrary

*** Keywords ***
Add Product To Cart
    Click Button    xpath:(//input[@value='Add to cart'])[1]
    Sleep    1s
    Page Should Contain    Shopping cart

Remove Product From Cart
     Click Link    Shopping cart
     Sleep    1s
     Select Checkbox    name:removefromcart
     Sleep    2s
     Click Button    name:updatecart
     Sleep    2s