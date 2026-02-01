*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}     Rohith
@{NUMBERS}  1   2   3

*** Test Cases ***
First Test Case
    Log    Hello ${NAME}
    Log To Console    Running First Test Case
    Log    Numbers list: @{NUMBERS}

Second Test Case
    Log    This is the second test case
    Log To Console    Second test Case Executed Successfully
