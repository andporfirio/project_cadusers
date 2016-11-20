#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from get_input import get_input
from getpass import getpass
from sql import connsql

def cadusers():
    users = {
    'nome':'',
    'sobrenome':'',
    'login':'',
    'senha':'',
    'conf_senha':'',
    }

    print("#" * 30)
    print("Cadastro de Usuários.")
    print("Precione 'q' para sair.")
    print("#" * 30)

    while True:
        users['nome'] = get_input("Digite o nome do usuário: ")
        if users['nome'] == 'q':
            break
            users.clean()
    
        users['sobrenome'] = get_input("Digite o sobrenome do usuário: ")
        if users['sobrenome'] == 'q':
            break
            users.clean()

        users['login'] = get_input("Digite o login do usuário: ")
        if users['login'] == 'q':
            break
            users.clean()

        users['senha'] = getpass("Digite a senha do usuário: ")
        if users['login'] == 'q':
            break
            users.clean()

        users['conf_senha'] = getpass("Confirme a senha do usuário: ")
        if users['login'] == 'q':
            break
            users.clean()
        
        save = get_input("Deseja salvar as informações do usuário? 's'/'n': ")
        if save == 's':
            colunas = users.keys()
            values = users.values()
            insert_info = ("INSERT INTO Users (%s) VALUES ('%s')" %
            (",".join(colunas),"','".join(values)))
            print(insert_info)
            connsql("Use Users")
            connsql(insert_info)
            print("Dados salvos com sucesso!") 
        else:
            break
           
cadusers()
