import sqlite3 as sql

class BaseDatos():
    def __init__(self):
        self.conexion = sql.connect('Basededatos.db')

    def reservabd(self,ID,Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final):
        cursor = self.conexion.cursor()
        resbd = f'''INSERT INTO Reservas VALUES({ID},'{Nombre}','{Apellidos}',{Celular},'{Correo}',{Salon},
        '{Fecha_inicial}','{Fecha_final}')'''.format(ID,Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final)
        cursor.execute(resbd)
        self.conexion.commit()
        cursor.close()
    def consultabd(self):
        cursor = self.conexion.cursor()
        consbd = f'''SELECT * FROM Reservas'''
        cursor.execute(consbd)
        consulta = cursor.fetchall()
        return consulta
    def consultaorden(self,campo):
        cursor = self.conexion.cursor()
        consbd = f'''SELECT * FROM Reservas ORDER BY {field}'''
        cursor.execute(consbd)
        consulta = cursor.fetchall()
        return consulta

if __name__ == "__main__":
    inst = BaseDatos()
    inst.reservabd(39582645,"Maria","Palacios",3125796351,"mpal@correo.co",2,"30/09/2022","31/09/2022")
    #consultabd()