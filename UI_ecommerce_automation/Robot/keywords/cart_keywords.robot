*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/locators.robot

*** Keywords ***

Open Shopping Cart
    Click Link    ${SHOPPING_CART_LINK}
    Wait Until Page Contains Element    ${QTY_INPUT}

Update Cart Quantity
    [Arguments]    ${qty}
    Input Text    ${QTY_INPUT}    ${qty}
    Click Button    ${UPDATE_CART_BTN}
    Wait Until Page Contains    ${qty}

Remove Item From Cart
    Click Element    ${REMOVE_ITEM_CHECKBOX}
    Click Button     ${UPDATE_CART_BTN}
    Wait Until Page Contains    Your Shopping Cart is empty!
