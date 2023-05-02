# Bitcoin-Price
A Python tool that prints out the current Bitcoin price.

This is a Python tool that retrieves the current Bitcoin price in USD from the Binance website using web scraping techniques with requests and BeautifulSoup libraries. The project is intended to provide a simple demonstration of web scraping with Python, as well as to provide an easy way to check the current Bitcoin price.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)
- `BeautifulSoup` library (install using `pip install beautifulsoup4`)

## Usage

To use this project, simply run the `bitcoin_price.py` script using Python:

```bash
python bitcoin_price.py
```

The script will retrieve the current Bitcoin price from the Binance website and print it to the console in the following format:

```bash
The Bitcoin price now is 20,000.00 per (BTC/USD)
```

Note that the price will be in USD and may be different from the current market price depending on when you run the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the Binance website for providing the Bitcoin price data.
