*** Settings ***
Library           SeleniumLibrary

Suite Setup       Suite Level Setup
Suite Teardown    Suite Level Teardown
Test Setup        Test Level Setup
Test Teardown     Test Level Teardown

*** Variables ***
${URL}    https://example.com
${BROWSER}    chrome

*** Test Cases ***
Open Example Site
    [Tags]    smoke    regression
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Example Domain
    sleep   5s
    Close Browser

*** Keywords ***
Suite Level Setup
    Log    ===== Suite Setup Started =====

Suite Level Teardown
    Log    ===== Suite Teardown Completed =====

Test Level Setup
    Log    ==== Test Setup Started ======

Test Level Teardown
    Log     ==== Test Teardown Completed =====
