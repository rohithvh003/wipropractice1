*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/login_users.csv    dialect=unix    encoding=utf-8
Resource    ../resources/common.resource
Test Template    Logout Test
Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Logout With CSV Data

*** Keywords ***
Logout Test
    [Arguments]    ${email}    ${password}

    Click Element Safe    xpath://a[text()='Log in']
    Input Text Safe    id:Email    ${email}
    Input Text Safe    id:Password    ${password}
    Click Element Safe    xpath://input[@value='Log in']

    Click Element Safe    xpath://a[text()='Log out']

    Page Should Contain    Log in
