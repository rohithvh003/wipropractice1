*** Settings ***
Library   SeleniumLibrary

*** Keywords ***
Search Product
    [Arguments]    ${product}
    Wait Until Element Is Visible    id:small-searchterms
    Input Text    id:small-searchterms    ${product}

    Click Button    xpath://input[@value='Search']

    Page Should Contain    ${product}

