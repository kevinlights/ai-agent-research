def analyze_stock_with_plot(ticker: str) -> dict:  # type: ignore[type-arg]
    import os
    from datetime import datetime, timedelta
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import akshare as ak
    import yfinance as yf
    from pytz import timezone  # type: ignore

    # https://akshare.akfamily.xyz/data/stock/stock.html#id61
    import akshare as ak

    os.makedirs("coding", exist_ok=True)

    # stock = yf.Ticker(ticker)

    stock_us_daily_df = ak.stock_us_daily(symbol=ticker, adjust="")
    # print(stock_us_daily_df)
    DATE_FMT = "%Y-%m-%d"
    # print(len(stock_us_daily_df))
    stock_us_daily_df.to_csv(f"coding/stock_us_daily_df_{ticker}.csv", index=False)

    # Get historical data (1 year of data to ensure we have enough for 200-day MA)
    end_date = datetime.now(timezone("UTC"))
    start_date = end_date - timedelta(days=365)
    # hist = stock.history(start=start_date, end=end_date)

    hist = stock_us_daily_df[
        (stock_us_daily_df["date"] >= start_date.strftime(DATE_FMT))
        & (stock_us_daily_df["date"] <= end_date.strftime(DATE_FMT))
    ].reindex()
    print(f"get stock history data: {len(hist)}")

    # Ensure we have data
    if hist.empty:
        return {"error": "No historical data available for the specified ticker."}

    # Compute basic statistics and additional metrics
    # current_price = stock.info.get("currentPrice", hist["close"].iloc[-1])
    # year_high = stock.info.get("fiftyTwoWeekHigh", hist["high"].max())
    # year_low = stock.info.get("fiftyTwoWeekLow", hist["low"].min())

    current_price = hist["close"].iloc[-1]
    year_high = hist["high"].max()
    year_low = hist["low"].min()

    # Calculate 50-day and 200-day moving averages
    ma_50 = hist["close"].rolling(window=50).mean().iloc[-1]
    ma_200 = hist["close"].rolling(window=200).mean().iloc[-1]

    # Calculate YTD price change and percent change
    ytd_start = datetime(end_date.year, 1, 1, tzinfo=timezone("UTC")).strftime(DATE_FMT)
    ytd_data = hist.loc[ytd_start:]  # type: ignore[misc]
    if not ytd_data.empty:
        price_change = ytd_data["close"].iloc[-1] - ytd_data["close"].iloc[0]
        percent_change = (price_change / ytd_data["close"].iloc[0]) * 100
    else:
        price_change = percent_change = np.nan

    # Determine trend
    if pd.notna(ma_50) and pd.notna(ma_200):
        if ma_50 > ma_200:
            trend = "Upward"
        elif ma_50 < ma_200:
            trend = "Downward"
        else:
            trend = "Neutral"
    else:
        trend = "Insufficient data for trend analysis"

    # Calculate volatility (standard deviation of daily returns)
    daily_returns = hist["close"].pct_change().dropna()
    volatility = daily_returns.std() * np.sqrt(252)  # Annualized volatility

    # Create result dictionary
    result = {
        "ticker": ticker,
        "current_price": current_price,
        "52_week_high": year_high,
        "52_week_low": year_low,
        "50_day_ma": ma_50,
        "200_day_ma": ma_200,
        "ytd_price_change": price_change,
        "ytd_percent_change": percent_change,
        "trend": trend,
        "volatility": volatility,
    }

    # Convert numpy types to Python native types for better JSON serialization
    for key, value in result.items():
        if isinstance(value, np.generic):
            result[key] = value.item()

    # Generate plot
    plt.figure(figsize=(12, 6))
    plt.plot(hist.date, hist["close"], label="Close Price")
    plt.plot(hist.date, hist["close"].rolling(window=50).mean(), label="50-day MA")
    plt.plot(hist.date, hist["close"].rolling(window=200).mean(), label="200-day MA")
    plt.title(f"{ticker} Stock Price (Past Year)")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)

    # Save plot to file
    # os.makedirs("coding", exist_ok=True)
    plot_file_path = f"coding/{ticker}_stockprice.png"
    plt.savefig(plot_file_path)
    print(f"Plot saved as {plot_file_path}")
    result["plot_file_path"] = plot_file_path

    return result


# analyze_stock_with_plot("AAPL")