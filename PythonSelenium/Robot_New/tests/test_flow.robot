*** Settings ***
Library    SeleniumLibrary
Library    DataDriver       file=variables/user.csv
Resource   ../resources/config.robot

Suite Setup       Open Browser To Demo Store
Suite Teardown    Close Browser
Test Template     Complete User Journey


*** Test Cases ***
Full End To End Flow
    [Tags]    datadriven



*** Keywords ***
Open Browser To Demo Store
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window


Complete User Journey
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${password}    ${product}

    ### REGISTER ###
    Wait Until Element Is Visible    css=a.ico-register
    Click Element    css=a.ico-register
    Wait Until Element Is Visible    id=FirstName

    Click Element    id=gender-male
    Input Text    id=FirstName    ${first_name}
    Input Text    id=LastName     ${last_name}
    Input Text    id=Email        ${email}
    Input Text    id=Password     ${password}
    Input Text    id=ConfirmPassword     ${password}
    Click Button    id=register-button

    Wait Until Page Contains    Your registration completed

    ### LOGOUT AFTER REGISTER ###
    Click Element    css=a.ico-logout
    Wait Until Page Contains Element    css=a.ico-login

    ### LOGIN ###
    Click Element    css=a.ico-login
    Wait Until Element Is Visible    id=Email
    Input Text    id=Email    ${email}
    Input Text    id=Password    ${password}
    Click Button    css=input[value="Log in"]
    Wait Until Page Contains Element    css=a.ico-logout

    ### SEARCH PRODUCT ###
    Input Text    id=small-searchterms    ${product}
    Click Button    css=input[value="Search"]
    Wait Until Page Contains    ${product}

    ### OPEN FIRST PRODUCT ###
    Click Element    xpath=(//h2[@class="product-title"]/a)[1]
    Wait Until Page Contains Element    css=input[value="Add to cart"]

    ### ADD TO CART ###
    Click Button    css=input[value="Add to cart"]
    Wait Until Page Contains    The product has been added

    ### OPEN CART ###
    Click Element    css=a.ico-cart
    Wait Until Page Contains    Shopping cart

    ### LOGOUT ###
    Click Element    css=a.ico-logout
    Wait Until Page Contains Element    css=a.ico-login
