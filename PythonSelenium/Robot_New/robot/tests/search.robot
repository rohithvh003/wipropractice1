*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/login_users.csv    dialect=unix    encoding=utf-8
Resource    ../resources/common.resource
Test Template    Search Product Test
Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Search With CSV Data

*** Keywords ***
Search Product Test
    [Arguments]    ${email}    ${password}    ${search_item}

    Click Element Safe    xpath://a[text()='Log in']
    Input Text Safe    id:Email    ${email}
    Input Text Safe    id:Password    ${password}
    Click Element Safe    xpath://input[@value='Log in']

    Input Text Safe    id:small-searchterms    ${search_item}
    Click Element Safe    xpath://input[@value='Search']

    Page Should Contain    ${search_item}

    #logout so next iteration works
    Click Element Safe    xpath://a[text()='Log out']
