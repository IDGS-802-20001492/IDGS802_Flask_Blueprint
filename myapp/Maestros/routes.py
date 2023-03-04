from flask import Blueprint

maestro = Blueprint('maestros',__name__)

@maestro.route('/getMaes',methods = ['GET'])
def getMaestro():
    return {'key':'Maestro'}