#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from get_input import get_input

def menu_sistema():

    print ("#"*30)
    print "\
        1 - Cadastrar usuários\n \
        2 - Acessar o sistema\n \
        3 - Sair do sistema\n"
    option = get_input("Escolha a opção desejada: ")
    return option

def switch(x):
    dict_option = {
    1:cadastro_user,
    2:acesso_sistema,
    3:sair_sistema
    }
    dict_option[x]()


if __name__ == "__main__":
    menu_sistema()
