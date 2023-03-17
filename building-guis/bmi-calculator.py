import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

st.title('BMI Calculator')

weight = st.number_input('Enter your weight (in kg)')
height = st.number_input('Enter your height (in cm)')

if st.button('Calculate BMI'):
    bmi = calculate_bmi(weight, height)
    st.write('Your BMI is:', bmi)

    if bmi < 18.5:
        st.write('You are underweight')
    elif bmi >= 18.5 and bmi < 25:
        st.write('You have a normal weight')
    elif bmi >= 25 and bmi < 30:
        st.write('You are overweight')
    else:
        st.write('You are obese')
