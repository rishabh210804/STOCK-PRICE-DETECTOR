import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Download stock data (e.g., Apple)
stock = yf.download('AAPL', start='2020-01-01', end='2023-12-31')

# Step 2: Prepare the data
stock['Date'] = stock.index
stock['Date_ordinal'] = pd.to_datetime(stock['Date']).map(pd.Timestamp.toordinal)
X = stock[['Date_ordinal']]
y = stock['Close']

# Step 3: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
print("✅ R² Score:", r2_score(y_test, y_pred))
print("📉 Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Step 7: Plot results
plt.figure(figsize=(10, 5))
plt.scatter(stock['Date'], stock['Close'], label="Actual Price", alpha=0.5)
plt.plot(X_test['Date_ordinal'].map(pd.Timestamp.fromordinal), y_pred, color='red', label="Predicted Price")
plt.title("Stock Price Prediction (AAPL)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
