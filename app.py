import streamlit as st
import joblib

"# Stroke Prediction using health data"
"Enter the following data to predict stroke"

# Load the machine learning model
model = joblib.load('model.pkl')

# Create a form
with st.form(key="health_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    ever_married = st.selectbox("Ever Married", ["No", "Yes"])
    work_type = st.selectbox("Work Type", ["Children", "Government job", "Never worked", "Private","Self-employed"])
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, step=0.1)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    smoking_status = st.selectbox("Smoking Status", ["Never smoked", "Formerly smoked", "Smokes", "Unknown"])

    # Submit button
    submit_button = st.form_submit_button(label="Submit")

# Process the form data after submission
if submit_button:
    st.write("Form Submitted Successfully!")

    # Store inputs as variables
    input_data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "residence_type": residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status
    }

    # Convert categorical inputs to numerical if needed for ML model
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    hypertension_map = {"No": 0, "Yes": 1}
    heart_disease_map = {"No": 0, "Yes": 1}
    ever_married_map = {"No": 0, "Yes": 1}
    work_type_map = {"Children": 0, 
                     "Government job": 1, 
                     "Never worked": 2, 
                     "Private": 3, 
                     "Self-employed": 4}
    residence_type_map = {"Urban": 0, "Rural": 1}
    smoking_status_map = {"Never smoked": 0, "Formerly smoked": 1, "Smokes": 2, "Unknown": 3}

    # Create numerical representation of inputs
    input_data = [
        gender_map[gender],
        age,
        hypertension_map[hypertension],
        heart_disease_map[heart_disease],
        ever_married_map[ever_married],
        work_type_map[work_type],
        residence_type_map[residence_type],
        avg_glucose_level,
        bmi,
        smoking_status_map[smoking_status]
    ]

    # make prediction
    prediction = model.predict([input_data])[0]

    # Map the prediction to text
    prediction_map = {0: 'Negative', 1: 'Positive'}
    prediction_text = prediction_map[prediction]

    # Display the prediction
    if prediction == 1:
        st.warning(f"Model Prediction: {prediction_text} - Please consult with a healthcare provider for further evaluation.")
    else:
        st.success(f"Model Prediction: {prediction_text} - You are in good health! Keep up the good work.")
