🚕 TripFare – Urban Taxi Fare Prediction using Machine Learning

TripFare is a Machine Learning–based project that predicts the total taxi fare amount
for an urban trip using historical taxi data.
The project follows a complete data science lifecycle — from data understanding and
EDA to model building and deployment using Streamlit.

📌 Problem Statement

Accurate taxi fare estimation improves pricing transparency and user trust in
ride-hailing services.
This project analyzes historical taxi trip data and builds a regression model
to predict the total fare amount based on trip-related features such as
trip duration, time of travel, and passenger count.

🧠 Machine Learning Details

Problem Type: Supervised Learning – Regression

Target Variable: total_amount

Models Used:

Linear Regression

Ridge Regression

Lasso Regression

Random Forest Regressor

Gradient Boosting Regressor

🛠️ Tech Stack

Programming Language: Python

Libraries & Tools: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Deployment: Streamlit

Platform: Google Colab

Version Control: GitHub

📂 Project Structure

TripFare-Taxi-Fare-Prediction/
├── 01_Data_Understanding_EDA.ipynb
├── 02_Feature_Engineering_Model.ipynb
├── 03_Final_Model_Streamlit.ipynb
├── app.py
├── README.md

📘 Notebook Overview
Notebook 1: Data Understanding & EDA

Dataset loading and inspection

Handling missing values and duplicates

Feature creation (pickup hour, weekend, night ride)

Exploratory Data Analysis using visualizations

Notebook 2: Feature Engineering & Model Building

Trip duration calculation

Encoding categorical features

Feature selection using correlation

Training and comparing multiple regression models

Notebook 3: Final Model & Deployment

Hyperparameter tuning using GridSearchCV

Final model selection

Model saving

Streamlit application preparation

🚀 Streamlit Application

The Streamlit web app allows users to input:

Passenger count

Trip duration

Pickup hour

Weekend indicator

Night ride indicator

and predicts the estimated total taxi fare in real time.

📊 Sample Input & Output

Input

Passenger Count: 2

Trip Duration: 15 minutes

Pickup Hour: 22

Weekend: Yes

Night Ride: Yes

Output
Estimated Total Fare: $13.77

🎯 Key Learning Outcomes

End-to-end Machine Learning project workflow

Feature engineering on real-world data

Regression model evaluation and comparison

Hyperparameter tuning

Model deployment using Streamlit

GitHub project structuring

📌 Conclusion

TripFare demonstrates how machine learning can be applied to real-world
urban transportation problems to generate realistic fare predictions.

👤 Author

Harsha Chourey
Artificial Intelligence & Machine Learning

📎 Note

The trained model file (.pkl) is not uploaded to GitHub as a best practice.
