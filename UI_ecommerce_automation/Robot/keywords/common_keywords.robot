*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/config.robot

*** Keywords ***
Open Browser To Demo Store
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window

Close Demo Browser
    Close Browser
