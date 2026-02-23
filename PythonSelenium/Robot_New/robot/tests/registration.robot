*** Settings ***
Library   SeleniumLibrary
Library   String
Library    DataDriver    file=../variables/test_data.csv    dialect=unix    encoding=utf-8
Resource   ../resources/common.resource
Test Template    Register New User
Suite Setup      Open Browser To Application
Suite Teardown   Close Browser Session

*** Test Cases ***
# Adding ${email} here gives each test a unique name in the log
Registration Test for ${email}

*** Keywords ***
Register New User
     [Arguments]    ${firstname}    ${lastname}    ${email_prefix}    ${password}    ${confirm_password}

     # 1. Open Register Page
     Wait Until Element Is Visible    xpath://a[text()='Register']    10s
     Click Element    xpath://a[text()='Register']

     # 2. Fill Form
     Wait Until Element Is Visible    id:gender-female    5s
     Click Element    id:gender-female

     Input Text       id:FirstName    ${firstname}
     Input Text       id:LastName     ${lastname}

     # 3. Generate Unique Email
     ${random_str}=   Generate Random String   5    [NUMBERS]
     ${final_email}=  Set Variable    ${email_prefix}${random_str}@mail.com
     Input Text       id:Email    ${final_email}

     Input Text       id:Password           ${password}
     Input Text       id:ConfirmPassword    ${confirm_password}

     Click Button     id:register-button

     # 4. Verification
     Wait Until Page Contains    Your registration completed    10s

     # 5. Logout (important for next iteration)
     Click Element    xpath://a[text()='Log out']
     Wait Until Element Is Visible    xpath://a[text()='Register']    5s