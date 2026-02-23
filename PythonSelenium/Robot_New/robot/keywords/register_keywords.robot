*** Settings ***
Library   SeleniumLibrary
Library   String


*** Keywords ***
Register New User
    Click Link    Register
    Sleep    1s
    Click Element    id:gender-female
    Sleep    1s
    Input Text    id:FirstName    Pavani
    Sleep    1s
    Input Text    id:LastName    Krishna
    Sleep    1s

    ${random}=   Generate Random String   5    [NUMBERS]
    ${email}=    Set Variable    test${RANDOM}@mail.com
    Input Text    id:Email    ${email}
    Sleep    1s
    Input Text    id:Password    Test@1234
    Sleep    1s
    Input Text    id:ConfirmPassword    Test@1234
    Sleep    1s
    Click Button    id:register-button
    Sleep    2s
    Page Should Contain    Your registration completed
