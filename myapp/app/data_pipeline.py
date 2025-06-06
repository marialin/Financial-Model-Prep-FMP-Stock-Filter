import requests
import os

data_api_key = os.getenv("FMP_API_KEY")

INDEXES = {
    'QQQ': 'qqq_holdings',
    'VGT': 'vgt_holdings',
    'SPY': 'spy_holdings'
}

BASE_URL = "https://financialmodelingprep.com/api/v3"

# Helper: Fetch tickers in an index (mocked for now)
def get_index_constituents(index_symbol):
    # Example: Replace with actual API endpoint when available
    if index_symbol == 'QQQ':
        return ['AAPL', 'MSFT', 'NVDA','GOOGL','AVGO', 'META']  # example subset
    if index_symbol == 'VGT':
        return ['AVGO', 'CSCO', 'ADBE']
    if index_symbol == 'SPY':
        return ['GOOGL', 'META', 'AMZN']
    return []

def fetch_company_profile(ticker):
    url = f"{BASE_URL}/profile/{ticker}?apikey={data_api_key}"
    res = requests.get(url)
    return res.json()[0] if res.ok and res.json() else None


def fetch_key_metrics(ticker):
    url = f"{BASE_URL}/ratios-ttm/{ticker}?apikey={data_api_key}"
    res = requests.get(url)
    return res.json()[0] if res.ok and res.json() else None

def fetch_growth_metrics(ticker):
    url = f"{BASE_URL}/income-statement-growth/{ticker}?apikey={data_api_key}&limit=1"
    res = requests.get(url)
    return res.json()[0] if res.ok and res.json() else None


def filter_companies(index_symbol, margin_threshold=0.01, max_de_ratio=2.0):
    tickers = get_index_constituents(index_symbol)
    qualified = []
    filtered =[]

    for ticker in tickers:
        profile = fetch_company_profile(ticker)
        metrics = fetch_key_metrics(ticker)
        growth = fetch_growth_metrics(ticker)


        if not profile or not metrics:
            continue

        sales_growth = growth.get("growthRevenue") if growth else None
        profit_margin = metrics.get("netProfitMarginTTM") if metrics else None
        debt_equity = metrics.get("debtEquityRatioTTM") if metrics else None
        filtered.append({
            "ticker": ticker,
            "companyName": profile.get("companyName"),
            "salesGrowth": sales_growth,
            "profitMargin": profit_margin,
            "deRatio": debt_equity                
        })

        if all([
            sales_growth and sales_growth > 0,
            profit_margin and profit_margin > margin_threshold,
            debt_equity is not None and debt_equity < max_de_ratio
        ]):
            qualified.append({
                "ticker": ticker,
                "companyName": profile.get("companyName"),
                "salesGrowth": sales_growth,
                "profitMargin": profit_margin,
                "deRatio": debt_equity
            })

    return qualified, filtered
