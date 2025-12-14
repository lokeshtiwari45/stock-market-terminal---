def calculate_levels(price, signal):
    if signal == "BUY":
        sl = price * 0.97
        target = price * 1.06
    elif signal == "SELL":
        sl = price * 1.03
        target = price * 0.94
    else:
        sl = target = price
    return round(sl,2), round(target,2)
