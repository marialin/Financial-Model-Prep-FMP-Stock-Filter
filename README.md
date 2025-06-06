# Financial-Model-Prep-FMP-Stock-Filter
This repository aims to find out the best growth companies to invest in based on a set of filters and their current valuation based on DCF intrinsic values.

Below is my plan

**Flask Starter Template with Login and Stripe Integration**

**Folder Structure**

```text
myapp/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── payments.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   └── static/
├── config.py
├── requirements.txt
├── run.py
```
**Features**

User registration and login (Flask-Login)

Stripe payment integration

Dashboard with access control

MVP Feature Roadmap

**Week 1: Project Setup**

Flask boilerplate with login system

Stripe test payment integration

Secure user session management

**Week 2: Data Pipeline & Index Filtering**

Connect to financialmodelingprep.com/api

Pull data for QQQ, VGT, SPY tickers

Filter companies with:

Positive sales growth

High profit margin

Low debt/equity (< threshold)

**Week 3: Growth Filtering**

Add filters for:
4. Growing free cash flow or EPS (with configurable percentage)
5. Stock buyback programs (repurchase data)

**Week 4: ChatGPT Wide Moat Analysis**

Integrate GPT API call to classify companies as "wide moat"

Save and cache responses

**Week 5: Free Cash Flow Forecasting**

Extract average historical FCF growth rate

Project FCF for 15 & 20 years using DCF model:

Use discount rate based on beta

Deduct latest LT & ST debt, add cash equivalents

Divide by total outstanding shares

**Week 6: UI Dashboard**

Display results in table:

Ticker

Intrinsic value for 15–20 years (highlight green if undervalued)

Current price

Discount to 20Y value (% with red/green color based on sign)

