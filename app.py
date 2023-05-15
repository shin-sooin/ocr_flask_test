from flask import Flask, request, redirect
from model import Model
import logging

app = Flask(__name__)

M=Model()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/ocr', methods={'GET','POST'})
def ocr():
    if request.method == 'GET':
        id = str(request.args.get('id'))
    elif request.method == 'POST':
        id = str(request.form['id'])
    print(id)
    if id=='':
        return 'error on url'
    elif id=='2':
        return 'connected'
    else:
        return M.ocr(id)

if __name__ == '__main__':
    app.run(debug=True)
