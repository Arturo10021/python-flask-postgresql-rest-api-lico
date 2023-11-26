from database.db import get_connection
from .entities.Bebida import Bebida

class BebidaModel():

    @classmethod
    def get_bebidas(self):
        try:
            connection = get_connection()
            bebidas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, tipo_licor, precio, cantidad FROM productos ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    bebida = Bebida(row[0], row[1], row[2], row[3], row[4])
                    bebidas.append(bebida.to_JSON())

            connection.close()
            return bebidas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_bebida(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, tipo_licor, precio, cantidad FROM productos WHERE id = %s", (id,))
                row = cursor.fetchone()

                bebida = None
                if row != None:
                    bebida = Bebida(row[0], row[1], row[2], row[3], row[4])
                    bebida = bebida.to_JSON()

            connection.close()
            return bebida
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_bebida(self, bebida):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO productos (id, nombre, tipo_licor, precio, cantidad) 
                                VALUES (%s, %s, %s, %s, %s)""", (bebida.id, bebida.nombre, bebida.tipo_licor, bebida.precio, bebida.cantidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_bebida(self, bebida):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE productos SET nombre = %s, tipo_licor = %s, precio = %s, cantidad = %s
                                WHERE id = %s""", (bebida.nombre, bebida.tipo_licor, bebida.precio, bebida.cantidad, bebida.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_bebida(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)