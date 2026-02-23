*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}   https://demowebshop.tricentis.com
${BROWSER}    chrome

${REGISTER_LINK}        xpath://a[text()='Register']
${LOGIN_LINK}           xpath://a[text()='Log in']
${LOGOUT_LINK}          xpath://a[text()='Log out']

${FIRSTNAME_FIELD}      id:FirstName
${LASTNAME_FIELD}       id:LastName
${EMAIL_FIELD}          id:Email
${PASSWORD_FIELD}       id:Password
${CONFIRM_PASSWORD}     id:ConfirmPassword
${REGISTER_BUTTON}      id:register-button
${LOGIN_BUTTON}         xpath://input[@value='Log in']

${SEARCH_BOX}           id:small-searchterms
${SEARCH_BUTTON}        xpath://input[@value='Search']

${FIRST_PRODUCT}        xpath:(//h2[@class='product-title']/a)[1]
${ADD_TO_CART_BTN}      xpath://input[@value='Add to cart']
${NOTIFICATION_BAR}     id:bar-notification
${SHOPPING_CART}        xpath://span[text()='Shopping cart']

${QTY_INPUT}            xpath://input[contains(@class,'qty-input')]
${UPDATE_CART_BTN}      xpath://input[@name='updatecart']
${REMOVE_CHECKBOX}      xpath://input[@name='removefromcart']

*** Keywords ***
Open Browser To Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Register Keyword To Run On Failure    Capture Page Screenshot

Close Browser Session
    Close Browser

Click Element Safe
    [Arguments]   ${locator}
    Wait Until Element Is Visible    ${locator}    10s
    Click Element    ${locator}

Input Text Safe
    [Arguments]   ${locator}   ${text}
    Wait Until Element Is Visible    ${locator}    10s
    Input Text    ${locator}    ${text}
