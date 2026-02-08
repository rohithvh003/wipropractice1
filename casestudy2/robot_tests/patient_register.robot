*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Registration Page
Suite Teardown    Close Browser

*** Keywords ***
Open Registration Page
    ${path}=    Set Variable    ${CURDIR}/../web/register.html
    Open Browser    file://${path}    chrome
    Maximize Browser Window

*** Test Cases ***
Register Patient
    Wait Until Element Is Visible    id=name    10s
    Input Text    id=name     Akash
    Input Text    id=age      22
    Click Element    id=male
    Input Text    id=contact  9999999999
    Input Text    id=disease  Fever
    Select From List By Label    id=doctor    Dr. Smith
    Click Button    Register
