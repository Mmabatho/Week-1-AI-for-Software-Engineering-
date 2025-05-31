def main():
    print("👋 Welcome to CryptoBuddy! Ask me about crypto trends.")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("CryptoBuddy: Goodbye!🚀\n Remember to invest wisely and stay updated on market trends! 🌟")
            break
        print("CryptoBuddy:", get_response(query))

if __name__ == "__main__":
    main()
