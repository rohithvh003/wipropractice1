*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}     Robot Framework
${VERSION}  7.1
${COLOUR}   Red  Green  Blue



*** Test Cases ***
Log Scalar Variables
    Log    WelCome to ${NAME}
    Log To Console   Running with version ${VERSION}


Log List Variables
    Log   Available colore : ${COLOUR}
    Log To Console  First color is ${COLOUR}[0]

