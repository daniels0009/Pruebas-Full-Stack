class View:
    """
    **************************
    * A view for a store DB  *
    **************************
    """

    #Funcion de Inico
    def start(self):
        print('=================================')
        print('= ¡Bienvenido a nuestra Tienda! =')
        print('=================================')
    
    #Funcion de Fin de Programa
    def end(self):
        print('=================================')
        print('=       ¡Hasta la vista!        =')
        print('=================================')

    #Funcion del Menu
    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. CPs')
        print('2. Productos')
        print('3. Clientes')
        print('4. Ordenes')
        print('5. Salir')

    #Funcion Opcion
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    #Funcion "No Valida"
    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')
    
    #Funcion de Pregunta algo de Usuario
    def ask(self, output):
        print(output, end = '')
    
    #Funcion de Mensaje de Pantalla
    def msg(self, output):
        print(output)

    #Funcion de OK (si algo se hizo correcto en el programa)
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    #Funcion de Error (si algo sale mal en alguna operacion en el programa)
    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ******************
    * Views for zips *
    ******************
    """

    #Funcion para el Menu de Codigo Postales
    def zips_menu(self):
        print('*********************')
        print('* -- Submenu CPs -- *')
        print('*********************') 
        print('1. Agregar CP')
        print('2. Mostrar CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de una ciudad')
        print('5. Actualizar CP')
        print('6. Borrar CP')
        print('7. Regresar')
    
    #Funcion de Mostrar Datos del Codigo Postal
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')
    
    #Funcion para ver lo que hay en la cabecera de salida
    def show_zip_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)

    #Funcion para separar Diferentes Datos
    def show_zip_midder(self):
        print('-'*78)

    #Funcion de Terminacion de los Codigos Postales
    def show_zip_footer(self):
        print('*'*78)

    """
    **********************
    * Views for products *
    **********************
    """

    #Funcion para el Menu de los Productos
    def products_menu(self):
        print('***************************')
        print('* -- Submenu Productos -- *')
        print('***************************')
        print('1. Agregar producto')
        print('2. Leer producto')
        print('3. Leer todos los productos')
        print('4. Leer productos de una marca')
        print('5. Leer productos de un rango de precios')
        print('6. Actualizar producto')
        print('7. Borrar Producto')
        print('8. Regresar')

    #Funcion Mostrar Producto
    def show_a_product(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Marca:', record[2])
        print('Descripcion:', record[3])
        print('Precio:', record[4])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_product_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    #Funcion para separar Diferentes Datos
    def show_product_midder(self):
        print('-'*48)

    #Funcion de Terminacion de los Productos
    def show_product_footer(self):
        print('*'*48)

    """
    *********************
    * Views for Clients *
    *********************
    """

    #Funcion de Menu de los Clientes
    def clients_menu(self):
        print('**************************')
        print('* -- Submenu Clientes -- *')
        print('**************************')
        print('1. Agregar Cliente')
        print('2. Leer cliente')
        print('3. Leer todos los clientes')
        print('4. Leer clientes de un CP')
        print('5. Actualizar cliente')
        print('6. Borrar cliente')
        print('7. Regresar')

    #Funcion de Mostrar Cliente
    def show_a_client(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Calle:', record[4])
        print('No exterior:', record[5])
        print('No interior:', record[6])
        print('Colonia:', record[7])
        print('Ciudad:', record[11])
        print('Estado:', record[12])
        print('CP:', record[8])
        print('Email', record[9])
        print('Telefono', record[10])

    #Funcion para Compactar la Informacion de los clientes (varios clientes)
    def show_a_client_brief(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
        print('Direccion:', record[4]+' '+record[5]+' - '+record[6]+', '+record[7])
        print(record[11]+', '+record[12]+', '+record[8])
        print('Email:', record[9])
        print('Telefono:', record[10])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_client_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    #Funcion para separar Diferentes Datos
    def show_client_midder(self):
        print('-'*53)

    #Funcion de Terminacion de los Clientes
    def show_client_footer(self):
        print('*'*53)

    """
    *********************
    * Views for orders  *
    *********************
    """

    #Funcion de Menu de Ordenes
    def orders_menu(self):
        print('*************************')
        print('* -- Submenu Ordenes -- *')
        print('*************************')
        print('1. Agregar orden')
        print('2. Leer orden')
        print('3. Leer todas las ordenes')
        print('4. Leer ordenes de una fecha')
        print('5. Leer ordenes de un cliente')
        print('6. Actualizar datos de orden')
        print('7. Agregar Productos a una orden')
        print('8. Modificar productos de una orden')
        print('9. Borrar productos de una orden')
        print('10. Borrar orden')
        print('11. Regresar')

    #Funcion para Mostrar las Ordenes
    def show_order(self, record):
        print('ID:', record[0])
        print('Estado de la orden:', record[1])
        print('Fecha:', record[2])
        print(' Datos del cliente '.center(81,'*'))
        self.show_a_client_brief(record[5:])
    
    #Funcion para ver lo que hay en la cabecera de salida
    def show_order_header(self, header):
        print(header.center(81,'+'))
    
    #Funcion para separar Diferentes Datos
    def show_order_midder(self):
        print('/'*81)
    
    #Funcion para Mostrar el Total de la Orden
    def show_order_total(self, record):
        print('Total de la orden: '+str(record[4]))

    #Funcion de Terminacion de las Ordenes
    def show_order_footer(self):
        print('+'*81)

    """
    ****************************
    * Views for Order Details  *
    ****************************
    """

    #Funcion para Mostrar los Detalles de la Orden
    def show_a_order_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}|{record[4]:<9}|{record[5]:<11}')

    #Funcion para ver lo que hay en la cabecera de salida (de la vista de detalles de orden)
    def show_order_details_header(self):
        print('-'*81)

        print('ID'.ljust(5)+'|'+'Producto'.ljust(20)+'|'+'Marca'.ljust(20)+'|'+'Precio'.ljust(11)+'|'+'Cantidad'.ljust(9)+'|'+'Total'.ljust(11))
        print('-'*81)
    
    #Funcion de Terminacion de los Detalles de la Orden
    def show_order_details_footer(self):
        print('-'*81)