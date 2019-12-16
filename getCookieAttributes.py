from urllib.request import HTTPCookieProcessor,build_opener
from datetime import datetime
from http.cookiejar import CookieJar
jar= CookieJar()
opener = build_opener(HTTPCookieProcessor(jar))
opener.open('http://www.github.com')
Cookies = list(jar)
for item in Cookies:    
    print(item.name,'Value:',item.value,'Expiers:',item.expires,'HttpOnly:',item.get_nonstandard_attr('HttpOnly'),'Secure:',item.secure)        
    if item.expires != None:        
       print( datetime.fromtimestamp(item.expires))
        