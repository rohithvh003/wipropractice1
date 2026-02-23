*** Settings ***
Library    SeleniumLibrary
Library    DataDriver     ../variables/users.csv
Resource   ../keywords/common_keywords.robot
Resource   ../keywords/register_keywords.robot

Suite Setup       Open Browser To Demo Store
Suite Teardown    Close Demo Browser
Test Template     Register Flow

*** Test Cases ***
Register Users From CSV  ${first_name} ${last_name} ${email} ${password}

*** Keywords ***
Register Flow
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${password}
    Register User From CSV   ${first_name}    ${last_name}    ${email}    ${password}
