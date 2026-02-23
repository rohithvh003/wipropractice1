*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/login_users.csv    dialect=unix    encoding=utf-8
Resource    ../resources/common.resource
Test Template    Add To Cart Test
Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session

*** Test Cases ***
Cart With CSV Data

*** Keywords ***
Add To Cart Test
    [Arguments]    ${email}    ${password}    ${search_item}

    Click Element Safe    xpath://a[text()='Log in']

    Input Text Safe    id:Email    ${email}
    Input Text Safe    id:Password    ${password}
    Click Element Safe    xpath://input[@value='Log in']

    Input Text Safe    id:small-searchterms    ${search_item}
    Click Element Safe    xpath://input[@value='Search']


    Click Element Safe    xpath:(//input[@value='Add to cart'])[1]
    Click Element Safe    xpath://span[text()='Shopping cart']

    Page Should Contain    ${search_item}

    #logout so next iteration works
    Click Element Safe    xpath://a[text()='Log out']

