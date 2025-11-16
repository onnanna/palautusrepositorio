*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Register Username  pirjo
    Register Password  hyvasalasana1
    Register Password Confirmation  hyvasalasana1
    Click Button  Register
    Register Should Succeed
    

Register With Too Short Username And Valid Password
    Register Username  ma
    Register Password  hyvasalasana2
    Register Password Confirmation  hyvasalasana2
    Click Button  Register
    Register Page Should Be Open


Register With Valid Username And Too Short Password
    Register Username  pekka
    Register Password  lyhyt
    Register Password Confirmation  lyhyt
    Click Button  Register
    Register Page Should Be Open

Register With Valid Username And Invalid Password
    Register Username  laura
    Register Password  salasana
    Register Password Confirmation  salasana
    Click Button  Register
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Register Username  manu
    Register Password  hyvasalasana1
    Register Password Confirmation  hyvasalasana2
    Click Button  Register
    Register Page Should Be Open

Register With Username That Is Already In Use
    Register Username  kalle
    Register Password  hyvasalasana3
    Register Password Confirmation  hyvasalasana3
    Click Button  Register
    Register Page Should Be Open


*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}

Register Username
    [Arguments]  ${username}
    Input Text  name=username  ${username}

Register Password
    [Arguments]  ${password}
    Input Text  name=password  ${password}

Register Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  name=password_confirmation  ${password_confirmation}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!
