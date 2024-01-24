import argparse
import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrape_quotes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract quotes (modify this based on the structure of your target website)
        quotes = [quote.text.strip() for quote in soup.select('.quote span.text')]

        return quotes
    except requests.exceptions.RequestException as e:
        print(f'Error: Unable to fetch content. {e}')
        return None

def save_to_csv(data, filename):
    # Save data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Quote'])
        writer.writerows(zip(data))

def main():
    # Create an argparse parser
    parser = argparse.ArgumentParser(description='Scrape quotes from a website and save to CSV.')
    parser.add_argument('--url', help='URL of the website to scrape', default='http://quotes.toscrape.com')
    parser.add_argument('command', help='Command to execute', choices=['scrape', 'save_to_csv'])

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.command == 'scrape':
        # Call the main function to scrape and both print to terminal and save to CSV
        quotes = scrape_quotes(args.url)
        if quotes:
            print(f'Successfully scraped {len(quotes)} quotes:')
            for quote in quotes:
                print(quote)
    elif args.command == 'save_to_csv':
        # Call the main function to get quotes and then save them to CSV
        quotes_to_save = scrape_quotes(args.url)
        if quotes_to_save:
            save_to_csv(quotes_to_save, 'quotes.csv')
    else:
        print('Invalid command. Usage: python main_edit.py {scrape|save_to_csv}')

if __name__ == "__main__":
    main()
