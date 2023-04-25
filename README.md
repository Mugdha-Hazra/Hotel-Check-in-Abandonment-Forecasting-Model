# Hotel-Check-in-Abandonment-Forecasting-Model
Hotel Check-in Abandonment Forecasting Model predicts if a guest would cancel a reservation, hotels could contact guests that most likely to cancel to confirm more efficiently and to resell the room to optimize revenues.
# Steps Involved :
Data Loading and Reading: In this step, we loaded the dataset into the environment and read the data using Python's Pandas library.

Data Cleaning and Preprocessing: We removed missing values, duplicates, and outliers from the dataset. We also performed data imputation for missing values using different techniques like mean imputation, mode imputation, and regression imputation. Additionally, we scaled the numerical variables using standard scaling to ensure that all variables have a similar scale. Furthermore, we converted categorical variables into numerical variables using one-hot encoding.

Exploratory Data Analysis: In this step, we analyzed the origin of guests, price paid per night by guests, busiest months for bookings, month with the highest Average Daily Rate (ADR), and whether bookings were made for weekdays, weekends, or both.

Feature Engineering: We created new features like total number of guests, total number of nights booked, and average price per night.

Feature Encoding: We transformed categorical variables into numerical variables using one-hot encoding.

Outlier Detection and Handling: We detected and handled outliers using different techniques like Z-score, Tukey's method, and Isolation Forest.

Feature Selection: We selected important features using correlation and univariate analysis.

Model Building: We built a machine learning model using various algorithms like Linear Regression, Random Forest Regression, and XGBoost Regression.

Model Cross-Validation: We performed cross-validation to evaluate the performance of the machine learning model.

Experimenting with Multiple Algorithms: We experimented with multiple algorithms for model building to find the best performing one.
