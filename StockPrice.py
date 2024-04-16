import csv
import os
import requests

def get_stock_prices(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        print("Error: Data not available.")
        return None

    time_series = data['Time Series (Daily)']
    daily_prices = []

    # Extracting prices for the last 7 days
    for date in sorted(time_series.keys(), reverse=True)[:40]:
        daily_prices.append((date, float(time_series[date]['4. close'])))

    return daily_prices

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Close Price'])
        for date, price in data:
            writer.writerow([date, price])

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'J1IQCXRM594TAQVV'
symbol = 'NVDA'  # NVIDIA's stock symbol
stock_prices = get_stock_prices(symbol, api_key)

if stock_prices:
    print("Date\t\t\tClose Price")
    for date, price in stock_prices:
        print(f"{date}\t${price}")

    # Specify the download folder path
    download_folder = 'C:\Downloads'

    # Check if the download folder exists, if not, create it
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Specify the file path where you want to save the CSV file
    file_path = os.path.join(download_folder, 'stock_prices.csv')

    # Save the data to the CSV file
    save_to_csv(stock_prices, file_path)
    print(f"Data saved to {file_path}")
