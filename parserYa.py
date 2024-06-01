import requests


def parseyandex():
   st_accept = "text/html" 
   st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

   headers = {
      "Accept": st_accept,
      "User-Agent": st_useragent
   }

   req = requests.get("https://yandex.ru", headers)

   src = req.text
   return src

