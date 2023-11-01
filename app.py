from flask import Flask, jsonify, request, render_template
import pandas as pd
from joblib import load

app = Flask(__name__)

@app.route('/api/predict', methods=['GET','POST'])
def api_predict():
    """API request
    """
    if request.method == 'POST':  #this block is only entered when the form is submitted
        Modelo = load('TratamientoAnemia.joblib')
        req_data = request.get_json () 
        if not req_data:
            return jsonify(error="request body cannot be empty"), 400

        ED_01 = 0 
        ED_02 = 0 
        ED_03 = 0
        ED_04 = 0
        ES_01 = 0
        ES_02 = 0
        ES_03 = 0
        ES_04 = 0
        AN_01 = 0
        HE_01 = 0
        AD_01 = 0

        ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)
        AN_01 = 0
        HE_01 = 0
        AD_01 = 0

        tipo_edad = req_data['tipo_edad']
        estrato_social = req_data['estrato_social']
        tipo_anemia = req_data['tipo_anemia']
        examen_hemoglobina = req_data['examen_hemoglobina']
        tipo_administracion = req_data['tipo_administracion']

        features = { 
            'tipo_edad': tipo_edad,
            'estrato_social': estrato_social,
            'tipo_anemia': tipo_anemia,
            'examen_hemoglobina': examen_hemoglobina,
            'tipo_administracion': tipo_administracion
        }

        if tipo_edad == '1':
            ED_01,ED_02,ED_03,ED_04 = (1,0,0,0)
        if tipo_edad == '2':
            ED_01,ED_02,ED_03,ED_04 = (0,1,0,0)
        if tipo_edad == '3':
            ED_01,ED_02,ED_03,ED_04 = (0,0,1,0)
        if tipo_edad == '4':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,1)
        if tipo_edad == '5':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '6':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '7':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '8':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '9':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '10':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '11':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '12':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)

        if estrato_social == '1':
            ES_01,ES_02,ES_03,ES_04 = (1,0,0,0)
        if estrato_social == '2':
            ES_01,ES_02,ES_03,ES_04 = (0,1,0,0)
        if estrato_social == '3':
            ES_01,ES_02,ES_03,ES_04 = (0,0,1,0)
        if estrato_social == '4':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,1)
        if estrato_social == '5':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        if tipo_anemia == '1':
            AN_01 = 1
        if tipo_anemia == '2':
            AN_01 = 0

        if examen_hemoglobina == '1':
            HE_01 = 1
        if examen_hemoglobina == '2':
            HE_01 = 0

        if tipo_administracion == '1':
            AD_01 = 1
        if tipo_administracion == '2':
            AD_01 = 0

        Xnew = [ED_01, ED_02, ED_03, ED_04,
                ES_01, ES_02, ES_03, ES_04,
                AN_01, HE_01, AD_01]        

        dataXnewValues = [['ED_01', 'ED_02', 'ED_03', 'ED_04',
                           'ES_01', 'ES_02', 'ES_03', 'ES_04',
                           'AN_01', 'HE_01', 'AD_01'], Xnew]

        dataXnewColumns = dataXnewValues.pop(0)

        dataXnewDf = pd.DataFrame(dataXnewValues, columns=dataXnewColumns)

        Ynew = Modelo.predict(dataXnewDf)

        if Ynew[0] == 1:
            Mensaje = 'Paciente con alta probabilidad de Sí Completar su Tratamiento contra la Anemia'
        else:
            Mensaje = 'Paciente con alta probabilidad de No Completar su Tratamiento contra la Anemia'

        return jsonify( inputs=features,predictions=Mensaje)

    return '''User postman u otro cliente para ejecutar esta API REST'''

@app.route('/', methods=['GET','POST'])
def predict():
    """
    """
    if request.method == 'POST':  #this block is only entered when the form is submitted
        Modelo = load('TratamientoAnemia.joblib')
        ED_01 = 0 
        ED_02 = 0 
        ED_03 = 0
        ED_04 = 0
        ES_01 = 0
        ES_02 = 0
        ES_03 = 0
        ES_04 = 0
        AN_01 = 0
        HE_01 = 0
        AD_01 = 0

        ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)
        AN_01 = 0
        HE_01 = 0
        AD_01 = 0

        tipo_edad = request.form.get('tipo_edad')
        estrato_social = request.form.get('estrato_social')
        tipo_anemia = request.form.get('tipo_anemia')
        examen_hemoglobina = request.form.get('examen_hemoglobina')
        tipo_administracion = request.form.get('tipo_administracion')

        features = { 
            'tipo_edad': tipo_edad,
            'estrato_social': estrato_social,
            'tipo_anemia': tipo_anemia,
            'examen_hemoglobina': examen_hemoglobina,
            'tipo_administracion': tipo_administracion
        }

        if tipo_edad == '1':
            ED_01,ED_02,ED_03,ED_04 = (1,0,0,0)
        if tipo_edad == '2':
            ED_01,ED_02,ED_03,ED_04 = (0,1,0,0)
        if tipo_edad == '3':
            ED_01,ED_02,ED_03,ED_04 = (0,0,1,0)
        if tipo_edad == '4':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,1)
        if tipo_edad == '5':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '6':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '7':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '8':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '9':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '10':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '11':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)
        if tipo_edad == '12':
            ED_01,ED_02,ED_03,ED_04 = (0,0,0,0)

        if estrato_social == '1':
            ES_01,ES_02,ES_03,ES_04 = (1,0,0,0)
        if estrato_social == '2':
            ES_01,ES_02,ES_03,ES_04 = (0,1,0,0)
        if estrato_social == '3':
            ES_01,ES_02,ES_03,ES_04 = (0,0,1,0)
        if estrato_social == '4':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,1)
        if estrato_social == '5':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        if tipo_anemia == '1':
            AN_01 = 1
        if tipo_anemia == '2':
            AN_01 = 0

        if examen_hemoglobina == '1':
            HE_01 = 1
        if examen_hemoglobina == '2':
            HE_01 = 0

        if tipo_administracion == '1':
            AD_01 = 1
        if tipo_administracion == '2':
            AD_01 = 0

        Xnew = [ED_01, ED_02, ED_03, ED_04,
                ES_01, ES_02, ES_03, ES_04,
                AN_01, HE_01, AD_01]        

        dataXnewValues = [['ED_01', 'ED_02', 'ED_03', 'ED_04',
                           'ES_01', 'ES_02', 'ES_03', 'ES_04',
                           'AN_01', 'HE_01', 'AD_01'], Xnew]

        dataXnewColumns = dataXnewValues.pop(0)

        dataXnewDf = pd.DataFrame(dataXnewValues, columns=dataXnewColumns)

        Ynew = Modelo.predict(dataXnewDf)

        if Ynew[0] == 1:
            Mensaje = 'Paciente con alta probabilidad de Sí Completar su Tratamiento contra la Anemia'
        else:
            Mensaje = 'Paciente con alta probabilidad de No Completar su Tratamiento contra la Anemia'
        return render_template("index.html", inputs=features, predictions=Mensaje, 
            tipo_edad=tipo_edad, estrato_social=estrato_social, 
            tipo_anemia=tipo_anemia, examen_hemoglobina=examen_hemoglobina, 
            tipo_administracion=tipo_administracion)

        tipo_edad = request.form.get('tipo_edad')
        estrato_social = request.form.get('estrato_social')
        tipo_anemia = request.form.get('tipo_anemia')
        examen_hemoglobina = request.form.get('examen_hemoglobina')
        tipo_administracion = request.form.get('tipo_administracion')

    return render_template("index.html")
