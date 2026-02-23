*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/locators.robot

*** Keywords ***

Search Product
    [Arguments]    ${term}
    Input Text    ${SEARCH_BOX}    ${term}
    Click Button    ${SEARCH_BTN}
    Wait Until Page Contains    ${term}

Open First Product
    Click Element    ${FIRST_PRODUCT}
    Wait Until Page Contains Element    ${PRODUCT_TITLE}
    Wait Until Page Contains Element    ${PRODUCT_PRICE}

Add Product To Cart
    Click Button    ${ADD_TO_CART_DYNAMIC}
    Wait Until Page Contains    The product has been added
