*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/login_users.csv    dialect=unix    encoding=utf-8
Resource    ../resources/common.resource
Test Template    Remove Item Test
Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Remove Item With CSV Data

*** Keywords ***
Remove Item Test
    [Arguments]    ${email}    ${password}    ${search_item}

    Click Element Safe    xpath://a[text()='Log in']
    Input Text Safe    id:Email    ${email}
    Input Text Safe    id:Password    ${password}
    Click Element Safe    xpath://input[@value='Log in']

    Wait Until Page Contains Element    id:small-searchterms    10s

    Input Text Safe    id:small-searchterms    ${search_item}
    Click Element Safe    xpath://input[@value='Search']

    Click Element Safe    xpath:(//input[@value='Add to cart'])

    Click Element Safe    xpath://span[text()='Shopping cart']

    Wait Until Element Is Visible    xpath://input[@name='removefromcart']    4s

    Select Checkbox    xpath://input[@name='removefromcart']

    Click Element Safe    xpath://a[text()='Log out']
