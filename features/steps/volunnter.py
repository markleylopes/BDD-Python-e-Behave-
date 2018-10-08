import requests
import behave
import json

@when('I register a Volunnter with the following data , name: {name}, user: {user}, password: {password}, email: {email}, phone: {phone}, address: {address}, cep: {cep}, services: {services}')
def step_volunnterrecord2( context, name, user, password, email, phone, address, cep, services ):

    name = "aongvol"
    user = "aongvol000"
    password = "12345"
    email = "aongvol@volunnter.com.br000"
    phone = "999999987"
    address = "rua joão firmino Régis"
    cep = "57626217"
    services = "corte de cabelo"
    
    global form
    form = {
        "nome": name,
        "usuario": user,
        "senha": password,
        "email": email,
        "fone": [{"numero": phone}],
        "endereco": address,
        "cep": cep,
        "servicos": [{'servicoId': services}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/voluntario", json = form)

    assert r.status_code == 200, 'Error: %s,\n code: %s' % (r.text, r.status_code)

@then('I see that the status code is 200')
def step_volunnterverify_code2(context):
    assert r.status_code == 200, 'Error: %s ' % (r.status_code)

@then('i see that the  volunnter name was recors as volunnterong')
def step_volunnterong_name2(context):
    assert form["nome"] == r.json()['nome']

@then('i sse that the  volunnter user was record as ongvolunnter')
def step_volunnterong_user2(context):
    assert form["usuario"] == r.json()['usuario']

@then('i see that the  volunnter email was record as ong@volunnter.com.br')
def step_volunnterong_email2(context):
    assert form["email"] == r.json()['email']

@then('i see that the  volunnter phone was record as 999999987')
def step_volunnterong_phone2(context):
    assert form['fone'][0]['numero'] == r.json()['fone'][0]['numero']

@then('i see that the  volunnter address was record as rua joão firmino Régis')
def step_volunnterong_address2(context):
    assert form["endereco"] == r.json()['endereco']

@then('i see that the  volunnter cep was record as 57626217')
def step_volunnterong_cep2(context):
    assert form["cep"] == r.json()['cep']

@then('i see that the  volunnter services was record as corte de cabelo')
def step_volunnterong_servico2(context):
    assert form['servicos'][0]['servicoId'] == r.json()['servicos'][0]['servicoId'], 'Error:  %s' % (r.text)

""" Scenario: Volunnter with email already registered """

@when('I re-register a Volunnter with the following data , name: {name}, user: {user}, password: {password}, email: {email}, phone: {phone}, address: {address}, cep: {cep}, services: {services}')
def step_volunnterrecord2_2(context, name, user, password, email, phone, address, cep, services ):

    name = "bongvol"
    user = "bongvol000"
    password = "12345"
    email = "bongvol@volunnter.com.br000"
    phone = "999999987"
    address = "rua joão firmino Régis"
    cep = "57626217"
    services = "corte de cabelo"
    
    global form
    form = {
        "nome": name,
        "usuario": user,
        "senha": password,
        "email": email,
        "fone": [{"numero": phone}],
        "endereco": address,
        "cep": cep,
        "servicos": [{'servicoId': services}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/voluntario", json = form)

    assert r.status_code == 200, 'Error: %s, code: %s' % (r.text, r.status_code)

@when('I re-register a Volunnter with the following data, name: volunnterong, user: ongvolunnter, password: 12345, email: ong@volunnter.com.br, phone: 999999987, address: rua joão firmino Régis, cep: 57626217, services: corte de cabelo')
def step_volunnterrecord2_1_2(context):
    global r
    r = requests.post("https://appelo.herokuapp.com/voluntario", json = form)

    assert r.status_code == 400, 'Error: %s, code: %s' % (r.text, r.status_code)

    
@then('I see that the status code is 400 - p2')
def step_volunnterstatus2(context):
    assert r.status_code == 400, 'Error: : %s, code: %s' % (r.text, r.status_code)

@then('the system returns the following message: {message} - p2')
def step_volunntermessage_volunnter1(context, message):
    message = "O usuário já está sendo usado."
    assert message in r.text, 'Error: : %s, code: %s' % (r.text, r.status_code)

""" Scenario """

@when('I re-register a Volunnter with a different user, and the following data, name: {name}, user: {user}, password: {password}, email: {email}, phone: {phone}, address: {address}, cep: {cep}, services: {services}')
def step_volunnterrecord3_2( context, name, user, password, email, phone, address, cep, services ):

        
    name = "congvol"
    user = "congvol000"
    password = "12345"
    email = "congvol@volunnter.com.br000"
    phone = "999999987"
    address = "rua joão firmino Régis"
    cep = "57626217"
    services = "corte de cabelo"
    
    global form
    form = {
        "nome": name,
        "usuario": user,
        "senha": password,
        "email": email,
        "fone": [{"numero": phone}],
        "endereco": address,
        "cep": cep,
        "servicos": [{'servicoId': services}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/voluntario", json = form)

    assert r.status_code == 200, 'Error: %s, code: %s' % (r.text, r.status_code)

@when('I re-register a Volunnter with the same email, and the following data, name: volunnterong, user: ongvolunnter, password: 12345, email: ong@volunnter.com.br, phone: 999999987, address: rua joão firmino Régis, cep: 57626217, services: corte de cabelo')
def step_volunnterrecord3_1_2(context):

    global r
    form["usuario"] = "dongvol000"
    r = requests.post("https://appelo.herokuapp.com/voluntario", json = form)

    assert r.status_code == 400, 'Error: %s, code: %s' % (r.text, r.status_code)
    
@then('I see that the status code is 400 too - p2')
def step_volunnterstatus2_2(context):
    assert r.status_code == 400, '-----_____ Error: : %s, code: %s' % (r.text, r.status_code)

@then('2 the system returns the following message: {message} - p3')
def step_volunntermessage2_2(context, message):
    message = "O email já está sendo usado."
    assert message in r.text, 'Error: %s, code: %s' % (r.text, r.status_code)