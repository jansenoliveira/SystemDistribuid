from flask import Flask, jsonify,make_response
from flask_cors import CORS, cross_origin # Problema

app = Flask(__name__)
CORS(app)

tasks = [
	{
		'id':1,
		'title': u'Estudo',
		'description': u'Sistemas Distribuidos',
		'done':True
	},
	{
		'id':2,
		'title': u'Monitoria',
		'description': u'Programacao e Algoritmos',
		'done': False
	}
]

@app.route('/')
def index():
	return "URL PARA O ACESSO DA API: '/api/tasks'"

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
	return make_response(jsonify({'tasks': tasks}), 200)

if __name__ == '__main__':
	app.run(debug=True)