from urllib import request

import requests

url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=B7F431C957692322&ie=utf-8&f=8&rsv_bp=1&tn=02003390_50_hao_pg&wd=jiayi&oq=%25E8%25B4%25BE%25E8%25B0%258A&rsv_pq=d56a34cd00bf45d5&rsv_t=0de9RX0gsY%2BhvN%2B%2BGKZUSGzm8KUuiTg46nWL2TA6WElqVclCpd5K8kGiAW28cWaVUAmF1pFBqdx4&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=%E8%B4%BE%E8%B0%8A&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=0&_cr1=28740'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

req=request.Request(url=url,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))
a = response.read().decode('utf-8')
with open('./1.html','w',encoding='utf-8') as fp:
    fp.write(a)
