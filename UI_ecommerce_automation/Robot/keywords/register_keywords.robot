*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Register User From CSV
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${password}

    # Click Register Link safely
    Wait Until Element Is Visible    css=a.ico-register
    Click Element    css=a.ico-register

    # Wait until form loads
    Wait Until Element Is Visible    id=FirstName    timeout=10s

    # Select Gender
    Click Element    id=gender-male

    # Fill Details
    Input Text    id=FirstName    ${first_name}
    Input Text    id=LastName     ${last_name}
    Input Text    id=Email        ${email}
    Input Text    id=Password     ${password}
    Input Text    id=ConfirmPassword     ${password}

    # Click Register
    Click Button    id=register-button

    # Validate Success
    Wait Until Page Contains    Your registration completed
