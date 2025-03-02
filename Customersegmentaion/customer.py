import pickle
import streamlit as st
import smtplib, ssl
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Load the ML model
diabetes_model = pickle.load(open('C:/Users/pokal/OneDrive/Desktop/Customersegmentaion/Customersegmentaion/customer.sav', 'rb'))

def send_email(receiver_email, result):
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender_email = "vinjamuru1819@gmail.com" 
    password = "Manoj@123" 

    message = f"""\
    Subject: Customer Segmentation Prediction Result

    The predicted segment is: {result}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def predict_segment(age, annual_income):
    
    cluster_label = diabetes_model.predict([[age, annual_income]])
    
    cluster_names = {
        0: 'HighSpender',
        1: 'LowSpender',
        2: 'MidSpender',
        3: 'YoungHighSpender',
        4: 'OldMidSpender',
        5: 'DiverseGroup'
    }

    
    predicted_segment = cluster_names.get(cluster_label[0], 'Unknown')
    
    return predicted_segment

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Customer Segmentation App',
                           ['Home', 'Login', 'Sign Up', 'Customer Segmentation', 'Graph Comparison', 'Result'],
                           default_index=0)

# Login and Signup logic
if selected == 'Login':
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        # Add authentication logic here
        st.success(f'Logged in as {username}')
        
if selected == 'Sign Up':
    st.title('Sign Up')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    if st.button('Sign Up'):
        # Add signup logic here
        st.success(f'Welcome, {username}! You have successfully signed up.')

# Customer Segmentation Page
if selected == 'Customer Segmentation':
    st.title('Customer Segmentation')
    age = st.text_input('Age')
    annual_income = st.text_input('Annual Income')
    if st.button('Predict Customer Segment'):
        diab_prediction = predict_segment(float(age), float(annual_income))
        st.success(f'The predicted segment is {diab_prediction}')

        # Send email to user
        receiver_email = st.text_input('Enter your email:')
        if receiver_email:
            send_email(receiver_email, diab_prediction)
            st.success('Email sent successfully!')

# Other Pages
if selected == 'Home':
    st.title('Home')
    st.image("picture2.jpg")

if selected == 'Graph Comparison':
    st.title('Graph Comparison')
    st.image("Capture.png")
    st.image("Capture1.png")

if selected == 'Result':
    st.title('Result')
    st.image("picture1.png")

if st.button("About"):
    st.text("Let's Learn")
    st.text("Built with Streamlit")
