def generate_signal(df):
    last = df.iloc[-1]
    score = 0

    if last['RSI'] < 35:
        score += 1
    if last['RSI'] > 65:
        score -= 1
    if last['Close'] > last['EMA20']:
        score += 1
    if last['Close'] < last['EMA20']:
        score -= 1
    if last['MACD'] > last['MACD_signal']:
        score += 1
    if last['MACD'] < last['MACD_signal']:
        score -= 1

    if score >= 2:
        return "BUY", min(90, 60 + score * 10)
    elif score <= -2:
        return "SELL", min(90, 60 + abs(score) * 10)
    else:
        return "HOLD", 50
