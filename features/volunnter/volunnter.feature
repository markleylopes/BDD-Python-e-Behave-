Feature: Volunnter

    Scenario: Volunnter record
    When I register a Volunnter with the following data , name: "ongvol", user: "ongvol", password: "12345", email: "ongvol@volunnter.com.br", phone: "999999987", address: "rua joão firmino Régis", cep: "57626217", services: "corte de cabelo"
    Then I see that the status code is 200
    And I see that the volunnter name was recors as volunnterong
    And i see that the volunnter user was record as ongvolunnter 
    And I see that the volunnter email was record as ong@volunnter.com.br 
    And I see that the volunnter phone was record as 999999987
    And I see that the volunnter address was record as rua joão firmino Régis
    And I see that the volunnter cep was record as 57626217
    And I see that the volunnter services was record as corte de cabelo   

    Scenario: Volunnter with email already registered
    When I re-register a Volunnter with the following data , name: "volunnterong", user: "ongvolunnter", password: "12345", email: "ong@volunnter.com.br", phone: "999999987", address: "rua joão firmino Régis", cep: "57626217", services: "corte de cabelo"
    And I re-register a Volunnter with the following data, name: volunnterong, user: ongvolunnter, password: 12345, email: ong@volunnter.com.br, phone: 999999987, address: rua joão firmino Régis, cep: 57626217, services: corte de cabelo
    Then I see that the status code is 400 - p2
    And the system returns the following message: "O usuário já está sendo usado." - p2

    Scenario: volunnters with user already registered
    When I re-register a Volunnter with a different user, and the following data, name: "volunnterong", user: "ongvolunnter2", password: "12345", email: "ong@volunnter.com.br", phone: "999999987", address: "rua joão firmino Régis", cep: "57626217", services: "corte de cabelo"
    And I re-register a Volunnter with the same email, and the following data, name: volunnterong, user: ongvolunnter, password: 12345, email: ong@volunnter.com.br, phone: 999999987, address: rua joão firmino Régis, cep: 57626217, services: corte de cabelo
    Then I see that the status code is 400 too - p2
    And 2 the system returns the following message: "O email já está sendo usado."