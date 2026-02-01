*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Browser Test
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Title Should Be    Google
    sleep  5s
    Capture Page Screenshot    title.png
    Close Browser
