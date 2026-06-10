def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 189.50,
        "TSLA": 250.75,
        "GOOGL": 145.30,
        "MSFT": 380.90,
        "AMZN": 195.45
    }
    
    portfolio = {}
    total_investment = 0
    
    print("=" * 60)
    print("Stock Portfolio Tracker")
    print("=" * 60)
    print("\nAvailable stocks:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")
    
    print("\n" + "-" * 60)
    
    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_name.lower() == "done":
            break
        
        if stock_name not in stock_prices:
            print("❌ Stock not found. Please try again.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        investment = stock_prices[stock_name] * quantity
        portfolio[stock_name] = {
            "quantity": quantity,
            "price": stock_prices[stock_name],
            "total": investment
        }
        total_investment += investment
        print(f"✅ Added {quantity} shares of {stock_name}")
    
    if not portfolio:
        print("No stocks added to portfolio.")
        return
    
    print("\n" + "=" * 60)
    print("PORTFOLIO SUMMARY")
    print("=" * 60)
    
    for stock, details in portfolio.items():
        print(f"\n{stock}:")
        print(f"  Quantity: {details['quantity']}")
        print(f"  Price per share: ${details['price']:.2f}")
        print(f"  Total value: ${details['total']:.2f}")
    
    print("\n" + "-" * 60)
    print(f"Total Portfolio Value: ${total_investment:.2f}")
    print("-" * 60)
    
    save_option = input("\nSave results to file? (yes/no): ").lower().strip()
    if save_option == "yes":
        save_portfolio(portfolio, total_investment)
    
def save_portfolio(portfolio, total):
    filename = "portfolio.txt"
    with open(filename, "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 50 + "\n\n")
        
        for stock, details in portfolio.items():
            file.write(f"{stock}\n")
            file.write(f"  Quantity: {details['quantity']}\n")
            file.write(f"  Price: ${details['price']:.2f}\n")
            file.write(f"  Total: ${details['total']:.2f}\n\n")
        
        file.write("=" * 50 + "\n")
        file.write(f"TOTAL PORTFOLIO VALUE: ${total:.2f}\n")
    
    print(f"✅ Portfolio saved to {filename}")

if __name__ == "__main__":
    stock_portfolio_tracker()