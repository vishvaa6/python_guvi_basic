import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch_data(self):
        response = requests.get(self.url)
        self.data = response.json()

    def display_countries_and_currencies(self):
        for country in self.data:
            name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                symbol = currency_info.get('symbol', 'No symbol')
                print(f"Country: {name}, Currency: {currency_code}, Symbol: {symbol}")

    def display_countries_with_currency(self, currency_name):
        for country in self.data:
            name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_name in currency_info.get('name', ''):
                    print(f"Country: {name}, Currency: {currency_code}")

    def display_countries_with_dollar(self):
        self.display_countries_with_currency('Dollar')

    def display_countries_with_euro(self):
        self.display_countries_with_currency('Euro')

# URL provided in the task
url = "https://restcountries.com/v3.1/all"

# Create an instance of the class
country_data = CountryData(url)

# Fetch the data
country_data.fetch_data()

# Display country names, currencies, and their symbols
print("Countries and their currencies:")
country_data.display_countries_and_currencies()

# Display countries using Dollar as currency
print("\nCountries using Dollar:")
country_data.display_countries_with_dollar()

# Display countries using Euro as currency
print("\nCountries using Euro:")
country_data.display_countries_with_euro()
