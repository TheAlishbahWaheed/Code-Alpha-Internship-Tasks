import csv
import os
from datetime import datetime
STOCK_PRICES = {
    "AAPL":  {"name": "Apple Inc.",        "price": 211.12},
    "TSLA":  {"name": "Tesla, Inc.",        "price": 248.50},
    "MSFT":  {"name": "Microsoft Corp.",    "price": 425.30},
    "GOOGL": {"name": "Alphabet Inc.",      "price": 178.90},
    "AMZN":  {"name": "Amazon.com Inc.",    "price": 196.75},
    "NVDA":  {"name": "NVIDIA Corp.",       "price": 137.60},
    "META":  {"name": "Meta Platforms",     "price": 598.40},
    "BRK":   {"name": "Berkshire Hathaway", "price": 530.20},
    "JPM":   {"name": "JPMorgan Chase",     "price": 265.10},
    "V":     {"name": "Visa Inc.",          "price": 355.80},
}
def show_available_stocks():
    """Display the list of available stocks with their current prices."""
    print("\n" + "=" * 52)
    print(f"  {'TICKER':<8} {'COMPANY':<24} {'PRICE':>10}")
    print("=" * 52)
    for ticker, info in STOCK_PRICES.items():
        print(f"  {ticker:<8} {info['name']:<24} ${info['price']:>9.2f}")
    print("=" * 52)
def get_portfolio_from_user():
    portfolio = []
    print("\nEnter your holdings (type 'done' when finished):")
    while True:
        ticker = input("\n  Stock ticker (e.g. AAPL): ").strip().upper()
        if ticker.lower() == "done":
            break
        if ticker not in STOCK_PRICES:
            print(f"  ✗ '{ticker}' not found. Available: {', '.join(STOCK_PRICES)}")
            continue
        try:
            qty = int(input(f"  Quantity of {ticker}: ").strip())
            if qty < 0:
                print("  ✗ Quantity must be 0 or greater.")
                continue
        except ValueError:
            print("  ✗ Please enter a whole number.")
            continue
        info = STOCK_PRICES[ticker]
        total_value = qty * info["price"]
        portfolio.append({
            "ticker": ticker,
            "name":   info["name"],
            "price":  info["price"],
            "qty":    qty,
            "total":  total_value,
        })
        print(f"  ✓ Added: {qty} × ${info['price']:.2f} = ${total_value:,.2f}")
    return portfolio
def display_summary(portfolio):
    if not portfolio:
        print("\n  No holdings entered.")
        return
    grand_total = sum(item["total"] for item in portfolio)
    print("\n" + "=" * 64)
    print("  PORTFOLIO SUMMARY")
    print("=" * 64)
    print(f"  {'TICKER':<8} {'COMPANY':<22} {'PRICE':>9} {'QTY':>6} {'VALUE':>12}")
    print("-" * 64)
    for item in portfolio:
        print(
            f"  {item['ticker']:<8} {item['name']:<22} "
            f"${item['price']:>8.2f} {item['qty']:>6,} "
            f"${item['total']:>11,.2f}"
        )
    print("=" * 64)
    print(f"  {'TOTAL PORTFOLIO VALUE':<42} ${grand_total:>11,.2f}")
    print("=" * 64)
    print("\n  Allocation:")
    sorted_port = sorted(portfolio, key=lambda x: x["total"], reverse=True)
    for item in sorted_port:
        pct = (item["total"] / grand_total * 100) if grand_total > 0 else 0
        bar = "█" * int(pct / 2)
        print(f"    {item['ticker']:<6} {bar:<25} {pct:5.1f}%")
def save_to_txt(portfolio, filename="portfolio.txt"):
    grand_total = sum(item["total"] for item in portfolio)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 64 + "\n")
        f.write("  STOCK PORTFOLIO REPORT\n")
        f.write(f"  Generated: {timestamp}\n")
        f.write("=" * 64 + "\n\n")
        f.write(f"  {'TICKER':<8} {'COMPANY':<22} {'PRICE':>9} {'QTY':>6} {'VALUE':>12}\n")
        f.write("-" * 64 + "\n")
        for item in portfolio:
            f.write(
                f"  {item['ticker']:<8} {item['name']:<22} "
                f"${item['price']:>8.2f} {item['qty']:>6,} "
                f"${item['total']:>11,.2f}\n"
            )
        f.write("=" * 64 + "\n")
        f.write(f"  {'TOTAL PORTFOLIO VALUE':<42} ${grand_total:>11,.2f}\n")
        f.write("=" * 64 + "\n")
    print(f"\n  ✓ Report saved to '{filename}'")
def save_to_csv(portfolio, filename="portfolio.csv"):
    grand_total = sum(item["total"] for item in portfolio)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Company", "Price (USD)", "Quantity", "Total Value (USD)"])
        for item in portfolio:
            writer.writerow([
                item["ticker"],
                item["name"],
                f"{item['price']:.2f}",
                item["qty"],
                f"{item['total']:.2f}",
            ])
        writer.writerow([])  # blank row
        writer.writerow(["", "", "", "GRAND TOTAL", f"{grand_total:.2f}"])
    print(f"  ✓ Data saved to '{filename}'")

def main():
    print("\n╔══════════════════════════════════╗")
    print("  ║   STOCK PORTFOLIO TRACKER v1.0   ║")
    print("  ╚══════════════════════════════════╝")
    show_available_stocks()
    portfolio = get_portfolio_from_user()
    if not portfolio:
        print("\n  Nothing to display. Goodbye!, See Ya!")
        return
    display_summary(portfolio)
    print("\nSave results?")
    print("  1 — Save as .txt")
    print("  2 — Save as .csv")
    print("  3 — Save both")
    print("  4 — No thanks")
    choice = input("\nChoice (1/2/3/4): ").strip()
    if choice in ("1", "3"):
        save_to_txt(portfolio)
    if choice in ("2", "3"):
        save_to_csv(portfolio)
    print("\n  Thank you for using Stock Portfolio Tracker!\n")
if __name__ == "__main__":
    main()