*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}   https://demowebshop.tricentis.com
${BROWSER}    chrome

*** Keywords ***
Open Browser To Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    1s
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