import requests
import behave
import json

@when('eu cadastro uma ong com os seguintes dados, nome: {nome}, usuario: {usuario}, senha: {senha}, email: {email}, cnpj: {cnpj}, fone: {fone}, endereco: {endereco}, cep: {cep}, estrutura: {estrutura}, servicos: {servicos}')
def step_record(context, nome, usuario, senha, email, cnpj, fone, endereco, cep, estrutura, servicos ):
    nome = "NGOong"
    usuario = "ngoong003"
    senha = "12345"
    email = "ngoong003@ngo.com.br"
    cnpj = "999999999999"
    fone = "999999987"
    endereco = "rua joão firmino Régis"
    cep = "57626217"
    estrutura = "casa com 5 quartos"
    servicos = "corte de cabelo"
    global formulario
    formulario = {
        "nome": nome,
        "usuario": usuario,
        "senha": senha,
        "email": email,
        "cnpj": cnpj,
        "fone": [{"numero": fone}],
        "endereco": endereco,
        "cep": cep,
        "estruturas": [{'name': estrutura}],
        "servicos": [{'servicoId': servicos}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/ong", json = formulario)

    assert r.status_code == 200, '_+_+_+_ Erro é: %s, code: %s' % (r.text, r.status_code)

@then('I see that status code is 200')
def step_verify_code(context):
    assert r.status_code == 200, 'Código de erro: %s ' % (r.status_code)

@then('i see that ngo name was recors as NGOong')
def step_ong_name(context):
    assert formulario["nome"] == r.json()['nome']

@then('i sse that ngo user was record as ongngo')
def step_ong_user(context):
    assert formulario["usuario"] == r.json()['usuario']

@then('i see that ngo email was record as ong@ngo.com.br')
def step_ong_email(context):
    assert formulario["email"] == r.json()['email']

@then('i see that ngo cnpj was record as 999999999999')
def step_ong_cnpj(context):
    assert formulario["cnpj"] == r.json()['cnpj']

@then('i see that ngo phone was record as 999999987')
def step_ong_phone(context):
    assert formulario['fone'][0]['numero'] == r.json()['fone'][0]['numero']

@then('i see that ngo endereco was record as rua joão firmino Régis')
def step_ong_address(context):
    assert formulario["endereco"] == r.json()['endereco']

@then('i see that ngo cep was record as 57626217')
def step_ong_cep(context):
    assert formulario["cep"] == r.json()['cep']

@then('i see that ngo estrutura was record as casa com 5 quartos')
def step_ong_place(context):
    assert formulario['estruturas'][0]['name'] == r.json()['estruturas'][0]['name'], 'ERRO é %s' % (r.text)

@then('i see that ngo servicos was record as corte de cabelo')
def step_ong_servico(context):
    assert formulario['servicos'][0]['servicoId'] == r.json()['servicos'][0]['servicoId'], 'ERRO é %s' % (r.text)

""" Scenario """

@when('eu cadastro uma nova ong com os seguintes dados, nome: {nome}, usuario: {usuario}, senha: {senha}, email: {email}, cnpj: {cnpj}, fone: {fone}, endereco: {endereco}, cep: {cep}, estrutura: {estrutura}, servicos: {servicos}')
def step_record2(context, nome, usuario, senha, email, cnpj, fone, endereco, cep, estrutura, servicos ):
    nome = "NGOong"
    usuario = "angoong003"
    senha = "12345"
    email = "angoong003g@ngo.com.br"
    cnpj = "999999999999"
    fone = "999999987"
    endereco = "rua joão firmino Régis"
    cep = "57626217"
    estrutura = "casa com 5 quartos"
    servicos = "corte de cabelo"
    global formulario
    formulario = {
        "nome": nome,
        "usuario": usuario,
        "senha": senha,
        "email": email,
        "cnpj": cnpj,
        "fone": [{"numero": fone}],
        "endereco": endereco,
        "cep": cep,
        "estruturas": [{'name': estrutura}],
        "servicos": [{'servicoId': servicos}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/ong", json = formulario)

    assert r.status_code == 200, '_+_+_+_ Erro é: %s, code: %s' % (r.text, r.status_code)

@when('eu cadastro novamente uma ong com os seguintes dados, nome: NGOong, usuario: ongngo, senha: 12345, email: ong@ngo.com.br, cnpj: 999999999999, fone: 999999987, endereco: rua joão firmino Régis, cep: 57626217, estrutura: casa com 5 quartos, servicos: corte de cabelo')
def step_record2_1(context):
    global r
    r = requests.post("https://appelo.herokuapp.com/ong", json = formulario)

    assert r.status_code == 400, '____---- Erro é: %s, code: %s' % (r.text, r.status_code)

    
@then('I see that status code is 400')
def step_status(context):
    assert r.status_code == 400, '-----_____ Erro é: %s, code: %s' % (r.text, r.status_code)

@then('the system returns the following message: {message}')
def step_message(context, message):
    message = "O usuário já está sendo usado."
    assert message in r.text, '-----_____ Erro é: %s, code: %s' % (r.text, r.status_code)

""" Scenario """

@when('eu cadastro uma nova ong, novo usuario com os seguintes dados, nome: {nome}, usuario: {usuario}, senha: {senha}, email: {email}, cnpj: {cnpj}, fone: {fone}, endereco: {endereco}, cep: {cep}, estrutura: {estrutura}, servicos: {servicos}')
def step_record3(context, nome, usuario, senha, email, cnpj, fone, endereco, cep, estrutura, servicos ):
    nome = "NGOong"
    usuario = "bngoong003"
    senha = "12345"
    email = "bngoong003@ngo.com.br"
    cnpj = "999999999999"
    fone = "999999987"
    endereco = "rua joão firmino Régis"
    cep = "57626217"
    estrutura = "casa com 5 quartos"
    servicos = "corte de cabelo"
    global formulario
    formulario = {
        "nome": nome,
        "usuario": usuario,
        "senha": senha,
        "email": email,
        "cnpj": cnpj,
        "fone": [{"numero": fone}],
        "endereco": endereco,
        "cep": cep,
        "estruturas": [{'name': estrutura}],
        "servicos": [{'servicoId': servicos}]
    }
    global r
    r = requests.post("https://appelo.herokuapp.com/ong", json = formulario)

    assert r.status_code == 200, '_+_+_+_ Erro é: %s, code: %s' % (r.text, r.status_code)

@when('eu cadastro novamente uma ong, com outro usuario com os seguintes dados, nome: NGOong, usuario: ongngo, senha: 12345, email: ong@ngo.com.br, cnpj: 999999999999, fone: 999999987, endereco: rua joão firmino Régis, cep: 57626217, estrutura: casa com 5 quartos, servicos: corte de cabelo')
def step_record3_1(context):
    global r
    formulario["usuario"] = "cngoong003"
    r = requests.post("https://appelo.herokuapp.com/ong", json = formulario)

    assert r.status_code == 400, '____---- Erro é: %s, code: %s' % (r.text, r.status_code)

    
@then('I see that status code is 400 to')
def step_status2(context):
    assert r.status_code == 400, '-----_____ Erro é: %s, code: %s' % (r.text, r.status_code)

@then('2 the system returns the following message: {message}')
def step_message2(context, message):
    message = "O email já está sendo usado."
    assert message in r.text, '-----_____ Erro é: %s, code: %s' % (r.text, r.status_code)