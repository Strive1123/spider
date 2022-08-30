import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'name':'germey'}),encoding='utf=8')
response = urllib.request.urlopen('https://www.httpbin.org/post',data=data)
print(response.read().decode('utf=8'))