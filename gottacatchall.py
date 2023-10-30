import os
os.chdir(r'..\ian\Pictures\pokemon')

import requests
from bs4 import BeautifulSoup
import threading #非同步進行
from concurrent.futures import ThreadPoolExecutor #非同步進行
def download(num):
    # add try to escape the accident that could not download
    try:
        web = requests.get(f'https://tw.portal-pokemon.com/play/pokedex/{num}')
        info = BeautifulSoup(web.text,"html.parser")
        img = info.select('meta[property="og:image"]') #爬取有property="og:image"屬性的<meta>標籤
        imgUrl = img[0]['content']#第0個網址的content內容
        imgFile = requests.get(imgUrl) #讀圖片資訊
        f = open(f'{num}.png','wb') #建立0001.png 圖片，開啟路徑寫完整的話，這邊寫檔名即可。 #wb 二進制寫入，write()argument must be str, not bytes 
        f.write(imgFile.content) #寫入圖片#write()二進制
        f.close()
        print(num)
    except:
        print('error')
        pass #accident happended, quit the download function



#method1: Threading. use forloop, dowloading 1~99 images at once.
for i in range(1,1011):
    n = f'{i:04d}'#4位數
    threading.Thread(target=download, args=(n,)).start() #非同步多頭進行



#method2: use current.futures while thread could not work
#numArr = [f'{j:04d}' for j in range(1,100)]  # 建立圖片檔名清單
#executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
#with ThreadPoolExecutor() as executor:
#    executor.map(download, numArr)       # 同時下載圖片，依照順序