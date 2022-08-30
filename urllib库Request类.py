from urllib import request,parse
url = 'https://www.httpbin.org/post'
hearders = {
    'User-Agent':'Mozilla/4.0(compatible;MISE 5.5;Windows NT)',
    'Host':'www.httpbin.org'
}
dict = {'name':'germey'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=hearders,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
