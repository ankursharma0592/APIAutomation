# Python API Automation Framework

### Integration Test cases for the Restful Booker
url - https://restful-booker.herokuapp.com/apidoc/index.html
1. Verify GET, POST, PATCH, DELETE, PUT
2. Response Body, Headers, Status Code.
2. Auth - Basic Auth, Cookie Based Auth.
3. JSON Schema Validation.


## Tech Stack(Python Packages used)
1. Request Module
2. PyTest, PyTest-html
3. Allure Report
4. Faker,CSV,JASON, YAML
5. Run via Commandline - Jenkins

#### P.S - DB Connection(in future)

## How to Run via Jenkins?

### Modules needs to be install below packages before execution:
`pip install requests pytest pytest-html faker allure-pytest jsonschema`

## How to run locally ad see the report?
`pytest -v -s test_create_booking.py --html=report.html --alluredir=./repor
ts
`
## if we forget the packages:
`pip freeze > requiermet.txt`

`pip install requirement.txt`

## For Allure report:
1. install node js
2. run `npm i-g allure-commandline` command on cmd

## To check allure installed or not
run on terminal `allure serve allure-result

## Install pytest-sdist module for parallel execution.
` pip install pytest-xdist`

### command for parallel execution
` pytest -n auto parallel -s -v `