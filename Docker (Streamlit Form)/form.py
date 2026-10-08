import streamlit as st 
print(st.__version__)

st.title("Know Your Customer (KYC) Form", text_alignment="center")
st.header("Enter Your Details")

st.markdown("[Check out my Portfolio](https://github.com/GurSewakIssar/Portfolio/)")

st.markdown("""
<style>
.st-emotion-cache-1wbqy5l.e19wr9s00
{
visibility:hidden;
}
</style>
""", 
unsafe_allow_html=True)

with st.form("Enter Details", clear_on_submit=True) as form:
    
    name, dob = st.columns(2)
    gender, disability = st.columns(2)
    isd, phone, = st.columns(2)

    name.text_input("Enter your name", placeholder="ENTER")
    dob.date_input("Enter you date of birth",)
    gender.selectbox("Enter your gender", options=("Male", "Female", "Others"))
    disability.selectbox("Do you have any disability", options=("No", "Yes"))
    isd.text_input("Enter ISD code", placeholder="+91", validate=r"^\+\d{1,3}$")
    phone.number_input("Enter Phone Number", value=None, min_value=0)
    
    submitted = st.form_submit_button()

    if submitted:
        st.success("Form Submitted!")