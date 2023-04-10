import streamlit as st
import pandas as pd
import pickle





# Load the pre-trained model
model = pickle.load(open("order_cancellation.pkl", 'rb'))


# Define the Streamlit app
def app():
    st.title('Order Cancellation Prediction')

    # Create the input form for the user
    hotel_id = st.text_input('Hotel ID')
    destination_country = st.text_input('Destination Country')
    room_count = st.number_input('Room Count', min_value=1)
    num_booked_nights = st.number_input('Number of Booked Nights', min_value=1)
    num_reviews = st.number_input('Number of Reviews', min_value=0)


    if st.button('Predict'):
        # Check if the input values are not empty strings
        if hotel_id != '' and destination_country != '':
            input_df = pd.DataFrame({
                'hotel_id': [hotel_id],
                'destinationCountry': [destination_country],
                'roomCount': [room_count],
                'numberOfBookedNights': [num_booked_nights],
                'numberOfReviews': [num_reviews]
            })

            # Make the prediction
            prediction = model.predict(input_df)

            # Display the prediction
            if prediction == 1:
                st.success('The Order Is Cancelled')
            else:
                st.write('The Order Is Not Cancelled')
        else:
            st.warning('Please enter values for Hotel ID and Destination Country.')

if __name__ == '__main__':
    app()
