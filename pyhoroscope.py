# pyhoroscope.py

import requests

def get_today_horoscope(sign):
    url = f"https://aztro.sameerkumar.website?sign={sign}&day=today"
    try:
        response = requests.post(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "date": data.get("current_date"),
                "sunsign": sign,
                "horoscope": data.get("description"),
                "mood": data.get("mood"),
                "compatibility": data.get("compatibility"),
                "color": data.get("color"),
                "lucky_number": data.get("lucky_number"),
                "lucky_time": data.get("lucky_time")
            }
        else:
            return {"error": "API'den veri alınamadı"}
    except Exception as e:
        return {"error": str(e)}
