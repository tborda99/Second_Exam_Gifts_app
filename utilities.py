from collections import Counter

def check_numero(numero):
    '''
    Dado un numero devuelve TRUE si es un int
    '''
    check = False
    if isinstance(numero,int) == True:
        check = True
    return check

def check_string(nombre):
    '''
    Chequea si el nombre es un string\n
    Devuelve True si es un string
    '''
    check = False
    if isinstance(nombre,str):
        check = True
    return check

def check_usuario_existe(usuario, lista_de_usuarios):
    '''
    Dado una lista de usuarios y un usuario\n
    chequea si existe el usuario
    Devuelve TRUE si existe el usuario
    '''

    check = False
    for i in lista_de_usuarios:
        if i.cedula == usuario:
            check = True
    
    return check



