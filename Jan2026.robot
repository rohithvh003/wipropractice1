*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.*** Settings ***

Library
    SeleniumLibrary

*** Variables ***
${URL}            https://www.google.com
${BROWSER} chrome    \
${MESSAGE} Hello, world!    \

*** Test Cases ***
Valid Login
    Open Login Page
    Input Username    demo
    Input Password    mode
    Submit Credentials
    Welcome Page Should Be Open

Setting Variables
    Do Something    first argument    second argument
    ${value}=    Get Some Value
    Should Be Equal    ${value}    Expected value

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Input Username
    [Arguments]    ${username}
    Log    Username entered: ${username}

Input Password
    [Arguments]    ${password}
    Log    Password entered: ${password}

Submit Credentials
    Log    Submitting credentials

Welcome Page Should Be Open
    Title Should Be    Google
    Log    ${MESSAGE}
    Close Browser

Do Something
    [Arguments]    ${arg1}    ${arg2}
    Log    First=${arg1}, Second=${arg2}

Get Some Value
    [Return]    Expected value

google.com
    chrome
    Maximize Browser Window

*** Test Cases ***
TC001_robot
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Log    ${MESSAGE}
    Sleep    5s
    Close Browser

*** Variables ***
${MESSAGE}        Hello, world!
