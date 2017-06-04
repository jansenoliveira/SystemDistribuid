from flask import Flask, jsonify

app = Flask(__name__)

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
	return "Sanity Test"

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks': tasks})

if __name__ == '__main__':
	app.run(debug=True)