from flask import Flask, request, render_template

import model 

app = Flask(__name__)

# render htmp page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [x for x in request.form.values()]
    age = input_features[0]
    ed = input_features[1]
    employ = input_features[2]
    address = input_features[3]
    income = input_features[4]
    debtinc = input_features[5]
    creddebt = input_features[6]
    othdebt = input_features[7]
    
    print(age,ed,employ,address,income,debtinc,creddebt,othdebt)    
    predicted_risk = model.predict_risk(age,ed,employ,address,income,debtinc,creddebt,othdebt) 
    
    print(predicted_risk)
    if (predicted_risk== 0.0):
        class1='Low Risk'
    else:
        class1='High Risk'
        
    return render_template('index.html', prediction_text=class1)
    
if __name__ == "__main__":
    app.run()    