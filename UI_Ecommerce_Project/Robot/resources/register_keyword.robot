*** Settings ***
Library   SeleniumLibrary
Library   String

*** Keywords ***
Register New User
    Click Link    Register
    Wait Until Element Is Visible    id:FirstName    10s

    Click Element    id:gender-male
    Input Text    id:FirstName    Rohit
    Input Text    id:LastName     Krishna

    ${random}=   Generate Random String   5    [NUMBERS]
    ${email}=    Set Variable    test${random}@mail.com

    Input Text    id:Email            ${email}
    Input Text    id:Password         Test@1234
    Input Text    id:ConfirmPassword  Test@1234

    Click Button    id:register-button
    Wait Until Page Contains    Your registration completed    10s
