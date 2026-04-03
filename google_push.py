# 你的API密钥和域名，已自动填好
API_KEY = "AIzaSyBRxZ5gbtnXWwfKPuKr2KbYb0Inv27p-C0"
site = "https://tool-web-coral.vercel.app/"
import requests

urls = [
    f"{site}",
    f"{site}timestamp",
    f"{site}base64",
    f"{site}privacy-policy",
    f"{site}terms-of-service",
    f"{site}about"
]

for url in urls:
    api_url = f"https://indexing.googleapis.com/v3/urlNotifications:publish?key={API_KEY}"
    data = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = requests.post(api_url, json=data)
    print(f"推送 {url}：状态码 {response.status_code}")
    if response.status_code == 200:
        print(f"✅ {url} 推送成功！")
    else:
        print(f"❌ 推送失败，响应：{response.text}")

print("\n✅ 所有链接推送完成！谷歌会在24-48小时内完成收录")
print(f"站点地图地址：{site}sitemap.xml")