*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/login_users.csv    dialect=unix    encoding=utf-8
Resource    ../resources/common.resource
Test Template    Product Details Test
Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Product Details With CSV Data

*** Keywords ***
Product Details Test
    [Arguments]    ${email}    ${password}    ${search_item}

    Click Element Safe    xpath://a[text()='Log in']
    Input Text Safe    id:Email    ${email}
    Input Text Safe    id:Password    ${password}
    Click Element Safe    xpath://input[@value='Log in']

    Wait Until Page Contains Element    id:small-searchterms    10s

    Input Text Safe    id:small-searchterms    ${search_item}
    Click Element Safe    xpath://input[@value='Search']

    Click Element Safe    xpath:(//h2[@class='product-title']/a)[1]

    Click Element Safe    xpath://a[text()='Log out']
