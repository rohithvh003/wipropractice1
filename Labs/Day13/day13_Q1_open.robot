*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}        https://www.google.com
${TITLE}      Google

*** Test Cases ***
Open Browser And Verify Title
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    ${TITLE}
    sleep  5s
    Capture Page Screenshot
    Close Browser
