*** Settings ***
Library    Process
Library    SeleniumLibrary


*** Test Cases ***
Check Environment
    ${py}=    Run Process    python    --version    stdout=YES
    Log To Console    Python Installed: ${py.stdout}

    ${rb}=    Run Process    robot    --version    stdout=YES
    Log To Console    Robot Installed: ${rb.stdout}

    ${ver}=    Evaluate    __import__('robot').__version__
    Log To Console    Robot Framework Version: ${ver}
    Log To Console    SeleniumLibrary Imported Successfully