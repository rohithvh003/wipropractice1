*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Login To Application
    [Arguments]    ${email}    ${password}

    Wait Until Element Is Visible    link:Log in    10s
    Click Link    link:Log in

    Wait Until Element Is Visible    id:Email    10s
    Input Text    id:Email    ${email}
    Input Text    id:Password    ${password}

    Click Button    xpath://input[@value='Log in']
    Wait Until Page Contains    Log out    10s

Logout From Application
    Wait Until Element Is Visible    link:Log out    10s
    Click Link    link:Log out
    Wait Until Page Contains    Log in    10s
