import random

indicators = ["SMA", "EMA", "MACD", "RSI", "Bollinger Bands"]
signals = ["crossed above", "crossed below", "above", "below"]
actions = ["buy", "sell", "hold"]

def generate_strategy():
    indicator = random.choice(indicators)
    signal = random.choice(signals)
    
    if indicator == "SMA" or indicator == "EMA":
        period = random.randint(5, 50)
    elif indicator == "MACD":
        period = (random.randint(5, 50), random.randint(25, 75), random.randint(5, 25))
    elif indicator == "RSI":
        period = random.randint(5, 50)
    elif indicator == "Bollinger Bands":
        period = random.randint(5, 50)
        std_dev = random.uniform(1, 3)
    
    action = random.choice(actions)
    
    if indicator == "Bollinger Bands":
        strategy = f"If {indicator}({period}, {std_dev}) {signal}: {action}"
    elif indicator == "MACD":
        strategy = f"If {indicator}({period[0]}, {period[1]}, {period[2]}) {signal}: {action}"
    else:
        strategy = f"If {indicator}({period}) {signal}: {action}"
    
    return strategy

for i in range(10):
    print(generate_strategy())
