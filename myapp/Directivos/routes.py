from flask import Blueprint

dir = Blueprint('directivos',__name__)

@dir.route('/getDir',methods = ['GET'])
def getDIr():
    return {'key':'Directivos'}