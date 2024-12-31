from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))                         

@app.route('/', methods= ['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''    
    parental_education_level_postgraduate=0
    if request.method == 'POST':
        attendance = float(request.form['Attendance'])
        hours_studied=int(request.form['Hours_studied'])
        previous_scores=float(request.form['Previous_Scores'])
        tutoring_sessions=int(request.form['Tutoring_Sessions'])
        
        parental_education_level=request.form['Parental_Education_Level']
        if(parental_education_level=='Postgraduate'):
            parental_education_level_postgraduate=1
            parental_education_level_high_school=0
        elif(parental_education_level=='High School'):
            parental_education_level_postgraduate=0
            parental_education_level_high_school=1
        else:
            parental_education_level_postgraduate=0
            parental_education_level_high_school=0
        
        distance_from_home=request.form['Distance_from_Home']
        if(distance_from_home=='Near'):
            distance_from_home_near=1
            distance_from_home_moderate=0
        elif(distance_from_home_moderate=='Moderate'):
            distance_from_home_near=0
            distance_from_home_moderate=1
        else:
            distance_from_home_near=0
            distance_from_home_moderate=0
        
        peer_influence=request.form['Peer_Influence']
        if(peer_influence=='Positive'):
            peer_influence_positive = 1
        else:
            peer_influence_positive = 0
        
        extracurricular_activities=request.form['Extracurricular_Activities']
        if(extracurricular_activities=='Yes'):
            extracurricular_activities_yes = 1
        else:
            extracurricular_activities_yes = 0
        
        internet_access=request.form['Internet_Access']
        if(internet_access=='Yes'):
            internet_access_yes = 1
        else:
            internet_access_yes = 0

        physical_activity=int(request.form['Physical_Activity'])
        
        family_income=request.form['Family_Income']
        if(family_income=='Medium'):
            family_income_medium = 1
            family_income_low = 0
        elif(family_income=='Low'):
            family_income_medium = 0
            family_income_low = 1
        else:
            family_income_medium = 0
            family_income_low = 0
        
        access_to_resources=request.form['Access_to_Resources']
        if(access_to_resources=='Medium'):
            access_to_resources_medium = 1
            access_to_resources_low = 0
        elif(access_to_resources=='Low'):
            access_to_resources_medium = 0
            access_to_resources_low = 1
        else:
            access_to_resources_medium = 0
            access_to_resources_low = 0
        
        parental_involvement=request.form['Parental_Involvement']
        if(parental_involvement=='Medium'):
            parental_involvement_medium = 1
            parental_involvement_low = 0
        elif(parental_involvement=='Low'):
            parental_involvement_medium = 0
            parental_involvement_low = 1
        else:
            parental_involvement_medium = 0
            parental_involvement_low = 0

        teacher_quality=request.form['Teacher_Quality']
        if(teacher_quality=='Medium'):
            teacher_quality_medium = 1
            teacher_quality_low = 0
        elif(teacher_quality=='Low'):
            teacher_quality_medium = 0
            teacher_quality_low = 1
        else:
            teacher_quality_medium = 0
            teacher_quality_low = 0

        motivation_level=request.form['Motivation_Level']
        if(motivation_level=='Low'):
            motivation_level_low = 1
        else:
            motivation_level_low = 0

        learning_disabilities=request.form['Learning_Disabilities']
        if(learning_disabilities=='Yes'):
            learning_disabilities_yes = 1
        else:
            learning_disabilities_yes = 0

        prediction=model.predict([[attendance, 
                                hours_studied, 
                                previous_scores,
                                tutoring_sessions, 
                                parental_education_level_postgraduate,
                                distance_from_home_near, 
                                peer_influence_positive,
                                extracurricular_activities_yes, 
                                internet_access_yes,
                                physical_activity, 
                                family_income_medium,
                                access_to_resources_medium, 
                                parental_involvement_medium,
                                teacher_quality_low, 
                                teacher_quality_medium,
                                distance_from_home_moderate, 
                                motivation_level_low,
                                learning_disabilities_yes, 
                                family_income_low,
                                parental_education_level_high_school,
                                parental_involvement_low,
                                access_to_resources_low]])
        
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="The Student's Predicted Score is {}%".format(output))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)