from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS, cross_origin
from DataClass import DataClass

app = Flask(__name__)
dataClass = DataClass()

@app.route('/', methods=['POST'])
def predict():
    print("ok")
    gender = request.form['gender']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    fit = request.form['fit']
    temp = request.form['temp']
    requestObject = {
        "gender" : gender,
        "height" : height,
        "weight" : weight,
        "fit" : fit,
        "temp" : temp
    }
    return requestObject


@app.route('/onclick', methods=['GET', 'POST'])
def on_click_test():
    requestObject = request.json
    dataClass.get_data(requestObject['height'], requestObject['weight'], requestObject['fit'], requestObject['gender'], requestObject['temp'])
    return requestObject


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('web01.html')

@app.route('/web01.html', methods=["GET", "POST"])
def web1():
    return render_template('web01.html')

@app.route('/web02.html', methods=["GET", "POST"])
def web2():
    return render_template('web02.html')

@app.route('/web03.html', methods=["GET", "POST"])
def web3():
    return render_template('web03.html')

@app.route('/test')
def dataObject_value():
    value1 = dataClass.toValue()
    print(value1['temp'])
    return value1['temp']

@app.route('/test1')
def result_size(): 
    result = dataClass.return_data()
    result_size = result[0]
    return (result_size)

@app.route('/test2')
def image_link():
    result = dataClass.return_data()
    result_num = result[1]
    print(result_num)
    image_link = dataClass.find_image_link(result_num)
    return (image_link)

@app.route('/test3')
def purchase_link():
    result = dataClass.return_data()
    result_num = result[1]
    print(result_num)
    purchase_link = dataClass.find_purchase_link(result_num)
    return (purchase_link)

if __name__ == '__main__':
    app.run(port=5000)