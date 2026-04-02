API_KEY = "后面填你谷歌拿到的API密钥"
site = "https://xxx.vercel.app"
import requests
urls = [site,site+"/timestamp",site+"/base64"]

for u in urls:
    res = requests.post(
        f"https://indexing.googleapis.com/v3/urlNotifications:publish?key={API_KEY}",
        json={"url":u,"type":"URL_UPDATED"}
    )
    print(u, res.status_code)