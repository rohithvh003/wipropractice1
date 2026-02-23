*** Settings ***
Library    SeleniumLibrary
Library    String
Library    DataDriver    file=../variables/users.csv    dialect=unix    encoding=utf-8
Resource   ../resources/common.resource
Resource   ../resources/register_keyword.robot
Resource   ../resources/login_keywords.robot
Resource   ../resources/search_keywords.robot
Resource   ../resources/cart_keyword.robot
Suite Setup      Open Browser To Application
Suite Teardown   Close Browser Session

*** Test Cases ***
E2E Flow for user ${firstname}
    [Template]    Complete User Flow

*** Keywords ***
Complete User Flow
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${password}    ${confirm_password}    ${search_item}
    Log    ${firstname}
#Register

    Click Element Safe    ${REGISTER_LINK}
    Wait Until Page Contains    Register    10s

    Click Element    id:gender-male

    Input Text Safe    ${FIRSTNAME_FIELD}    ${firstname}
    Input Text Safe    ${LASTNAME_FIELD}     ${lastname}

    ${random}=    Generate Random String    4    [NUMBERS]
    ${generated_email}=    Set Variable    ${email}${random}@mail.com

    Input Text Safe    ${EMAIL_FIELD}    ${generated_email}
    Input Text Safe    ${PASSWORD_FIELD}    ${password}
    Input Text Safe    ${CONFIRM_PASSWORD}    ${confirm_password}

    Click Element Safe    ${REGISTER_BUTTON}
    Wait Until Page Contains    Your registration completed    10s

    Click Element Safe    ${LOGOUT_LINK}

    Click Element Safe    ${LOGIN_LINK}
    Input Text Safe    ${EMAIL_FIELD}    ${generated_email}
    Input Text Safe    ${PASSWORD_FIELD}    ${password}
    Click Element Safe    ${LOGIN_BUTTON}

    Wait Until Element Is Visible    ${LOGOUT_LINK}    10s

    Input Text Safe    ${SEARCH_BOX}    ${search_item}
    Click Element Safe    ${SEARCH_BUTTON}
    Wait Until Page Contains    ${search_item}    10s

    Click Element Safe    ${FIRST_PRODUCT}
    Wait Until Element Is Visible    ${ADD_TO_CART_BTN}    10s

    Click Element Safe    ${ADD_TO_CART_BTN}
    Wait Until Element Is Visible    ${NOTIFICATION_BAR}    10s
    Element Should Contain    ${NOTIFICATION_BAR}    The product has been added

    Click Element Safe    ${SHOPPING_CART}
    Wait Until Page Contains    ${search_item}    10s

    Clear Element Text    ${QTY_INPUT}
    Input Text Safe    ${QTY_INPUT}    2
    Click Element Safe    ${UPDATE_CART_BTN}
    Wait Until Page Contains    ${search_item}    10s

    Select Checkbox    ${REMOVE_CHECKBOX}
    Click Element Safe    ${UPDATE_CART_BTN}
    Wait Until Page Contains    Your Shopping Cart is empty!    10s

    Click Element Safe    ${LOGOUT_LINK}
    Wait Until Element Is Visible    ${REGISTER_LINK}    10s