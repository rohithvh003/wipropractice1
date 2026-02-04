*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL}          https://demo.automationtesting.in/Register.html
${BROWSER}      chrome

*** Test Cases ***
Fill Mandatory Fields And Submit Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    xpath=//input[@placeholder='First Name']    Ravi
    Input Text    xpath=//input[@placeholder='Last Name']     kumar
    Input Text    xpath=//textarea[@ng-model='Adress']        Banglore
    Input Text    xpath=//input[@type='email']                bhanu@test.com
    Input Text    xpath=//input[@type='tel']                  9876543210
    Click Element    xpath=//input[@value='Male']
    Select From List By Label    id=Skills    Python

    Select From List By Label    id=countries    Select Country
    Select From List By Label    id=yearbox     1998
    Select From List By Label    xpath=//select[@placeholder='Month']    September
    Select From List By Label    id=daybox      10

    Input Text    id=firstpassword    Test@123
    Input Text    id=secondpassword   Test@123
    Sleep    2s

    Close Browser
