from Entities.libro import Libro
from Entities.producto import Producto
from Entities.regalo import Regalo
from Entities.usuario import Usuario
from Entities.vestimenta import Vestimenta
from utilities import check_string,check_numero,check_usuario_existe
from Exceptions.entidad_no_existe import EntidadNoExiste
from Exceptions.entidad_ya_existe import EntidadYaExiste
from Exceptions.informacion_invalida import InformacionInvalida
from Exceptions.regalo_no_disponible import RegaloNoDisponible

class AppListaDeDeseos():

    def __init__(self):
        self._usuarios = []

    def crear_usuario(self,cedula, nombre, telefono):

        if cedula is None or nombre is None or telefono is None:
            print('Hay datos incorrectos')
            raise InformacionInvalida

        else:
            if check_numero(cedula) == True and check_numero(telefono) == True and check_string(nombre) == True:
                
                if check_usuario_existe(cedula,self._usuarios) == False:
                    #El usuario no existe aun, lo agrego
                    self._usuarios.append(Usuario(cedula,nombre,telefono))
                
                else:
                    #Ya existe usuario
                    print('Ya existe el usuario')
                    raise EntidadYaExiste
                    

            else:
                print('Hay datos incorrectos')
                raise InformacionInvalida
            



    def agregar_producto_a_lista_deseo(self,cedula_usuario, tipo, nombre, precio_promedio, talle = None, color = None, autores = None):

        if cedula_usuario is None or tipo is None or nombre is None or precio_promedio is None:

            print('Hay datos incorrectos')
            raise InformacionInvalida
        
        else:
            if check_numero(cedula_usuario) == True and check_numero(precio_promedio) == True and check_string(nombre) == True and check_string(tipo):
                
                if check_usuario_existe(cedula_usuario,self._usuarios) == True:

                    if tipo.lower() == 'libro':
                        if autores is not None:
                            if check_string(autores) == True:

                                #LIBROS OK AGREGO
                                for usuario in self._usuarios:
                                    if usuario.cedula == cedula_usuario:
                                        usuario.listaDeseos.append(Libro(nombre,precio_promedio,autores))

                            else:
                                print('Hay datos incorrectos')
                                raise InformacionInvalida

                        else:
                            print('Hay datos incorrectos')
                            raise InformacionInvalida
                    
                    elif tipo.lower() == 'vestimenta':

                        if talle is None or color is None:
                            print('Hay datos incorrectos')
                            raise InformacionInvalida
                        
                        else:
                            if check_string(talle) == True and check_string(color):

                                #VESTIMENTA OK AGREGO
                                for usuario in self._usuarios:
                                    if usuario.cedula == cedula_usuario:
                                        usuario.listaDeseos.append(Vestimenta(nombre,precio_promedio,talle,color))
                            

                            else:
                                print('Hay datos incorrectos')
                                raise InformacionInvalida

                    
                    else:
                        print('Hay datos incorrectos')
                        raise InformacionInvalida

                else:
                    print('Ya existe el usuario')
                    raise EntidadYaExiste

            else:
                print('Hay datos incorrectos')
                raise InformacionInvalida

        

    def registrar_regalo(self,cedula_origen, cedula_destino_regalo, nombre_producto):
        if cedula_origen is None or cedula_destino_regalo is None or nombre_producto is None:
            print('Hay datos incorrectos')
            raise InformacionInvalida
        
        else:
            if check_numero(cedula_origen) == True  and check_numero(cedula_destino_regalo) == True and check_string(nombre_producto) == True:
                
                if check_usuario_existe(cedula_origen,self._usuarios) == True and check_usuario_existe(cedula_destino_regalo,self._usuarios) == True:
                    #Chequeo si esta en la lista de deseos del usuario
                    lo_quiere = False
                    for usuario in self._usuarios:
                        if usuario.cedula == cedula_destino_regalo:
                            for regalo in usuario.listaDeseos:
                                if regalo.nombre.lower() == nombre_producto.lower():
                                    lo_quiere = True
                                    instancia_de_regalo = regalo
                    
                    
                    if lo_quiere == True:

                        #chequeo si ya se lo regalaron
                        ya_regalado = False
                        for usuario in self._usuarios:
                            if usuario.cedula == cedula_destino_regalo:
                                for regalo in usuario.deseos_satisfechos:
                                    if regalo.lower() == nombre_producto.lower():
                                        ya_regalado = True
                        
                        if ya_regalado == True:
                            print('Regalo ya fue regalado por otro usuario')
                            raise RegaloNoDisponible

                        else:
                            #Todo ok para que lo regale

                            #Agrego a lista de deseos satisfechos
                            for usuario in self._usuarios:
                                if usuario.cedula == cedula_destino_regalo:
                                    usuario.deseos_satisfechos.append(nombre_producto)
                            
                            #Agrego a la lista de regalos del que regala
                            for usuario in self._usuarios:
                                if usuario.cedula == cedula_origen:
                                    usuario.regalos.append(Regalo(cedula_destino_regalo))
                            
                            for usuario in self._usuarios:
                                if usuario.cedula == cedula_origen:
                                    for regalo in usuario.regalos:
                                        if cedula_destino_regalo == regalo.amigo:
                                            regalo.regalos.append(instancia_de_regalo)
                            
                    
                    else:
                        print('El usuario no quiere ese regalo, sos un mal amigo')
                        raise RegaloNoDisponible


                
                else:
                    print('Usuario no registrado')
                    raise EntidadNoExiste




            else:
                print('Hay datos incorrectos')
                raise InformacionInvalida


    def obtener_productos_mas_regalados(self):
        '''
        "Daniel: Los productos que más desean los usuarios\n
        ignorar el nombre de la función"
        '''
        lista_deseados = []
        for usuario in self._usuarios:
            for deseo in usuario.listaDeseos:
                lista_deseados.append(deseo.nombre)

        top3 = []
        i = 1
        while i <= 3:
            top = max(set(lista_deseados), key = lista_deseados.count)
            if top not in top3:
                top3.append(top)

            lista_deseados.remove(top)

            i += 1
        
        return top3


    def obtener_usuarios_amantes_de_libros(self):

        lista_desean_libros = []
        lista_regalaron_libros = []

        #Desean regalos
        for usuario in self._usuarios:
            for deseo in usuario.listaDeseos:
                if isinstance(deseo, Libro):
                    lista_desean_libros.append(usuario.cedula)

        libros = []
        for usuario in self._usuarios:
            for deseo in usuario.listaDeseos:
                if isinstance(deseo, Libro):
                    libros.append(deseo)
        
                    
        for usuario in self._usuarios:
            for regalo in usuario.regalos:
                for i in regalo.regalos:
                    for j in libros:
                        if i.nombre == j.nombre:
                            lista_regalaron_libros.append(usuario.cedula)
              
        

        #Pueden haber repetidos
        lista_desean_libros = list(set(lista_desean_libros)) #si lo transformo en tuple quedan solo unicos
        lista_regalaron_libros = list(set(lista_regalaron_libros))

        lista_final =[]
        for persona in lista_regalaron_libros:
            if persona in lista_desean_libros:
                lista_final.append(persona)
        
        return lista_final




