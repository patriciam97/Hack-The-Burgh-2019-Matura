import hashlib
import hmac
import base64

api_key     = 'V37UcPDfsVDiaYgs'
secret_key  = b'yOjBov7vc-0op26qkHmaLOL4abzb34oK'
query       = ('/events?filter=that&key=' + api_key).encode("utf-8")
signature   = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url         = 'https://api.edinburghfestivalcity.com' + query.decode() + '&signature=' + signature

print(url)
