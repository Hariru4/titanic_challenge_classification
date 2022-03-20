
from flask import Flask, request

app = Flask(__name__)
@app.route('/api',methods=['POST'])
def say_hello():
    data = request.get_json(force=True)
    name = data['name']
    return 'Hello '+name

if __name__ == '__main__':
    app.run(port=10001,debug=True)
