import streamlit as st

def format_currency(amount):
    return f"{amount:,.0f} DKK".replace(",", ".")

def calculate_loan_expense(loan_amount):
    return (loan_amount / 100000) * 450

st.title('Leje vs. hus')

# Leje sektion
st.header('Leje')
col1, col2 = st.columns(2)

with col1:
    st.subheader('Månedlig')
    rent = st.number_input('Husleje', value=10000, step=100, format='%d', key='rent_monthly')
    rent_utilities = st.number_input('Vand, varme, el', value=2500, step=100, format='%d', key='rent_utilities_monthly')
    rent_total_monthly = rent + rent_utilities
    st.write(f'Total pr. måned: {format_currency(rent_total_monthly)}')

with col2:
    st.subheader('Årlig')
    rent_yearly = st.number_input('Husleje (Årlig)', value=rent*12, step=1000, format='%d', key='rent_yearly')
    rent_utilities_yearly = st.number_input('Vand, varme, el (Årlig)', value=rent_utilities*12, step=1000, format='%d', key='rent_utilities_yearly')
    rent_total_yearly = rent_yearly + rent_utilities_yearly
    st.write(f'Total pr. år: {format_currency(rent_total_yearly)}')

st.markdown("---")  # Horisontal linje

# Hus sektion
st.header('Hus')
col3, col4 = st.columns(2)

with col3:
    st.subheader('Månedlig')
    loan_amount = st.number_input('Lånt til huskøb', value=2000000, step=10000, format='%d')
    loan_expense = calculate_loan_expense(loan_amount)
    st.write(f'Låne-udgift pr. måned: {format_currency(loan_expense)}')
    
    property_tax = st.number_input('Ejendomsskat (Månedlig)', value=1600, step=100, format='%d', key='property_tax_monthly')
    house_utilities = st.number_input('Vand, varme, el (Månedlig)', value=2500, step=100, format='%d', key='house_utilities_monthly')
    maintenance = st.number_input('Vedligehold (Månedlig)', value=750, step=50, format='%d', key='maintenance_monthly')
    insurance = st.number_input('Husforsikring (Månedlig)', value=500, step=50, format='%d', key='insurance_monthly')
    
    house_total_monthly = loan_expense + property_tax + house_utilities + maintenance + insurance
    st.write(f'Total pr. måned: {format_currency(house_total_monthly)}')

with col4:
    st.subheader('Årlig')
    st.write(f'Låne-udgift pr. år: {format_currency(loan_expense * 12)}')
    property_tax_yearly = st.number_input('Ejendomsskat (Årlig)', value=property_tax*12, step=1000, format='%d', key='property_tax_yearly')
    house_utilities_yearly = st.number_input('Vand, varme, el (Årlig)', value=house_utilities*12, step=1000, format='%d', key='house_utilities_yearly')
    maintenance_yearly = st.number_input('Vedligehold (Årlig)', value=maintenance*12, step=500, format='%d', key='maintenance_yearly')
    insurance_yearly = st.number_input('Husforsikring (Årlig)', value=insurance*12, step=500, format='%d', key='insurance_yearly')
    
    house_total_yearly = (loan_expense * 12) + property_tax_yearly + house_utilities_yearly + maintenance_yearly + insurance_yearly
    st.write(f'Total pr. år: {format_currency(house_total_yearly)}')

st.markdown("---")  # Horisontal linje

# Sammenligning af månedlige udgifter
st.header('Sammenligning af månedlige udgifter')
col5, col6 = st.columns(2)
with col5:
    st.write(f'Leje pr. måned: {format_currency(rent_total_monthly)}')
with col6:
    st.write(f'Hus pr. måned: {format_currency(house_total_monthly)}')

if savings_monthly > 0:
    st.info(f'I dette tilfælde er det billigst at leje. Besparelse: {format_currency(savings_monthly)} pr. måned.')
elif savings_monthly < 0:
    st.info(f'I dette tilfælde er det billigst at eje. Besparelse: {format_currency(-savings_monthly)} pr. måned.')
else:
    st.info('I dette tilfælde er omkostningerne ens for at leje og eje.')

st.markdown("---")  # Horisontal linje

# Opsparing sektion
st.header('Opsparing')
savings_monthly = house_total_monthly - rent_total_monthly
savings_yearly = house_total_yearly - rent_total_yearly
monthly_goal = st.number_input('Ønsket månedlig opsparing', value=5000, step=100, format='%d')

st.write(f'Månedlig besparelse ved at leje: {format_currency(savings_monthly)}')
st.write(f'Årlig besparelse ved at leje: {format_currency(savings_yearly)}')

if savings_monthly >= monthly_goal:
    st.success(f'Du når dit månedlige opsparingsmål på {format_currency(monthly_goal)}!')
else:
    st.warning(f'Du mangler {format_currency(monthly_goal - savings_monthly)} for at nå dit månedlige opsparingsmål.')