if __name__ == '__main__':
    
    #PRUEBAS
    print('\n PRUEBAS')

    #Creo datos
    app = AppListaDeDeseos()

    #Crear Usuarios
    app.crear_usuario(51434026, 'Tomás Bordaberry', 26017244)
    app.crear_usuario(12345678, 'John Doe 1', 26017244)
    app.crear_usuario(12234567, 'John Doe 2', 26017244)
    app.crear_usuario(11234567, 'John Doe 3', 26017244)
    app.crear_usuario(12334567, 'John Doe 4', 26017244)
    app.crear_usuario(12344567, 'John Doe 5', 26017244)
    app.crear_usuario(12345567, 'John Doe 6', 26017244)
    app.crear_usuario(12345667, 'John Doe 7', 26017244)

    #Agregar Deseos
    #Deseos Tomás
    app.agregar_producto_a_lista_deseo(51434026,'vestimenta','remera blanca',200,'M','blanca')
    app.agregar_producto_a_lista_deseo(51434026,'vestimenta','remera azul',200,'M','azul')
    app.agregar_producto_a_lista_deseo(51434026,'libro','The psychology of money',400,None,None,'Morgan Housel')
    app.agregar_producto_a_lista_deseo(51434026,'libro','Atomic Habits',400,None,None,'James Clear')

    #Deseos John Doe 1
    app.agregar_producto_a_lista_deseo(12345678,'libro','Atomic Habits',400,None,None,'James Clear')
    app.agregar_producto_a_lista_deseo(12345678,'vestimenta','remera blanca',200,'M','blanca')

    #Deseos John Doe 2
    app.agregar_producto_a_lista_deseo(12234567,'vestimenta','remera blanca',200,'M','blanca')
    app.agregar_producto_a_lista_deseo(12234567,'libro','The psychology of money',400,None,None,'Morgan Housel')


    app.registrar_regalo(12345678,51434026,'The psychology of money')
    app.registrar_regalo(12234567,51434026,'Atomic Habits')
    app.registrar_regalo(51434026,12345678,'Atomic Habits')



    #EXCEPTIONS
    print('\n PRUEBAS DE EXCEPTIONS:\n ')

    #Prueba 1
    prueba1 = 'Mal'
    try:
        app.crear_usuario(51434026, 'Tomás Bordaberry', 26017244)
    
    except EntidadYaExiste:
        prueba1 = 'OK'

    finally:
        print(f'Prueba 1 {prueba1}')
    
    #Prueba 2
    prueba2 = 'Mal'
    try:
        app.registrar_regalo(12345678,98765432,'remera blanca')
    
    except EntidadNoExiste:
        prueba2 = 'OK'

    finally:
        print(f'Prueba 2 {prueba2}')
    
    #Prueba 3
    prueba3 = 'Mal'
    try:
        #(Ya me lo regalaron)
        app.registrar_regalo(12234567,51434026,'The psychology of money')
    
    except RegaloNoDisponible:
        prueba3 = 'OK'

    finally:
        print(f'Prueba 3 {prueba3}')

    
    #Prueba 4
    prueba4 = 'Mal'
    try:
        #(Cedula mal)
        app.crear_usuario('Hola Esto no deberia funcionar','Juan Perez',26017244)
    
    except InformacionInvalida:
        prueba4 = 'OK'

    finally:
        print(f'Prueba 4 {prueba4}')


    #Prueba 5
    prueba5 = 'Mal'
    try:
        #(Nombre mal)
        app.crear_usuario(51434027,132,26017244)
    
    except InformacionInvalida:
        prueba5 = 'OK'

    finally:
        print(f'Prueba 5 {prueba5}')

    
    #Prueba 6
    prueba6 = 'Mal'
    try:
        #(Nombre mal)
        app.crear_usuario(51434027,'John Doe Jr','Hola')
    
    except InformacionInvalida:
        prueba6 = 'OK'

    finally:
        print(f'Prueba 6 {prueba6}')


    #PRUEBAS DE FUNCIONAMIENTO
    #Prueba 7 - 9
    lista_mas_regalados = app.obtener_productos_mas_regalados()
    for i in range(len(lista_mas_regalados)):
        #7
        if lista_mas_regalados[i] == 'remera blanca':
            print(f'Prueba {7+i}  OK')
        #8
        if lista_mas_regalados[i] == 'Atomic Habits':
            print(f'Prueba {7+i}  OK')
        #9
        if lista_mas_regalados[i] == 'The psychology of money':
            print(f'Prueba {7+i}  OK')
        
        

    #Prueba 10 - 12
    lista_amantes_libros = app.obtener_usuarios_amantes_de_libros()
    for i in range(len(lista_amantes_libros)):
        #10
        if lista_amantes_libros[i] == 51434026:
            print(f'Prueba {10+i}  OK')
        #11
        if lista_amantes_libros[i] == 12345678:
            print(f'Prueba {10+i}  OK')
        #12
        if lista_amantes_libros[i] == 12234567:
            print(f'Prueba {10+i}  OK')

    

