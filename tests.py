import requests

def test_rene():
    file = open("example_data/exampleRENE.txt")
    content = file.read()
    response = requests.post(
                'http://localhost:8000/payments/api', data={"employee_data": content})
    response = response.json()
    message = response.get('message')
    assert message == "The amount to pay RENE is: 215.0 USD"

def test_astrid():
    file = open("example_data/exampleASTRID.txt")
    content = file.read()
    response = requests.post(
                'http://localhost:8000/payments/api', data={"employee_data": content})
    response = response.json()
    message = response.get('message')
    assert message == "The amount to pay ASTRID is: 85.0 USD"

def test_federico():
    file = open("example_data/exampleFEDERICO.txt")
    content = file.read()
    response = requests.post(
                'http://localhost:8000/payments/api', data={"employee_data": content})
    response = response.json()
    message = response.get('message')
    assert message == "The amount to pay FEDERICO is: 290.0 USD"

def test_wrong():
    file = open("example_data/exampleWrong.txt")
    content = file.read()
    response = requests.post(
                'http://localhost:8000/payments/api', data={"employee_data": content})
    response = response.json()
    message = response.get('message')
    assert message == None