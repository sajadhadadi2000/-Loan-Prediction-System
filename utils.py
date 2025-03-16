import base64
from pathlib import Path
import streamlit as st

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def manual_input():
    col1, col2, col3 = st.columns(3)
    with col1:
        credit_policy = st.selectbox('Credit Policy', [0, 1], help='Credit policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.')
    with col2:
        purpose = st.selectbox('Purpose', ['debt_consolidation', 'credit_card', 'all_other', 'home_improvement', 'small_business', 'major_purchase', 'educational'], help='Purpose of the loan.')
    with col3:
        int_rate = st.number_input('Interest Rate', min_value=0.0, max_value=1.0, step=0.01, format="%.2f", help='Interest rate on the loan.')

    # Second row of inputs
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        installment = st.number_input('Installment', min_value=0.0, step=0.01, format="%.2f", help='Monthly installment amount.')
    with col5:
        log_annual_inc = st.number_input('Log Annual Income', min_value=0.0, step=0.01, format="%.2f", help='Natural logarithm of the annual income.')
    with col6:
        dti = st.number_input('Debt-to-Income Ratio', min_value=0.0, step=0.01, format="%.2f", help='Debt-to-income ratio.')
    with col7:
        fico = st.number_input('FICO Score', min_value=300, max_value=850, step=1, help='FICO credit score.')

    # Third row of inputs    
    col8, col9, col10 = st.columns(3)
    with col8:
        days_with_cr_line = st.number_input('Days with Credit Line', min_value=0, step=1, help='Number of days the borrower has had a credit line.')
    with col9:
        revol_bal = st.number_input('Revolving Balance', min_value=0.0, step=0.01, format="%.2f", help='Revolving balance.')
    with col10:
        revol_util = st.number_input('Revolving Utilization', min_value=0.0, max_value=100.0, step=0.1, format="%.1f", help='Revolving line utilization rate.')

    col11, col12, col13 = st.columns(3)
    with col11:
        inq_last_6mths = st.number_input('Inquiries in Last 6 Months', min_value=0, step=1, help='Number of inquiries in the last 6 months.')
    with col12:
        delinq_2yrs = st.number_input('Delinquencies in Last 2 Years', min_value=0, step=1, help='Number of delinquencies in the last 2 years.')
    with col13:
        pub_rec = st.number_input('Public Records', min_value=0, step=1, help='Number of derogatory public records.')

    
    return [credit_policy, purpose, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line,
            revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec]
        
