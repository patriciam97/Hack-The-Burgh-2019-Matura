import hashlib
import hmac
import base64
import urllib.request, json

api_key     = 'V37UcPDfsVDiaYgs'
secret_key  = b'yOjBov7vc-0op26qkHmaLOL4abzb34oK'
query       = ('/events?year=2012&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2012       = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature


query       = ('/events?year=2013&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2013       = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2014&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2014         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2015&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2015         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2016&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2016       = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2017&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2017         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2018&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2018         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

query       = ('/events?year=2019&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url2019         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature




import urllib.request
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    for p in data:
        print('festival id: ' + p)
        break
    #print(data)
