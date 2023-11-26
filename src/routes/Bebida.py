from flask import Blueprint, jsonify , request

# Entities
from models.entities.Bebida import Bebida

# Models
from models.BebidaModel import BebidaModel

main=Blueprint('productos_blueprint', __name__)

@main.route('/')
def get_bebidas():
    try:
        bebidas=BebidaModel.get_bebidas()
        return jsonify(bebidas)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_bebida(id):
    try:
        bebida=BebidaModel.get_bebida(id)
        if bebida != None:
            return jsonify(bebida)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_bebida():
    try:
        id=request.json['id']
        nombre=request.json['nombre']
        tipo_licor=request.json['tipo_licor']
        precio=int(request.json['precio'])
        cantidad=int(request.json['cantidad'])
        bebida=Bebida(id, nombre, tipo_licor, precio, cantidad)
        affected_rows=BebidaModel.add_bebida(bebida)
        if affected_rows == 1:
            return jsonify(bebida.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

    
@main.route('/update/<id>', methods=['PUT'])
def update_bebida(id):
    try:
        nombre=request.json['nombre']
        tipo_licor=request.json['tipo_licor']
        precio=int(request.json['precio'])
        cantidad=int(request.json['cantidad'])
        bebida=Bebida(id, nombre, tipo_licor, precio, cantidad)
        
        affected_rows=BebidaModel.update_bebida(bebida)
        
        if affected_rows == 1:
            return jsonify(bebida.id)
        else:
            return jsonify({'message': "Error on update"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_bebida(id):
    try:
        bebida=Bebida(id)
        affected_rows=BebidaModel.delete_bebida(bebida)
        
        if affected_rows == 1:
            return jsonify(bebida.id)
        else:
            return jsonify({'message': "Error on delete"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
