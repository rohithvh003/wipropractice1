*** Settings ***
Library   SeleniumLibrary

*** Keywords ***
Search Product
    [Arguments]    ${product}
    Wait Until Element Is Visible    id:small-searchterms   10s
    Input Text    id:small-searchterms    ${product}
    Sleep    1s
    Click Button    xpath://input[@value='Search']
    Sleep    1s
    Page Should Contain    ${product}

