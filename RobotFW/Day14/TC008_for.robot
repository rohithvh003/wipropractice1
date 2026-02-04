*** Test Cases ***
FOR Loop Basic
    FOR    ${item}    IN    one    two    three
        Log    Item: ${item}
    END

#FOR loop with list variable
*** Variables ***
@{COLORS}    Red    Green    Blue

*** Test Cases ***
FOR Loop With List variable
    FOR    ${color}    IN    @{COLORS}
        Log    Color: ${color}
    END

# For loop in Range
*** Test Cases ***
FOR Loop Range
    FOR  ${i}    IN RANGE  1  6
        Log  Number:${i}

    END

#For loop -with steps
*** Test Cases ***
FOR Loop With Step
    FOR   ${i}    IN RANGE    0    10    2
        Log    Value: ${i}
    END

#For loop -Enumerate
*** Test Cases ***
FOR Loop Enumerate
    FOR  ${index}  ${Value}  IN ENUMERATE   a  b  c
        Log  ${index}=${value}

    END