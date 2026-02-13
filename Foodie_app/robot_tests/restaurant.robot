*** Settings ***
Library    RequestsLibrary
Suite Setup    Setup Data

*** Variables ***
${BASE}    http://127.0.0.1:5000


*** Keywords ***
Setup Data
    Create Session    foodie    ${BASE}

    # ---------------- CREATE RESTAURANT ----------------
    ${rand}=    Evaluate    random.randint(10000,99999)    modules=random
    ${name}=    Set Variable    Robot${rand}
    ${data}=    Create Dictionary    name=${name}
    ${res}=    POST On Session    foodie    /api/v1/restaurants    json=${data}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    $res.json()
    Set Suite Variable    ${RID}    ${json["id"]}

    # ---------------- CREATE DISH ----------------
    ${data}=    Create Dictionary    name=Pizza    type=veg    price=200
    ${res}=    POST On Session    foodie    /api/v1/restaurants/${RID}/dishes    json=${data}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    $res.json()
    Set Suite Variable    ${DID}    ${json["id"]}

    # ---------------- CREATE USER ----------------
    ${rand}=    Evaluate    random.randint(10000,99999)    modules=random
    ${email}=    Set Variable    robot${rand}@mail.com
    ${data}=    Create Dictionary    name=Robot    email=${email}    password=123
    ${res}=    POST On Session    foodie    /api/v1/users/register    json=${data}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    $res.json()
    Set Suite Variable    ${UID}    ${json["id"]}

    # ---------------- PLACE ORDER ----------------
    ${data}=    Create Dictionary    user_id=${UID}    restaurant_id=${RID}
    ${res}=    POST On Session    foodie    /api/v1/orders    json=${data}
    Status Should Be    201    ${res}
    ${json}=    Evaluate    $res.json()
    Set Suite Variable    ${OID}    ${json["id"]}


*** Test Cases ***

View Restaurant
    ${res}=    GET On Session    foodie    /api/v1/restaurants/${RID}
    Status Should Be    200    ${res}


Update Restaurant
    ${data}=    Create Dictionary    location=Delhi
    ${res}=    PUT On Session    foodie    /api/v1/restaurants/${RID}    json=${data}
    Status Should Be    200    ${res}


Update Dish
    ${data}=    Create Dictionary    price=300
    ${res}=    PUT On Session    foodie    /api/v1/dishes/${DID}    json=${data}
    Status Should Be    200    ${res}


Dish Status
    ${data}=    Create Dictionary    enabled=False
    ${res}=    PUT On Session    foodie    /api/v1/dishes/${DID}/status    json=${data}
    Status Should Be    200    ${res}


Delete Dish
    ${res}=    DELETE On Session    foodie    /api/v1/dishes/${DID}
    Status Should Be    200    ${res}


Orders By Restaurant
    ${res}=    GET On Session    foodie    /api/v1/restaurants/${RID}/orders
    Status Should Be    200    ${res}


Orders By User
    ${res}=    GET On Session    foodie    /api/v1/users/${UID}/orders
    Status Should Be    200    ${res}


Give Rating
    ${data}=    Create Dictionary    order_id=${OID}    rating=5    comment=Nice
    ${res}=    POST On Session    foodie    /api/v1/ratings    json=${data}
    Status Should Be    201    ${res}


Admin Approve
    ${res}=    PUT On Session    foodie    /api/v1/admin/restaurants/${RID}/approve
    Status Should Be    200    ${res}


Admin Disable
    ${res}=    PUT On Session    foodie    /api/v1/admin/restaurants/${RID}/disable
    Status Should Be    200    ${res}


Admin Feedback
    ${res}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${res}


Admin Orders
    ${res}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${res}
