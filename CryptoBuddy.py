# crypto_chatbot.py

crypto_db = {
  "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 2/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 5/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 9/10
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    },
    "Polkadot": {
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Algorand": {
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Ripple (XRP)": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "low",
        "sustainability_score": 7/10
    }
}

def get_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"These coins are trending up: {', '.join(trending)} 🚀"

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"{coin} is trending up and has a top-tier sustainability score! 🚀"
        return "No ideal long-term option found."

    else:
        return "Sorry, I can't understand that. Try asking about trending or sustainable cryptos!"

# Simple CLI loopclose

print("👋 Welcome to CryptoBuddy! Ask me about crypto trends.")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("CryptoBuddy: Goodbye! 🚀")
        break
    print("CryptoBuddy:", get_response(query))
