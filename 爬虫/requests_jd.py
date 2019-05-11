import requests
url = "https://item.jd.com/2967929"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

# r.request.headers
# r.request.url