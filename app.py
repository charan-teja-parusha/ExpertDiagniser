from flask import Flask, render_template, request
from expert import MedicalExpert
from experta import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/diagnosis', methods=['POST'])
# def diagnosis():
#     # Create a new instance of the expert system
#     expert = MedicalExpert()
#     # Retrieve the symptoms from the form
#     red_eyes = request.form.get('red_eyes')
#     fatigue = request.form.get('fatigue')
#     short_breath = request.form.get('short_breath')
#     appetite_loss = request.form.get('appetite_loss')
#     fever = request.form.get('fever')

#     # Convert radio button values to "yes" or "no"
#     red_eyes = "yes" if red_eyes == "yes" else "no"
#     fatigue = "yes" if fatigue == "yes" else "no"
#     short_breath = "yes" if short_breath == "yes" else "no"
#     appetite_loss = "yes" if appetite_loss == "yes" else "no"
#     fever = "yes" if fever == "yes" else "no"

#     # Add user inputs to the expert system's knowledge base
#     expert.reset()
#     print(red_eyes)
#     #expert.run()
#     #expert.declare(Fact(action="questionnaire"))
#     expert.declare(Fact(red_eyes="yes"))
#     expert.declare(Fact(fatigue="no"))
#     expert.declare(Fact(short_breath="no"))
#     expert.declare(Fact(appetite_loss="no"))
#     expert.declare(Fact(fever="no"))
#     # Run the expert system and get the diagnosis
#     expert.run()
#     diagnosis = expert.get_diagnosis()

#     # Render the diagnosis template with the diagnosis result
#     return render_template('diagnosis.html', diagnosis=diagnosis)


def suggest_disease(disease, symptoms):
    print(f"\nYou might be suffering from {disease}")
    symptoms = '- ' + '\n - '.join(symptoms)
    print(f"This conclusion is reached because you show symptoms among the following:\n {symptoms}")
    open_doc = yes_no(f"\nDo you want to know more regarding {disease}?")
    if open_doc == "yes":
        webbrowser.open(f"Treatment/html/{disease}.html", new=2)
    # add the following code to redirect to the diagnosis page with the results
    diseases = [disease]
    url_params = {
        "name": engine.facts["name"],
        "disease": diseases
    }
    query_string = urllib.parse.urlencode(url_params, doseq=True)
    webbrowser.open(f"diagnosis.html?{query_string}", new=2)
    exit(0)
