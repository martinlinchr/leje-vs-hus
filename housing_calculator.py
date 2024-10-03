import streamlit as st
import locale

# Set locale to Danish
locale.setlocale(locale.LC_ALL, 'da_DK.UTF-8')

def format_currency(amount):
    return locale.currency(amount, grouping=True, symbol='DKK')

def calculate_loan_expense(loan_amount):
    return (loan_amount / 100000) * 450

st.title('Bolig Omkostnings Beregner')

col1, col2 = st.columns(2)

with col1:
    st.header('Leje')
    rent = st.number_input('Husleje', value=10000, step=100, format='%d')
    rent_utilities = st.number_input('Vand, varme, el (Leje)', value=2500, step=100, format='%d')
    rent_total = rent + rent_utilities
    st.write(f'Total (Leje): {format_currency(rent_total)}')

with col2:
    st.header('Hus')
    loan_amount = st.number_input('Lånt til huskøb', value=2000000, step=10000, format='%d')
    loan_expense = calculate_loan_expense(loan_amount)
    st.write(f'Låne-udgift: {format_currency(loan_expense)}')
    
    property_tax = st.number_input('Ejendomsskat', value=1600, step=100, format='%d')
    house_utilities = st.number_input('Vand, varme, el (Hus)', value=2500, step=100, format='%d')
    maintenance = st.number_input('Vedligehold', value=750, step=50, format='%d')
    insurance = st.number_input('Husforsikring', value=500, step=50, format='%d')
    
    house_total = loan_expense + property_tax + house_utilities + maintenance + insurance
    st.write(f'Total (Hus): {format_currency(house_total)}')

st.header('Sammenligning')
savings = rent_total - house_total
monthly_goal = 5000

st.write(f'Månedlig opsparing: {format_currency(savings)}')
st.write(f'Årlig opsparing: {format_currency(savings * 12)}')

if savings >= monthly_goal:
    st.success(f'Du når dit månedlige opsparingsmål på {format_currency(monthly_goal)}!')
else:
    st.warning(f'Du mangler {format_currency(monthly_goal - savings)} for at nå dit månedlige opsparingsmål.')

if savings > 0:
    st.info('Positive opsparing: Det er billigere at eje end at leje.')
elif savings < 0:
    st.info('Negative opsparing: Det er dyrere at eje end at leje.')
else:
    st.info('Ingen opsparing: Omkostningerne er ens for at eje og leje.')
