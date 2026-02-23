*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Login User
    [Arguments]    ${email}    ${password}
    Click Link    Log in
    Wait Until Element Is Visible    id=Email
    Input Text    id=Email        ${email}
    Input Text    id=Password     ${password}
    Click Button    css=input[value="Log in"]
    Wait Until Page Contains Element    css=a[href="/logout"]

Logout User
    Click Link    Log out
    Wait Until Page Contains Element    css=a[href="/login"]
