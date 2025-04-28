from models import model, label_encoders
import pandas as pd 
import streamlit as st 
from llm import get_mitigation_strategy


# Streamlit UI
st.title("Project Delay Prediction and Mitigation Assistant 🤖")

st.markdown("### Enter Project Details")

risk = st.selectbox('Risk Level', ['Low', 'Medium', 'High'])
priority = st.selectbox('Priority Level', ['Low', 'Medium', 'High'])
hours = st.number_input('Planned Hours', min_value=1, max_value=500, value=10)
Delay = st.number_input('Delay', min_value=-50, max_value=365, value=30)
root_cause = st.text_input('Root Cause', value='Unknown')
project_discipline = st.text_input('Project Discipline', value='Unknown')

if st.button('Predict and Suggest Mitigation'):
    # Prepare single input row
    input_data = pd.DataFrame([{
        'Risk': risk,
        'Priority': priority,
        'Hours': hours,
        'Delay': Delay,
        'RootCause': root_cause,
        'ProjectDiscipline': project_discipline,
    
    }])
    print("running till here SUCCESSFULLY")
    # Encode input
    input_encoded = input_data.copy()
    input_encoded = input_encoded[['Risk', 'Priority', 'Hours', 'ProjectDiscipline', 'Delay', 'RootCause']]

    for col in ['Risk', 'Priority', 'ProjectDiscipline', 'RootCause']:
        if col in label_encoders:
            input_encoded[col] = label_encoders[col].transform(input_encoded[col].str.lower())
    
    # Predict
    prediction = model.predict(input_encoded)[0]
    print(f'This is prediction{prediction}')
    prob = model.predict_proba(input_encoded)[0, 1]


    # Display Prediction
    st.subheader('🔎 Prediction Result')
    st.write(f"**Will the task likely be delayed?** {'✅ Yes' if prediction else '❌ No'}")
    # st.write(f"**Confidence:** {prob:.2%}")

    # Get mitigation suggestion
    st.subheader('💡 Suggested Mitigation Strategy')
    strategy = get_mitigation_strategy(input_data.iloc[0], prediction)
    st.success(strategy)
