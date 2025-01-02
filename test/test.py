import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

attendance = 70
hours_studied = 22
previous_scores = 72
tutoring_sessions = 4
parental_education_level_postgraduate = 0
parental_education_level_high_school = 0
distance_from_home_near = 1
distance_from_home_moderate = 0 
peer_influence_positive = 1
extracurricular_activities_yes = 1
internet_access_yes = 0
physical_activity = 2
parental_involvement_medium = 0
parental_involvement_low = 0
teacher_quality_low = 0
teacher_quality_medium = 0
motivation_level_low = 0
learning_disabilities_yes = 0
access_to_resources_medium = 0
access_to_resources_low = 1
family_income_medium = 0
family_income_low = 0

model = pickle.load(open('model.pkl', 'rb'))

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
print(f"Exam Score Prediction : {output}")