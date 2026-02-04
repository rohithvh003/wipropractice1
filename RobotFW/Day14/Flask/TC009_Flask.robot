*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary


*** Variables ***
${baseurl} =  http://127.0.0.1:5000


*** Test Cases ***
Verify Get_user
    Create Session   mysession   ${baseurl}
    ${response}=  GET On Session   mysession   /users
    Status Should Be   200    ${response}
    ${resp.json()}=    To Json    ${response.content}
    log      ${resp.json()}=    console=True


Verify Get Single_user
    Create Session   mysession   ${baseurl}
    ${response}=  GET On Session   mysession   /users/2
    Status Should Be   200    ${response}
    ${res_json}=    To Json    ${response.content}
    log      ${res_json}=    console=True

Create new user
    ${data}=  Create Dictionary   name= karthik
    ${response}=  POST On Session    mysession  /users     json=${data}
    Status Should Be  201   ${response}
    ${res_json}=   To Json   ${response.content}
     log      ${res_json}=    console=True

Verify user-not-found

    ${response}=    GET On Session    Mysession    /users/4
    Status Should Be    200    ${response}
    # ${resp.json}=    To Json    ${response.content} // Deprecated
    Log To Console    ${response.json()}

update user
     ${data}=  Create Dictionary   name= mahesh
    ${response}=  PUT On Session    mysession  /users/2     json=${data}
    Status Should Be  200   ${response}
    ${res_json}=   To Json   ${response.content}
     log      ${res_json}=    console=True

patch user
     ${data}=  Create Dictionary   name= mahesh patched
    ${response}=  PATCH On Session    mysession  /users/2    json=${data}
    Status Should Be  200   ${response}
    ${res_json}=   To Json   ${response.content}
     log      ${res_json}=    console=True

Delete user

     ${data}=  Create Dictionary     name= mahesh patched
    ${response}=  DELETE On Session    mysession  /users/2    json=${data}
    Status Should Be   200   ${response}
    ${res_json}=   To Json   ${response.content}
     log      ${res_json}=    console=True