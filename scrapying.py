import requests
from bs4 import BeautifulSoup

web = requests.get(f'https://tw.portal-pokemon.com/play/pokedex/0001')
info = BeautifulSoup(web.text,"html.parser")
img = info.select('meta[property="og:image"]') #爬取有property="og:image"屬性的<meta>標籤
imgUrl = img[0]['content']#第0個網址的content內容
print(imgUrl)

#<meta property="og:image" content="https://tw.portal-pokemon.com/play/resources/pokedex/img/pm/cf47f9fac4ed3037ff2a8ea83204e32aff8fb5f3.png">

import os
os.chdir (r'..\ian\Pictures\pokemon') #存檔路徑，windows system use '\'

imgFile = requests.get(imgUrl) #讀圖片資訊
f = open(f'0001.png','wb') #建立0001.png 圖片，開啟路徑寫完整的話，這邊寫檔名即可。 #wb 二進制寫入，write()argument must be str, not bytes 
f.write(imgFile.content) #寫入圖片#write()二進制
f.close()
print('OK')