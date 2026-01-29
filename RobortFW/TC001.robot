#  Created by Rohith at 29-01-2026
*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    firefox
    Maximize Browser Window

*** Test Cases ***
tc001.robot
    Open Application
    Title Should Be    Google
    Close Browser