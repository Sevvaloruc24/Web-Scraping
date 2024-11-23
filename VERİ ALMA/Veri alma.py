import requests
from bs4 import BeautifulSoup

def wikipedia_content(title):
    #wikipedia url
    url=f"https://tr.wikipedia.org/wiki/{title}"

    #http get isteği gönderme
    response= requests.get(url)

    #yanıt durumu kontrol
    if response.status_code==200:
        #html icerik analiz için beautifulsoup kullnaım
        soup=BeautifulSoup(response.text,'html.parser')

        #ilgili içerik için uygun etiket
        content=soup.find("div",{"id":"mw-content-text"})

        #içeriği metin olarak döndürme
        return content.get_text()
    else:
        #yanıt alınmazsa hata mesajı döndürme
        return f"Hata:{response.status_code}"
    
 #örnek bir başlık kullanarak wikipedia içeriği alınır
title="Çanakkale"
content=wikipedia_content(title)  
print(content)



