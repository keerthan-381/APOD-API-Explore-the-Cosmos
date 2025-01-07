# APOD-API-Explore-the-Cosmos

This project allows users to view NASA's Astronomy Picture of the Day (APOD) using both a Streamlit app and an HTML interface. The app fetches daily astronomy images or videos from NASA's APOD API and displays them along with a description. Users can search for pictures from specific dates or fetch random images.

You can also visit the live project [here]#https://keerthan-381.github.io/APOD-API-Explore-the-Cosmos/

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Streamlit App](#streamlit-app)
  - [HTML Interface](#html-interface)
- [Project Structure](#project-structure)
- [API Details](#api-details)

## Overview

This project provides two different interfaces to access the APOD content:

1. **Streamlit App** (`app.py`): A Python-based app to fetch and display the Astronomy Picture of the Day.
2. **HTML Interface** (`index.html`): A web-based interface with the same functionality for users who prefer using a browser.

Both interfaces allow users to:
- Enter a NASA API key.
- Select a specific date (from 1995 onwards).
- Fetch random images.
- Display images or videos with captions and explanations.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/keerthan-381/APOD-API-Explore-the-Cosmos.git
   cd APOD-API-Explore-the-Cosmos.git
   ```

2. **Install Python dependencies (for Streamlit App):**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Streamlit App

1. Navigate to the project directory.
2. Run the app with the following command:
   ```bash
   streamlit run app.py
   ```
3. Open your browser and go to `http://localhost:8501` to access the Streamlit app.
4. Enter your NASA API Key in the sidebar.
5. Select a date or choose the option to fetch random images.
6. Click on the "Fetch APOD" button to retrieve and display the image or video.

### HTML Interface

1. Open the `index.html` file in a browser.
2. Enter your NASA API Key.
3. Select a date or choose to fetch random images.
4. Click the "Fetch APOD" button to view the picture or video.

The HTML interface uses JavaScript to make requests to the NASA API and dynamically display the results.

## Project Structure

The project consists of two main parts:

- **`app.py`**: The Streamlit Python app for interacting with NASA's API.
- **`index.html`**: The HTML file for the browser-based interface.
- **`requirements.txt`**: The file that lists the Python dependencies required for the project.

### `app.py`

This is a Python-based Streamlit app that uses the NASA APOD API to fetch and display astronomy pictures. The app features the following:

- **Sidebar**:
  - Input fields for API Key and Date selection.
  - Checkbox for fetching random images.
  - Number input for specifying the count of random images.

- **Main Content**:
  - Displays the title, explanation, and media (image or video) of the selected or random APOD.

#### Key Libraries:
- `streamlit`: Framework to build the interactive app.
- `requests`: Used to make HTTP requests to the NASA APOD API.


### `index.html`

This is a simple HTML and JavaScript interface that allows users to interact with the NASA APOD API. The file consists of:

- **Input Fields** for the API Key and Date selection.
- **Random Images Checkbox** for selecting the option to fetch random images.
- **Count Input** for specifying how many random images to retrieve.
- **Display Area** for showing the fetched APOD content (images or videos) along with titles and explanations.

#### Key Sections:
- **HTML Structure**: Defines the layout of the page.
- **CSS Styling**: Provides responsive design and styles for the interface.
- **JavaScript**: Handles API requests, dynamically updates the content, and toggles the count section based on the user's selection.



## API Details

- **Base URL**: `https://api.nasa.gov/planetary/apod`
- **Required Parameters**:
  - `api_key`: Your NASA API key (required for all requests).
  - `date`: Specific date for which you want the APOD (optional if random images are requested).
  - `count`: The number of random images to fetch (optional if fetching a single image).


---
