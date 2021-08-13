#Importing the libraries
import pickle
from flask import Flask , render_template,request
import pandas as pd
app = Flask(__name__)

model = pickle.load(open("predictor model.pkl",'rb'))
car=pd.read_csv("Cleaned car.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique())
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('form.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    kms_driven=request.form.get('kilo_driven')
    

    prediction = pipe.predict(pd.DataFrame([[car_model,company,year,kmd_driven,'fuel_type']],columns=['name','company','year','kms_driven','fuel_type']))
    
    return str(prediction[0])
if __name__=="__main__":
    app.run(debug = True)



