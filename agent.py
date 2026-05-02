import requests
import json
from datetime import datetime

def fetch_data():
    data = {
        "status": "ONLINE",
        "last_sync": datetime.now().strftime("%H:%M:%S"),
        "prices": {},
        "ai_state": "bull" # 默认给个看多，测试你的语音引擎
    }
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=10)
        data["prices"]["BTC"] = f"{float(r.json()['price']):,.0f}"
    except:
        data["prices"]["BTC"] = "ERROR"
    
    with open('data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    fetch_data()
