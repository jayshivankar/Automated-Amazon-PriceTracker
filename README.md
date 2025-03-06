# Amazon Price Tracker with Python

## Overview
This Python script tracks the price of a product on Amazon and sends an email alert if the price drops below a specified threshold. It uses `requests` for web scraping, `BeautifulSoup` for parsing HTML, and `smtplib` for sending emails.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python (>=3.7)
- Required Python packages:
  ```bash
  pip install requests beautifulsoup4 python-dotenv
  ```
- An email account for sending alerts (Gmail recommended)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add the following lines to `.env`:
     ```
     my_email=your_email@gmail.com
     password=your_email_password
     ```

## Usage
1. Open the script (`amazon_price_tracker.py`) and update the `URL` variable with the product link:
   ```python
   URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
   ```

2. Run the script:
   ```bash
   python amazon_price_tracker.py
   ```

## Functionality
- Fetches product details from Amazon.
- Extracts the current price of the product.
- Compares the price with a set threshold (e.g., $100).
- Sends an email notification if the price drops below the threshold.

## Notes
- Ensure that the `User-Agent` in the request headers matches your browser to avoid being blocked by Amazon.
- Avoid making frequent requests to Amazon to prevent getting temporarily banned.
- Using hardcoded credentials is **not recommended**; always store them securely using environment variables.

## Disclaimer
This script is for educational and personal use only. Web scraping Amazon may violate their terms of service. Use this script responsibly and at your own risk.

