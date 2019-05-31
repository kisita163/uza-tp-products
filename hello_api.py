from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    d = {}
    
    d['hello'] = 10
    return jsonify(d)



if __name__ == "__main__":
    app.run(port=80,debug=True)
