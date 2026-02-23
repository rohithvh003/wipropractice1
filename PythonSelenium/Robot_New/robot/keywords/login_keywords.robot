*** Settings ***
Library   SeleniumLibrary
Variables    ../variables/testdata.py

*** Keywords ***
Login To Application
     Wait Until Element Is Visible    link:Log in   10s
     Click Link    Log in
     Sleep    1s
     Wait Until Element Is Visible    id:Email   10s
     Input Text    id:Email    ${EMAIL}
     Sleep    1s
     Input Text    id:Password    ${PASSWORD}
     Sleep    1s
     Click Button    xpath://input[@value='Log in']
     Sleep    2s
     Page Should Contain    Log out

Logout From Application
    Click Link    Log out
    Page Should Contain    Log in

