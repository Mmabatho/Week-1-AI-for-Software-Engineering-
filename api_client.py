import requests

class CryptoAPIClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_crypto_data(coin_id):
        url = f"{CryptoAPIClient.BASE_URL}/coins/{coin_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def get_trending_coins():
        url = f"{CryptoAPIClient.BASE_URL}/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @staticmethod
    def get_price_trend(coin_id):
        url = f"{CryptoAPIClient.BASE_URL}/coins/{coin_id}/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': '7'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

def fetch_crypto_data(coin_id):
    # Dummy implementation: return a sample dictionary for Bitcoin, None otherwise
    if coin_id == "Bitcoin":
        return {"price": 50000, "market_cap": 1000000000}
    else:
        return None