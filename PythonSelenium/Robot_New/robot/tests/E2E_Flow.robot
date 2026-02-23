*** Settings ***
Library    SeleniumLibrary
Library    String
Library    DataDriver    file=../variables/users.csv    dialect=unix    encoding=utf-8
Resource   ../resources/common.resource
Suite Setup      Open Browser To Application
Suite Teardown   Close Browser Session

*** Test Cases ***
E2E Flow for user ${firstname}
    [Template]    Complete User Flow

*** Keywords ***
Complete User Flow
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${password}    ${confirm_password}    ${search_item}
    Log    ${firstname}
#Register
    Log    Clicking on Register Link
    Element Should Be Visible    xpath://a[text()='Register']

    Click Element    xpath://a[text()='Register']

    Page Should Contain    Register

    Click Element    id:gender-female

    Log    Entering Firstname
    Element Should Be Visible    id:FirstName
    Input Text    id:FirstName    ${firstname}

    Log    Entering Lastname
    Element Should Be Visible    id:LastName
    Input Text    id:LastName     ${lastname}

    ${random}=    Generate Random String    4    [NUMBERS]
    ${generated_email}=     Set Variable    ${email}${random}@mail.com

    Log    Entering Email
    Element Should Be Visible    id:Email
    Input Text    id:Email    ${generated_email}

    Log    Entering Password
    Element Should Be Visible    id:Password
    Input Text    id:Password    ${password}

    Log    Entering Confirm Password
    Element Should Be Visible    id:ConfirmPassword
    Input Text    id:ConfirmPassword    ${confirm_password}

    Click Button    id:register-button

    Log     Registration Successful
    Page Should Contain    Your registration completed
#log in
    Log    Logging out after registration
    Click Element    xpath://a[text()='Log out']

    Log    Logging in with registered credentials
    Click Element    xpath://a[text()='Log in']
    Input Text    id:Email    ${generated_email}
    Input Text    id:Password    ${password}
    Click Button    xpath://input[@value='Log in']

    Element Should Be Visible    xpath://a[text()='Log out']
#search product
    Log    Search bar should be visible
    Element Should Be Visible    id:small-searchterms

    Log    Entering search product
    Input Text    id:small-searchterms    ${search_item}

    Click Element    xpath://input[@value='Search']

    Log    Verifying search results
    Page Should Contain    ${search_item}
#product Deatils
    Log    Opening product details
    Click Element    xpath:(//h2[@class='product-title']/a)[1]

    Element Should Be Visible    xpath://input[@value='Add to cart']

#add to cart
    Click Element    xpath://input[@value='Add to cart']

    Wait Until Element Is Visible    id:bar-notification    10s
    Element Should Contain    id:bar-notification    The product has been added
    Log    The product has been added to the cart

    Click Element    xpath://span[text()='Shopping cart']

    Page Should Contain    ${search_item}
#update cart
    Log    Updating quantity
    Element Should Be Visible    xpath://input[contains(@class,'qty-input')]
    Clear Element Text    xpath://input[contains(@class,'qty-input')]
    Input Text    xpath://input[contains(@class,'qty-input')]    2

    Click Element    xpath://input[@name='updatecart']

    Page Should Contain    ${search_item}
#Remove Item
    Log    Removing item from cart
    Select Checkbox    xpath://input[@name='removefromcart']
    Click Element    xpath://input[@name='updatecart']

    Page Should Contain    Your Shopping Cart is empty!
#logout
    Log    Logging out
    Element Should Be Visible    xpath://a[text()='Log out']
    Click Element    xpath://a[text()='Log out']

    Element Should Be Visible    xpath://a[text()='Register']
