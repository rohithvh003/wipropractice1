*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE}    http://127.0.0.1:5000


*** Test Cases ***
End To End Flow

    Create Session    foodie    ${BASE}

    # ==========================================
    # Create Restaurant
    # ==========================================
    ${rand}=    Evaluate    random.randint(1000,9999)    modules=random
    ${rname}=    Set Variable    Hotel${rand}

    ${rdata}=    Create Dictionary
    ...    name=${rname}
    ...    category=Indian
    ...    location=City
    ...    contact=999

    ${res}=    POST On Session    foodie    /api/v1/restaurants    json=${rdata}
    Status Should Be    201    ${res}

    ${body}=    Set Variable    ${res.json()}
    ${RID}=    Set Variable    ${body["id"]}

    # ==========================================
    # Add Dish
    # ==========================================
    ${ddata}=    Create Dictionary
    ...    name=Pizza
    ...    price=200

    ${res}=    POST On Session    foodie    /api/v1/restaurants/${RID}/dishes    json=${ddata}
    Status Should Be    201    ${res}

    # ==========================================
    # Register User
    # ==========================================
    ${email}=    Set Variable    user${rand}@mail.com

    ${udata}=    Create Dictionary
    ...    name=User${rand}
    ...    email=${email}
    ...    password=123

    ${res}=    POST On Session    foodie    /api/v1/users/register    json=${udata}
    Status Should Be    201    ${res}

    ${body}=    Set Variable    ${res.json()}
    ${UID}=    Set Variable    ${body["id"]}

    # ==========================================
    # Place Order
    # ==========================================
    ${item}=    Create Dictionary    name=Pizza    qty=2
    ${items}=    Create List    ${item}

    ${odata}=    Create Dictionary
    ...    user_id=${UID}
    ...    restaurant_id=${RID}
    ...    items=${items}

    ${res}=    POST On Session    foodie    /api/v1/orders    json=${odata}
    Status Should Be    201    ${res}

    ${body}=    Set Variable    ${res.json()}
    ${OID}=    Set Variable    ${body["id"]}

    # ==========================================
    # Orders by User
    # ==========================================
    ${res}=    GET On Session    foodie    /api/v1/users/${UID}/orders
    Status Should Be    200    ${res}

    # ==========================================
    # Orders by Restaurant
    # ==========================================
    ${res}=    GET On Session    foodie    /api/v1/restaurants/${RID}/orders
    Status Should Be    200    ${res}

    # ==========================================
    # Give Rating
    # ==========================================
    ${rating}=    Create Dictionary
    ...    order_id=${OID}
    ...    rating=5
    ...    comment=Good

    ${res}=    POST On Session    foodie    /api/v1/ratings    json=${rating}
    Status Should Be    201    ${res}

    # ==========================================
    # Admin Feedback
    # ==========================================
    ${res}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${res}

    # ==========================================
    # Admin Orders
    # ==========================================
    ${res}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${res}
