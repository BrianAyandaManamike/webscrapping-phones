# Mobile Phones Scraper

## Overview
This project is a web scraper designed to extract information about mobile phones from various websites. It retrieves data such as phone models, specifications, and prices from different brand websites and stores them in an Excel file for further analysis.

## Features
- Scrapes data from multiple brand websites simultaneously.
- Extracts phone models and specifications.
- Organizes data into an Excel file with each brand having its own sheet.
- Applies borders and formatting to the Excel sheets for better readability.

## Dependencies
- Python 3.10
- Requests library (for making HTTP requests)
- BeautifulSoup4 (for parsing HTML content)
- Pandas (for data manipulation and exporting to Excel)
- Openpyxl (for handling Excel files)
  
## Installation
1. Clone the repository:

    ```
    git clone https://github.com/BrianAyandaManamike/webscrapping-phones
    ```

2. Navigate to the project directory:

    ```
    cd mobile-phones-scraper
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
1. Open `main.py` in a text editor.
2. Update the `brand_urls` list with the URLs of the brand websites you want to scrape.
3. Run the `main.py` script:

    ```
    python main.py
    ```

4. The scraped data will be saved to an Excel file named `mobile_phones.xlsx` in the project directory.

## Notes
- This scraper is designed to work with specific HTML structures of the brand websites. Any changes to the website structure may require modifications to the scraper code.
- Use responsibly and adhere to website terms of service and scraping guidelines.

## License
[MIT License](LICENSE)

