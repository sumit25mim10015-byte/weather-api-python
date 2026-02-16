
# 🌤 Python Weather API Project (Console-Based)

## 📌 Overview

This project is a simple **console-based Weather Application** built using Python.
It fetches real-time weather information for any city using the **OpenWeatherMap API**.
The goal of this project is to learn basic API integration, JSON data handling, and error handling in Python.

---

## 🎯 Features

* User enters a city name
* Fetches live weather data using API
* Displays:

  * Temperature (Celsius & Fahrenheit)
  * Weather Condition
  * Humidity
  * Wind Speed
* Handles errors such as:

  * Invalid city name
  * API issues
  * No internet connection

---

## 🛠 Technologies Used

* Python
* Requests Library
* OpenWeatherMap API
* JSON Data Parsing

---

## 📂 Project Structure

```
weather-api-python/
│
├── main.py        # Main Python program
├── README.md      # Project documentation
└── screenshots/   # Output images
```

---

## ⚙️ How the Code Works (Step-by-Step)

### 1️ Import Library

The program imports the `requests` module to send HTTP requests to the weather server.

### 2️ API Key Setup

A personal API key from OpenWeatherMap is added to authenticate requests.

### 3️ User Input

The program asks the user to enter a city name using `input()`.

### 4️ API Request

A URL is created using the city name and API key.
The program sends a GET request to fetch weather data.

### 5️ JSON Parsing

The API returns data in JSON format.
Python converts it into a dictionary using:

```
response.json()
```

### 6️ Data Extraction

The program reads:

* Temperature
* Humidity
* Weather description
* Wind speed

### 7️ Temperature Conversion

Temperature is converted from Kelvin to Celsius and Fahrenheit.

### 8️ Output Display

Weather details are printed neatly in the terminal.

### 9️ Error Handling

The program handles:

* Invalid city names
* Internet connection problems
* Unexpected errors

---

##  Installation & Usage

### Step 1: Install Python

Download Python from https://python.org

### Step 2: Install Required Library

```
pip install requests
```

### Step 3: Add Your API Key

Open `main.py` and replace:

```
API_KEY = "YOUR_API_KEY_HERE"
```

with your own key from OpenWeatherMap.

### Step 4: Run the Program

```
python main.py
```

---

## 🖥 Example Output

```
Enter city name: Delhi

🌍 Weather Report
City: Delhi
Temperature: 30.25°C / 86.45°F
Condition: Clear Sky
Humidity: 45 %
Wind Speed: 3.5 m/s
```

---

## 📚 Learning Objectives

This project helped in understanding:

* How APIs work
* Making HTTP requests in Python
* JSON data parsing
* Basic exception handling

---

## 👨‍💻 Author

Beginner Python project created for learning API integration and real-world data handling.
