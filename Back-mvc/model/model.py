from mysql import connector

class Model:
    """
    *****************************************
    * A data model with MySQL for a store DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *****************
    * Zip methods   *
    *****************
    """
    #Metodo para crear codigo postal
    def create_zip(self, zip, city, state):
        try:
            sql = 'INSERT INTO zips (`zip`, `z_city`, `z_state`) VALUES (%s, %s, %s)'
            vals = (zip, city, state)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Metodo para leer el codigo postal
    def read_a_zip(self, zip):
        try:
            sql = 'SELECT * FROM zips WHERE zip = %s'
            vals =(zip,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo leer todos los codigos postales
    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM zips'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Leer Codigos Postales que pertenezcan a una ciudad
    def read_zips_city(self, city):
        try:
            sql = 'SELECT * FROM zips WHERE z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Actualizar Codigo Postal
    def update_zip(self, fields, vals):
        try:
            sql = 'UPDATE zips SET '+','.join(fields)+'WHERE zip = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Borrar un Codigo Postal
    def delete_zip(self, zip):
        try:
            sql = 'DELETE FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Product methods  *
    ********************
    """

    #Metodo para crear Productos
    def create_product(self, name, brand, descrip, price):
        try:
            sql = 'INSERT INTO products (`p_name`, `p_brand`, `p_descrip`, `p_price`) VALUES (%s, %s, %s,%s)'
            vals = (name, brand, descrip, price)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Metodo para Leer un Producto
    def read_a_product(self, id_product):
        try:
            sql = 'SELECT * FROM products WHERE id_product = %s'
            vals = (id_product,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    #Metodo para Leer todos los Productos
    def read_all_products(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM products'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer las Marcas de los Productos
    def read_products_brand(self, brand):
        try:
            sql = 'SELECT * FROM products WHERE p_brand = %s'
            vals = (brand,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer el rango de Precios de los Productos
    def read_products_price_range(self, price_ini, price_end):
        try:
            sql = 'SELECT * FROM products WHERE p_price >= %s and p_price <= %s'
            vals = (price_ini, price_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar los Productos
    def update_product(self, fields, vals):
        try:
            sql = 'UPDATE products SET '+','.join(fields)+' WHERE id_product = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar Productos
    def delete_product(self, id_product):
        try:
            sql = 'DELETE FROM products WHERE id_product = %s'
            vals = (id_product,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *******************
    * Client methods  *
    *******************
    """

    #Metodo para Crear Clientes
    def create_client(self, name, sname1, sname2, street, noext, noint, col, zip, email, phone):
        try:
            sql = 'INSERT INTO clients (`c_fname`, `c_sname1`, `c_sname2`, `c_street`, `c_noext`, `c_noint`, `c_col`, `c_zip`, `c_email`, `c_phone`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (name, sname1, sname2, street, noext, noint, col, zip, email, phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Cliente
    def read_a_client(self, id_client):
        try:
            sql = 'SELECT clients.*,zips.z_city,zips.z_state FROM clients JOIN zips ON clients.c_zip = zips.zip and clients.id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Clientes
    def read_all_clients(self): #Caution with large amount of data
        try:
            sql = 'SELECT clients.*,zips.z_city,zips.z_state FROM clients JOIN zips ON clients.c_zip = zips.zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    #Metodo para Leer a los Clientes mediante su Codigo Postal
    def read_clients_zip(self, zip):
        try:
            sql = 'SELECT clients.*,zips.z_city,zips.z_state FROM clients JOIN zips ON clients.c_zip = zips.zip and clients.c_zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
        
    #Metodo para Actualizar un Cliente
    def update_client(self, fields, vals):
        try:
            sql = 'UPDATE clients SET '+','.join(fields)+' WHERE id_client = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Metodo para Borrar un Cliente
    def delete_client(self, id_client):
        try:
            sql = 'DELETE FROM clients WHERE id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    * Order methods  *
    ******************
    """

    #Metodo para crear Ordenes
    def create_order(self, id_client, status, date, total):
        try:
            sql = 'INSERT INTO orders (`id_client`, `o_status`, `o_date`, `o_total`) VALUES (%s, %s, %s, %s)'
            vals = (id_client, status, date, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_order = self.cursor.lastrowid
            return id_order
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer las Ordenes
    def read_a_order(self, id_order):
        try:
            sql = 'SELECT orders.*, clients.*, zips.*, FROM orders JOIN clients ON clients.id_client = orders.id_client and orders.id_order = %s JOIN zips ON zips.zip = clients.c_zip'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todas las Ordenes
    def read_all_orders(self): #Caution with large amount of data
        try:
            sql = 'SELECT orders.*, clients.*, zips.* FROM orders JOIN clients ON clients.id_client = orders.id_client JOIN zips ON zips.zip = clients.c_zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer las Ordenes por fecha
    def read_orders_date(self, date):
        try:
            sql = 'SELECT orders.*, clients.*, zips.* FROM orders JOIN clients ON clients.id_client = orders.id_client and orders.o_date = %s JOIN zips ON zips.zip = clients.c_zip'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer todas las Ordenes de un Cliente
    def read_orders_client(self, id_client):
        try:
            sql = 'SELECT orders.*, clients.*, zips.* FROM orders JOIN clients ON clients.id_client = orders.id_client and orders.id_client = %s JOIN zips ON zips.zip = clients.c_zip'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar una Orden
    def update_order(self, fields, vals):
        try:
            sql = 'UPDATE orders SET '+','.join(fields)+' WHERE id_order = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar una Orden
    def delete_order(self, id_order):
        try:
            sql = 'DELETE FROM orders WHERE id_order = %s'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************
    * Order Details methods  *
    **************************
    """
    
    #Metodo para Crear un Detalle de Orden
    def create_order_detail(self, id_order, id_product, od_amount, od_total):
        try:
            sql = 'INSERT INTO order_details (`id_order`, `id_product`, `od_amount`, `od_total`) VALUES (%s, %s, %s, %s)'
            vals = (id_order, id_product, od_amount, od_total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer la Orden con los Detalles
    def read_a_order_detail(self, id_order, id_product):
        try:
            sql = 'SELECT products.id_product, products.p_name, products.p_brand, products.p_price, order_details.od_amount, order_details.od_total FROM order_details JOIN products ON order_details.id_product = products.id_product and order_details.id_order = %s and order_details.id_product = %s'
            vals = (id_order, id_product)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Detalles de la Orden
    def read_order_details(self, id_order):
        try:
            sql = 'SELECT products.id_product, products.p_name, products.p_brand, products.p_price, order_details.od_amount, order_details.od_total FROM order_details JOIN products ON order_details.id_product = products.id_product and order_details.id_order = %s'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar los Detalles de la Orden
    def update_order_details(self, fields, vals):
        try:
            sql = 'UPDATE order_details SET '+','.join(fields)+' WHERE id_order = %s and id_product = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar los Detalles de la Orden 
    def delete_order_detail(self, id_order, id_product):
        try:
            sql = 'DELETE FROM order_details WHERE id_order = %s and id_product = %s'
            vals = (id_order, id_product)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
            