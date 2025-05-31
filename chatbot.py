from nlp_utils import process_query
from crypto_db import crypto_db
from api_client import CryptoAPIClient, fetch_crypto_data  # <-- Add this import

def get_response(user_query):
    if not user_query:
        return "Please enter a question about crypto trends or sustainability."

    processed_query = process_query(user_query).lower()

    # Help message
    if "help" in processed_query or "options" in processed_query:
        return (
            "You can ask me about:\n"
            "- Trending or rising coins\n"
            "- Sustainable or eco-friendly cryptos\n"
            "- Least sustainable coins\n"
            "- Coins that are not trending\n"
            "- Price or market cap of a coin\n"
            "- Long-term growth options\n"
            "Type 'exit' or 'quit' to leave."
        )

    # Handle negative or "not trending" queries
    if "not trending" in processed_query or "falling" in processed_query or "down" in processed_query:
        not_trending = [coin for coin in crypto_db if crypto_db[coin].get("price_trend") != "rising"]
        if not_trending:
            return f"These coins are not trending up: {', '.join(not_trending)}"
        else:
            return "All tracked coins are currently trending up!"

    # Handle negative or "not sustainable" queries
    if "not sustainable" in processed_query or "unsustainable" in processed_query or "least sustainable" in processed_query:
        least_sustainable = min(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"{least_sustainable} is the least sustainable option."

    # Handle sustainable queries
    if "sustainable" in processed_query or "eco-friendly" in processed_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!"

    # Handle trending/rising queries
    if "trending" in processed_query or "rising" in processed_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending:
            return f"These coins are trending up: {', '.join(trending)} 🚀"
        else:
            return "No coins are currently trending up."

    # Handle long-term/growth queries
    if "long-term" in processed_query or "growth" in processed_query:
        coins = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7
        ]
        if coins:
            return f"{', '.join(coins)} are trending up and have a top-tier sustainability score! 🚀"
        return "No ideal long-term option found."

    # Handle price or market cap queries
    for coin in crypto_db:
        if coin.lower() in processed_query:
            # Try to fetch real-time data first
            api_data = fetch_crypto_data(coin)
            if "price" in processed_query:
                price = api_data["price"] if api_data and "price" in api_data else crypto_db[coin].get("price", "unknown")
                return f"The current price of {coin} is ${price}."
            if "market cap" in processed_query or "marketcap" in processed_query:
                market_cap = api_data["market_cap"] if api_data and "market_cap" in api_data else crypto_db[coin].get("market_cap", "unknown")
                return f"The market cap of {coin} is ${market_cap}."
    
    # Default fallback
    return (
        "Sorry, I can't understand that. Try asking about trending, sustainable, or price info for cryptos! "
        "Type 'help' for options."
    )


# API
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
