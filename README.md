# Predicting-Student-Performance

This project demonstrates how to predict student exam scores using various regression models based on different predictor variables like hours studied, attendance, sleep, previous scores, tutoring sessions, and physical activity. The goal is to identify key factors influencing exam scores and to build predictive models to estimate exam scores.

## Project Overview

This project aims to use machine learning regression models to predict a students `Exam Score`. The dataset includes several predictor variables such as:

`Motivation Level:` Student's level of motivation (Low, Medium, High).

`Internet Access:` Availability of internet access (Yes, No).

`Tutoring Sessions:` Number of tutoring sessions attended per month.

`Family Income:` Family income level (Low, Medium, High).

`Teacher Quality:` Quality of the teachers (Low, Medium, High).

`School Type:` Type of school attended (Public, Private).

`Peer Influence:` Influence of peers on academic performance (Positive, Neutral, Negative).

`Physical Activity:` Average number of hours of physical activity per week.

`Learning Disabilities:` Presence of learning disabilities (Yes, No).

`Parental Education Level:` Highest education level of parents (High School, College, Postgraduate).

`Distance from Home:` Distance from home to school: (Near, Moderate, Far).

`Gender:` Gender of the student (Male, Female).


## Project Highlights:

- Analyzed Student Performance Factors for predicting the exam score of a student.
- Built a machine learning model using Linear Regression, Lasso Regression Ridge Regression and the Random Forest Regressor but selected the <b>Linear Regression Model</b> which achieved the lowest <b>RMSE</b> of `2.046497` showing how far the model's predictions are from the actual values and the highest score of <b>R²</b> score of `0.730480` which is indicating the proportion of variance explained in the target by the predictor variables.
- This model can be used for Potential  help educators and policymakers implement targeted interventions that can enhance learning outcomes

## Data Sources:

Source: Student Performance Factors [https://www.kaggle.com/datasets/lainguyn123/student-performance-factors]

Tools and Technologies:

Programming Language(s): Python

Libraries: scikit-learn, pandas, numpy, seaborn, matplotlib, statsmodels


<h3>Getting Started:</h3><a id=""></a>

* Clone this repository: `git clone https://github.com/02sagoe/Predicting-Student-Performance.git`

* cd `Predicting-Student-Performance`

* create new env with python 3 and activate it .

* Install the required packages using pip install -r requirements.txt

* Use this notebook: `python main.ipynb`