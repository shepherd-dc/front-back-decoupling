from flask import Flask, render_template, jsonify
 
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
 
 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/test')
def api_test():
    return jsonify({'tasks': tasks})
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
