#coding=utf-8
import urllib2
url="http://apis.baidu.com/heweather/weather/free?city=beijing"
req=urllib2.Request(url)
req.add_header("apikey", "09d988a704224c14e62843579a2cb87b")
resp=urllib2.urlopen(req)
content=resp.read()
if (content):
    print content