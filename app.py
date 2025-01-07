import streamlit as st
import requests
from datetime import date

# Base URL for APOD
BASE_URL_APOD = "https://api.nasa.gov/planetary/apod"

# Streamlit App
st.title("Astronomy Picture of the Day (APOD)")

# Sidebar for User Input
st.sidebar.subheader("APOD Query Options")

# Ask for API Key
api_key = st.sidebar.text_input("Enter your NASA API Key:", type="password")

# Date Input
selected_date = st.sidebar.date_input(
    "Select Date",
    value=date.today(),
    min_value=date(1995, 6, 16),  # First APOD published
    max_value=date.today(),
)

# Option for Random Images
count_option = st.sidebar.checkbox("Random Images (Count)")
count = None
if count_option:
    count = st.sidebar.number_input("Number of Random Images", min_value=1, max_value=10, step=1)

# Fetch and Display Data
if st.sidebar.button("Fetch APOD"):
    if not api_key:
        st.error("Please enter a valid NASA API Key.")
    else:
        # Set Query Parameters
        params = {"api_key": api_key}
        if count_option and count:
            params["count"] = count
        else:
            params["date"] = selected_date

        # Make API Request
        response = requests.get(BASE_URL_APOD, params=params)
        if response.status_code == 200:
            try:
                data = response.json()

                # Handle multiple images if 'count' is used
                if isinstance(data, list):
                    for item in data:
                        st.subheader(item.get("title", "No Title"))
                        st.write(item.get("explanation", "No Description Available"))
                        if item.get("media_type") == "image":
                            st.image(item.get("url"), caption=item.get("title"))
                        elif item.get("media_type") == "video":
                            st.video(item.get("url"))
                        else:
                            st.write("Unsupported media type.")
                else:
                    # Single Image Response
                    st.subheader(data.get("title", "No Title"))
                    st.write(data.get("explanation", "No Description Available"))
                    if data.get("media_type") == "image":
                        st.image(data.get("url"), caption=data.get("title"))
                    elif data.get("media_type") == "video":
                        st.video(data.get("url"))
                    else:
                        st.write("Unsupported media type.")
            except ValueError:
                st.error("Unexpected response format. Please try again.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
