# STOCK PRICE PREDICTOR

COMPANY: CODECH TECHNOLOGIES

NAME: RISHABH CHOUHAN

DOMAIN: ARTIFICIAL INTELLIGENCE INTERN

DURATION - 1 MONTH 

# PROJECT - STOCK PRICE PREDICTOR

# Objective

The primary objective of this project titled “Stock Price Predictor” is to develop a machine learning model that can predict the future price of a stock based on its historical price data. This project leverages the power of data science and machine learning to analyze stock trends and provide insights that may aid in making investment decisions or financial forecasts.

Stock market prediction is one of the most complex and high-stakes applications of machine learning due to the influence of countless factors such as news, economic conditions, investor behavior, company performance, and global events. However, by focusing on historical price data alone, it is possible to extract trends and patterns that help forecast short-term price movements using predictive models.

The project focuses on building a stock price prediction system using Linear Regression, one of the simplest and most interpretable machine learning algorithms. Linear regression is particularly effective for modeling relationships between continuous variables, such as date and closing price. The model is trained on historical stock prices fetched using reliable APIs like yfinance, which allows real-time access to stock market data for any publicly listed company.

This project covers the full lifecycle of a data science workflow:
	1.	Data Collection: We fetch historical price data for a specific stock (e.g., Apple Inc. - AAPL) using the yfinance Python library. The dataset includes important financial indicators such as opening price, closing price, high, low, volume, and adjusted close.
	2.	Data Preprocessing: The date feature is converted into a numerical format using ordinal encoding to make it suitable for regression modeling. The closing price is used as the target variable (y), while the date is used as the independent feature (X).
	3.	Model Training: The dataset is split into training and testing sets using train_test_split from scikit-learn. A LinearRegression model is then fitted to the training data.
	4.	Prediction: The trained model is used to predict closing prices on unseen test data.
	5.	Model Evaluation: The model’s performance is evaluated using metrics such as Mean Squared Error (MSE) and R-squared (R² Score). These metrics help determine how well the model can explain the variance in stock prices.
	6.	Visualization: A scatter plot of actual prices versus dates is displayed, with a line graph overlay of the predicted prices. This helps visually assess the performance of the model.

This project is designed to introduce learners to the application of machine learning in the finance domain. It demonstrates how past data can be used to train predictive models, the importance of feature engineering (e.g., converting date to ordinal), and how to evaluate model accuracy. Although stock markets are inherently volatile and influenced by unpredictable events, simple models like linear regression can still serve as useful tools for trend analysis and short-term forecasting.

By completing this project, learners gain practical experience in:
	•	Fetching and handling real-world time-series data,
	•	Applying linear regression in a practical context,
	•	Understanding the limitations of simple ML models in complex domains,
	•	Visualizing financial data and predictions in an interpretable manner.

In conclusion, the Stock Price Predictor project provides a strong foundation in financial data analysis and predictive modeling. While it may not offer accurate long-term predictions due to market complexity, it sets the stage for future improvements using more advanced techniques such as polynomial regression, support vector machines, recurrent neural networks (RNNs), or LSTM models.

# OUTPUT
<img width="1792" alt="Image" src="https://github.com/user-attachments/assets/ae87af4d-c2cf-42d7-b5d7-91f01370e4bb" />

![Image](https://github.com/user-attachments/assets/fe93ce1b-3c77-4ca5-8eea-91f5f29ef188)
