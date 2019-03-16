import hashlib
import hmac
import base64
import urllib.request, json
f= open("data.json","w+")
api_key     = 'V37UcPDfsVDiaYgs'
secret_key  = b'yOjBov7vc-0op26qkHmaLOL4abzb34oK'
query       = ('/events?year=2012&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2013&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2014&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2015&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2016&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2017&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2018&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)

query       = ('/events?year=2019&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature
i=-1
with urllib.request.urlopen(url) as url:
    i=i+1
    data = json.loads(url.read().decode())
    f.write(str(data)+"\n")
    print(data)
