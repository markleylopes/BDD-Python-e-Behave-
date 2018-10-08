Feature: NGO

   Testes nos cenários

    Scenario: NGO record
    When eu cadastro uma ong com os seguintes dados, nome: "NGOong", usuario: "ongngo", senha: "12345", email: "ong@ngo.com.br", cnpj: "999999999999", fone: "999999987", endereco: "rua joão firmino Régis", cep: "57626217", estrutura: "casa com 5 quartos", servicos: "corte de cabelo"
    Then I see that status code is 200
    And i see that ngo name was recors as NGOong
    And i sse that ngo user was record as ongngo 
    And i see that ngo email was record as ong@ngo.com.br 
    And i see that ngo cnpj was record as 999999999999
    And i see that ngo phone was record as 999999987
    And i see that ngo endereco was record as rua joão firmino Régis
    And i see that ngo cep was record as 57626217
    And i see that ngo estrutura was record as casa com 5 quartos
    And i see that ngo servicos was record as corte de cabelo   

    Scenario: NGOs with email already registered
    When eu cadastro uma nova ong com os seguintes dados, nome: "NGOong", usuario: "ongngo", senha: "12345", email: "ong@ngo.com.br", cnpj: "999999999999", fone: "999999987", endereco: "rua joão firmino Régis", cep: "57626217", estrutura: "casa com 5 quartos", servicos: "corte de cabelo"
    And eu cadastro novamente uma ong com os seguintes dados, nome: NGOong, usuario: ongngo, senha: 12345, email: ong@ngo.com.br, cnpj: 999999999999, fone: 999999987, endereco: rua joão firmino Régis, cep: 57626217, estrutura: casa com 5 quartos, servicos: corte de cabelo
    Then I see that status code is 400
    And the system returns the following message: "O usuário já está sendo usado."

    Scenario: NGOs with user already registered
    When eu cadastro uma nova ong, novo usuario com os seguintes dados, nome: "NGOong", usuario: "ongngo2", senha: "12345", email: "ong@ngo.com.br", cnpj: "999999999999", fone: "999999987", endereco: "rua joão firmino Régis", cep: "57626217", estrutura: "casa com 5 quartos", servicos: "corte de cabelo"
    And eu cadastro novamente uma ong, com outro usuario com os seguintes dados, nome: NGOong, usuario: ongngo, senha: 12345, email: ong@ngo.com.br, cnpj: 999999999999, fone: 999999987, endereco: rua joão firmino Régis, cep: 57626217, estrutura: casa com 5 quartos, servicos: corte de cabelo
    Then I see that status code is 400 to
    And 2 the system returns the following message: "O email já está sendo usado."