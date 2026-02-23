*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=../variables/login_users.csv   dialect=unix   encoding=utf-8
Resource          ../resources/common.resource
Test Template     Login User
Suite Setup       Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Login with CSV Data

*** Keywords ***
Login User
    [Arguments]    ${email}    ${password}

    Wait Until Element Is Visible    link:Log in   10s
    Click Link    Log in
    Wait Until Element Is Visible    id:Email   10s
    Input Text    id:Email    ${email}
    Input Text    id:Password    ${password}
    Click Button    xpath://input[@value='Log in']
    Page Should Contain    Log out

    #Logout after each test
    Click Element Safe    xpath://a[text()='Log out']
    Page Should Contain   Log in