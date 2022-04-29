from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def weight_prediction():
    if request.method == 'GET':
        return render_template("Tugas.html")
    elif request.method == 'POST':
        _height = request.form['tinggi_badan']
        _gender = request.form['gender']
        if _gender == 'laki-laki':
            _gender = 0
        else:
            _gender = 1
        
        model = joblib.load('Model-development/prediksi berat badan dengan linear regression.pkl')
        result = model.predict([[_height, _gender]]) 
        return render_template('Tugas.html', result = result)
    else:
        return "Unsupported Request Method"
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)