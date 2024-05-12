from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

countries = (
    "United States",
    "India",
    "United Kingdom",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
)

education_levels = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree",
    "Post grad",
)

def predict_salary(country, education, experience):
    X = np.array([[country, education, experience]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)

    salary = regressor.predict(X)
    return salary[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        country = request.form['country']
        education = request.form['education']
      
        education = education.replace("'","’")

        experience = int(request.form['experience'])

        salary = predict_salary(country, education, experience)
        return render_template('result.html', salary=salary)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
