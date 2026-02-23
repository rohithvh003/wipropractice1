*** Variables ***

# Register Page
${FIRSTNAME}               id=FirstName
${LASTNAME}                id=LastName
${EMAIL}                   id=Email
${PASSWORD_INPUT}          id=Password
${CONFIRM_PASSWORD}        id=ConfirmPassword
${REGISTER_BTN}            id=register-button

# Login Page
${LOGIN_EMAIL}             id=Email
${LOGIN_PASSWORD}          id=Password
${LOGIN_BTN}               css=input[value="Log in"]

# Search Page
${SEARCH_BOX}              id=small-searchterms
${SEARCH_BTN}              css=input[value="Search"]

# Product Page
${FIRST_PRODUCT}           xpath=(//h2[@class="product-title"]/a)[1]
${ADD_TO_CART_DYNAMIC}     css=input[id^="add-to-cart-button"]
${PRODUCT_TITLE}           css=h1
${PRODUCT_PRICE}           css=span[itemprop="price"]

# Cart Page
${SHOPPING_CART_LINK}      link=Shopping cart
${QTY_INPUT}               css=input.qty-input
${UPDATE_CART_BTN}         name=updatecart
${REMOVE_ITEM_CHECKBOX}    name=removefromcart

# Navigation
${REGISTER_LINK}           link=Register
${LOGIN_LINK}              link=Log in
${LOGOUT_LINK}             link=Log out
