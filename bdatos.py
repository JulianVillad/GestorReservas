import sqlite3 as sql

class BaseDatos():
    def __init__(self):
        self.conexion = sql.connect('Basededatos.db')

    def reservabd(self,ID,Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final):
        cursor = self.conexion.cursor()
        resbd = f'''INSERT INTO Reservas VALUES('{ID}','{Nombre}','{Apellidos}','{Celular}','{Correo}','{Salon}',
        '{Fecha_inicial}','{Fecha_final}')'''.format(ID,Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final)
        cursor.execute(resbd)
        self.conexion.commit()
        cursor.close()
    def consultabd(self):
        cursor = self.conexion.cursor()
        consbd = f'''SELECT * FROM Reservas'''
        cursor.execute(consbd)
        consulta = cursor.fetchall()
        cursor.close()
        print(consulta)
        return consulta
    def orden(self):
        cursor = self.conexion.cursor()
        consbd = f'''SELECT * FROM Reservas ORDER BY Fecha_inicial'''
        cursor.execute(consbd)
        consulta = cursor.fetchall()
        self.conexion.commit()
        cursor.close()
    def cancelarev(self,Fecha_inicial,Salon):
        cursor = self.conexion.cursor()
        bd = f'''DELETE FROM Reservas WHERE Fecha_inicial = '{Fecha_inicial}' and Salon = '{Salon}' '''.format(Fecha_inicial, Salon)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    def buscarevento(self,Fecha_inicial,Salon):
        cursor = self.conexion.cursor()
        consbd = f'''SELECT * FROM Reservas WHERE Fecha_inicial = '{Fecha_inicial}' and Salon = '{Salon}' '''.format(Fecha_inicial, Salon)
        cursor.execute(consbd)
        consulta = cursor.fetchall()
        cursor.close()
        return consulta
    def modificarevento(self,Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final,ID):
        cursor = self.conexion.cursor()
        bd = f'''UPDATE Reservas SET Nombre ='{Nombre}', Apellido = '{Apellidos}',Celular = '{Celular}',
        Correo = '{Correo}', Salon = '{Salon}', Fecha_inicial = '{Fecha_inicial}', 
        Fecha_final = '{Fecha_final}' WHERE ID = '{ID}' '''.format(Nombre,Apellidos,Celular,Correo,Salon,Fecha_inicial,Fecha_final,ID)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
        
if __name__ == "__main__":
    inst = BaseDatos()
    #inst.reservabd("6168148","Gregorio","Montes","654651","Grego@correo.co","2","25/09/2022","26/09/2022")
    #inst.consultabd()
    #inst.cancelarev("01/12/2022", "1")
    #inst.buscarevento('10/12/2022', '1')
    #inst.modificarevento("Marco","Marquez","654651","GREGORIO@correo.co","2","25/09/2022","26/09/2022")