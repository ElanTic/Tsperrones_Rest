from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL


app = Flask(__name__)

conexion = MySQL(app)

@app.route('/')
def index():
    return 'text more and more'

@app.route('/jovenes', methods = ['GET'])
def listar_jovenes():
    try:
        cursor = conexion.connection.cursor()
        sql = "Select nombre, email, telefono, contacto from joven_0"
        cursor.execute(sql)
        datos = cursor.fetchall()
        jovenes = []
        for fila in datos:
            joven ={'nombre': fila[0], 'email': fila[1], 'telefono': fila[2], 'contacto' : fila[3]}
            jovenes.append(joven)
        return jsonify({'Jovenes': jovenes, 'resul':"resuls"})

    except Exception as ex: 
        return jsonify({'resul': 'Error'})

@app.route('/jovenes/<nombre>', methods = ['GET'])
def leer_joven(nombre):
    try:
        cursor = conexion.connection.cursor()
        sql = "Select nombre, email, telefono, contacto from joven_0 where nombre = '{0}' ".format(nombre)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            joven = {'nombre': datos[0], 'email': datos[1], 'telefono': datos[2], 'contacto' : datos[3]}
            return jsonify({'Joven': joven, 'resul': 'encontrado'})
        return jsonify({'resul': 'Not found'})
    except Exception as ex:
        return jsonify({'resul': 'Error'})
    
@app.route('/jovenes', methods = ['POST'])
def agregar_joven():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT into joven_0 (nombre, email, telefono, contacto) values
        ('{0}','{1}','{2}','{3}')""".format(request.json['nombre'], request.json['email'],
                                            request.json['telefono'], request.json['contacto'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})
    except Exception as ex:
        return jsonify({'resul': 'Error'})
    
@app.route('/jovenes/<nombre>', methods = ['DELETE'])
def eliminar_joven(nombre):
    try:
        cursor = conexion.connection.cursor()
        sql = "Delete from joven_0 where nombre = '{0}'".format(nombre)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})
    except Exception as ex:
        return jsonify({'resul': 'Error'})

@app.route('/jovenes/<nombre>', methods=['PUT'])
def actualizar_joven(nombre):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE joven_0 SET email = '{0}', telefono = '{1}', 
        contacto = '{2}' WHERE nombre = '{3}'""".format(
            request.json['email'], request.json['telefono'], request.json['contacto'], nombre)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})
    except Exception as ex:
        return jsonify({'resul': 'Error'})

'''
ahora va lo de la pertenencia
'''

@app.route('/pertenencias', methods=['GET'])
def listar_pertenencias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM pertenencia"
        cursor.execute(sql)
        datos = cursor.fetchall()
        pertenencias = []
        for fila in datos:
            pertenencia = {
                'id': fila[0],
                'dueno': fila[1],
                'nombre': fila[2],
                'categoria': fila[3],
                'marca': fila[4],
                'modelo': fila[5],
                'color': fila[6],
                'descripcion': fila[7],
                'foto': fila[8]
            }
            pertenencias.append(pertenencia)
        return jsonify({'Pertenencias': pertenencias, 'resul': 'results'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/pertenencias/<id>', methods=['GET'])
def leer_pertenencia(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM pertenencia WHERE id = {0}".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:
            pertenencia = {
                'id': datos[0],
                'dueno': datos[1],
                'nombre': datos[2],
                'categoria': datos[3],
                'marca': datos[4],
                'modelo': datos[5],
                'color': datos[6],
                'descripcion': datos[7],
                'foto': datos[8]
            }
            return jsonify({'Pertenencia': pertenencia, 'resul': 'encontrado'})
        return jsonify({'resul': 'Not found'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/pertenencias', methods=['POST'])
def agregar_pertenencia():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO pertenencia (dueno, nombre, categoria, marca, modelo, color, descripcion, foto)
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')""".format(
            request.json['dueno'], request.json['nombre'], request.json['categoria'],
            request.json['marca'], request.json['modelo'], request.json['color'],
            request.json['descripcion'], request.json['foto'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/pertenencias/<id>', methods=['DELETE'])
def eliminar_pertenencia(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM pertenencia WHERE id = {0}".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/pertenencias/<id>', methods=['PUT'])
def actualizar_pertenencia(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE pertenencia SET 
                 dueno = '{0}', nombre = '{1}', categoria = '{2}', marca = '{3}',
                 modelo = '{4}', color = '{5}', descripcion = '{6}', foto = '{7}'
                 WHERE id = {8}""".format(
            request.json['dueno'], request.json['nombre'], request.json['categoria'],
            request.json['marca'], request.json['modelo'], request.json['color'],
            request.json['descripcion'], request.json['foto'], id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})

'''
Las fichas
'''

@app.route('/fichas_objeto_p', methods=['GET'])
def listar_fichas_objeto_p():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM ficha_objeto_p"
        cursor.execute(sql)
        datos = cursor.fetchall()
        fichas_objeto_p = []
        for fila in datos:
            ficha_objeto_p = {
                'id': fila[0],
                'date_found': fila[1],
                'date_lost': fila[2],
                'ubicacion': fila[3],
                'is_found': fila[4],
                'owner_id': fila[5],
                'pertenencia_id': fila[6]
            }
            fichas_objeto_p.append(ficha_objeto_p)
        return jsonify({'FichasObjetoP': fichas_objeto_p, 'resul': 'results'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/fichas_objeto_p/<id>', methods=['GET'])
def leer_ficha_objeto_p(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM ficha_objeto_p WHERE id = {0}".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:
            ficha_objeto_p = {
                'id': datos[0],
                'date_found': datos[1],
                'date_lost': datos[2],
                'ubicacion': datos[3],
                'is_found': datos[4],
                'owner_id': datos[5],
                'pertenencia_id': datos[6]
            }
            return jsonify({'FichaObjetoP': ficha_objeto_p, 'resul': 'encontrado'})
        return jsonify({'resul': 'Not found'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/fichas_objeto_p', methods=['POST'])
def agregar_ficha_objeto_p():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO ficha_objeto_p (date_found, date_lost, ubicacion, is_found, owner_id, pertenencia_id)
                 VALUES ('{0}', '{1}', '{2}', {3}, '{4}', {5})""".format(
            request.json['date_found'], request.json['date_lost'], request.json['ubicacion'],
            request.json['is_found'], request.json['owner_id'], request.json['pertenencia_id'])
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/fichas_objeto_p/<id>', methods=['DELETE'])
def eliminar_ficha_objeto_p(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM ficha_objeto_p WHERE id = {0}".format(id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


@app.route('/fichas_objeto_p/<id>', methods=['PUT'])
def actualizar_ficha_objeto_p(id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE ficha_objeto_p SET 
                 date_found = '{0}', date_lost = '{1}', ubicacion = '{2}',
                 is_found = {3}, owner_id = '{4}', pertenencia_id = {5}
                 WHERE id = {6}""".format(
            request.json['date_found'], request.json['date_lost'], request.json['ubicacion'],
            request.json['is_found'], request.json['owner_id'], request.json['pertenencia_id'], id)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'resul': 'ok'})

    except Exception as ex:
        return jsonify({'resul': 'Error'})


def not_found_ese(error):
    return "Sin datos"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found_ese)
    app.run()