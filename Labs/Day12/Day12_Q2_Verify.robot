*** Settings ***
Library    BuiltIn
Library    OperatingSystem
Library    SeleniumLibrary

*** Test Cases ***
Verify Environment Setup
    Run    python --version
    Run    robot --version
    ${version}=    Evaluate    __import__('robot').version.get_version()
    Log To Console    Robot Framework Version: ${version}
    Log    All dependencies are installed correctly
