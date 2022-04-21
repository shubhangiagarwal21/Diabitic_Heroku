#importing the library

from flask import Flask , render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

#load the model
model = joblib.load('model/diabitic_80.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['post'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    result = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if result[0]==1:
        data = "person is diabitic"
    else:
        data = "person is not diabitic"

    print(data)

    return render_template('predict.html', data = data)
    

# @app.route('/data', methods=['post'])
# def data1():
#     url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

#     names=['preg','plas','pres','skin','test','mass','pedi','age','class']

#     df = pd.read_csv(url , names = names)
#     array = df.values
#     X = array[:,0:8]

#     result = model.predict(X)

#     if result[0]==1:
#         data = "person is diabitic"
#     else:
#         data = "person is not diabitic"

#     print(data)

#     return "data received"

app.run(debug = True) # should be always at the end


"""
http: hyper text transfer protocol
127.0.0.1 - ip address - localhost
:5000 - port
/ - route

http://127.0.0.1:5000/

"""

