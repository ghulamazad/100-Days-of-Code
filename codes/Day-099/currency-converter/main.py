from currency_converter import CurrencyConverter
from app import App


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    App(converter).mainloop()
