import streamlit as st
from streamlit_option_menu import option_menu
from prediction import predict
from utils import img_to_bytes, manual_input
import pandas as pd


page = option_menu(None, ["Home", "Prediction", "About Us"], 
    icons=['house-fill', 'piggy-bank-fill', "cup-hot-fill"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"icon": {"font-size": "25px"}})


def home():
    col1, col2 = st.columns(2)
    with col1:
        st.title("NeuroTech watching your money!")
    with col2:
        st.image("./static/home.jpg",)
    
    st.write("We help you make the best decisions for the bank by providing accurate predictions and comprehensive financial insights. This ensures informed lending practices and minimizes risk.")
        
    
def prediction():
    
    #  initialize st.session_state for "submit"
    if 'submit' not in st.session_state:
        st.session_state.submit = False

    if not st.session_state.submit:
        
        st.title("Prediction")
        option = st.radio("Select Input Method", ('Manual Input', 'Upload CSV File'))

        if option == 'Manual Input':

            st.write("Enter the values for the following features to get a prediction:")
            data = manual_input()

            if st.button('Predict', type='primary'):
            
                # Placeholder for prediction logic
                st.session_state.submit = True    
                st.session_state.result = predict(data)

                # Clear input fields
                st.rerun()
        elif option == "Upload CSV File":
            
            st.write("Upload a CSV file containing the features for prediction:")
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

            if uploaded_file is not None:

                data = pd.read_csv(uploaded_file)
                st.write("Data uploaded successfully. Displaying first 5 rows:")
                st.write(data.head())

                if st.button('Predict', type='primary'):
                    st.session_state.submit = True
                    predictions = data.apply(lambda row: predict(row.tolist())[0], axis=1)
                    data['not.fully.paid'] = predictions
                    output_file = './Output/output.csv'
                    data.to_csv(output_file, index=False)
                    st.session_state.result = [2, output_file]
                    st.rerun()
          
    
    else:
        st.title("Prediction result:")
        if st.session_state.result[0] == 1:
            st.warning(f"{st.session_state.result[1]}", icon="⚠️")
        elif st.session_state.result[0] == 0:
            st.success(f"{st.session_state.result[1]}", icon="✅")
        else:
            st.write(f"Results saved in {st.session_state.result[1]}")
            data = pd.read_csv(st.session_state.result[1])
            st.write(data.head())        
            st.download_button(label="Download CSV", data=open(st.session_state.result[1], 'rb').read(),file_name="predictions.csv", mime="text/csv")

        if st.button('Reset',type='primary'):
            st.session_state.submit = False
            st.rerun()


def about():

    st.subheader("About Us")
    st.write("""NeuroTech is a team in the field of deep learning and artificial intelligence, dedicated to pushing the boundaries of what machines can achieve. Our mission is to leverage cutting-edge neural network research to develop innovative solutions that transform industries and improve lives.""")
    
    st.markdown("<h3 style='text-align: center;'>Meet Our Team</h3>", unsafe_allow_html=True)
    
    html_code = f"""
    <div style="display: flex; justify-content: space-around;">
        <div style="text-align: center;">
            <img src="data:image/jpg;base64,{img_to_bytes('./static/morteza.jpg')}" width="150"  style="border-radius: 50%; padding: 10px;">
            <p>Morteza Rashidpour</p>
        </div>
        <div style="text-align: center;">
            <img src="data:image/jpg;base64,{img_to_bytes('./static/milad.jpg')}" width="150"  style="border-radius: 50%; padding: 10px;">
            <p>MohammadMilad Karimi</p>
        </div>
        <div style="text-align: center;">
            <img src="data:image/jpg;base64,{img_to_bytes('./static/sajad.jpg')}" width="150" style="border-radius: 50%; padding: 10px;">
            <p>Sajad Hadadi</p>
        </div>
        <div style="text-align: center;">
            <img src="data:image/jpg;base64,{img_to_bytes('./static/mohamad.jpg')}" width="150" style="border-radius: 50%; padding: 10px;">
            <p>MohammadHossein Noohpisheh</p>
        </div>
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/150" width="150" style="border-radius: 50%; padding: 10px;">
            <p>Ali Nasiri Kia</p>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True, )

def main():
    if page == "Home":
        home()
    elif page == "Prediction":
        prediction()
    elif page == "About Us":
        about()

if __name__ == "__main__":
    main()