import requests
r=requests.get('https://item.jd.com/4645290.html', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.status_code)
print(r.encoding)
print(r.text[:2000])
