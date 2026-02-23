*** Settings ***
Documentation    DataDriver Testing with Excel
Library     DataDriver     data.csv
Library     SeleniumLibrary
Suite Setup        Open The Browser
Suite Teardown    Close Browser
Test Setup        Launch URL

Test Template    Read All The Data


*** Variables ***
${URL}            https://demoqa.com/text-box
${FULLNAME}       id:userName
${EMAILADD}       id:userEmail
${CURRENTADD}     id:currentAddress
${PERMANENTADD}   id:permanentAddress
${SUBMIT_BTN}     id:submit
${NAMEVERIFY}     id:name


*** Test Cases ***
Fill Form With Data


*** Keywords ***
Read All The Data
    [Arguments]    ${username}    ${email}    ${currentAddress}    ${permanentAddress}
    Input Text    ${FULLNAME}    ${username}
    Input Text    ${EMAILADD}    ${email}
    Input Text    ${CURRENTADD}    ${currentAddress}
    Input Text    ${PERMANENTADD}    ${permanentAddress}
    Click Button    ${SUBMIT_BTN}

*** Keywords ***
Open The Browser
    Open Browser    https://demoqa.com/text-box    chrome
    Maximize Browser Window

Launch URL
    Go To    https://demoqa.com/text-box



