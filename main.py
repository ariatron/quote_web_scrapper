import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrape_quotes(url):
    # Make an HTTP request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract quotes (modify this based on the structure of your target website)
        quotes = [quote.text.strip() for quote in soup.select('.quote span.text')]

        return quotes
    else:
        print(f'Error: Unable to fetch content. Status Code: {response.status_code}')
        return None

def save_to_csv(data, filename):
    # Save data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Quote'])
        writer.writerows(zip(data))

def main():
    # URL of the website to scrape (replace with your target website)
    target_url = 'http://quotes.toscrape.com'

    # Call the scrape_quotes function
    quotes = scrape_quotes(target_url)

    if quotes:
        # Print quotes to the terminal
        print(f'Successfully scraped {len(quotes)} quotes:')
        for quote in quotes:
            print(quote)

        # Save quotes to a CSV file
        save_to_csv(quotes, 'quotes.csv')

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == 'scrape':
            # Call the main function to scrape and both print to terminal and save to CSV
            main()
        elif sys.argv[1] == 'save_to_csv':
            # Call the save_to_csv function
            quotes_to_save = ['quote1', 'quote2']  # Replace with actual quotes to save
            save_to_csv(quotes_to_save, 'quotes.csv')
        else:
            print('Invalid argument. Usage: python myscript.py [scrape|save_to_csv]')
    else:
        # Call the main function if no command-line arguments are provided
        main()
