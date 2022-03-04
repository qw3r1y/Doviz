import socket ,time ,requests

from bs4 import BeautifulSoup 

import tkinter as tk

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("www.google.com",80))
    s.close()
    print("Bağlanıyor")

except Exception:
    print("Lütfen Bağalantıyı Kontrol Ediniz")
    time.sleep(3)
    exit()

url = "https://www.doviz.com"

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

data = soup.find("span", {"data-socket-key":"gram-altin"}).text
data1 = soup.find("span", {"data-socket-key":"USD"}).text
data2 = soup.find("span", {"data-socket-key":"EUR"}).text
data3 = soup.find("span", {"data-socket-key":"GBP"}).text
data4 = soup.find("span", {"data-socket-key":"XU100"}).text
data5 = soup.find("span", {"data-socket-key":"bitcoin"}).text

windows = tk.Tk()
windows.geometry("310x270")
windows.title("Döviz-Borsa")
windows.configure(background="black")

label = tk.Label(windows, text="Döviz-Borsa",font="arial 15 bold", bg="orange")
label.pack()

gramaltin = tk.Label(windows, text="Gram Altın", font="arial 12", bg="yellow")
gramaltin.pack()
gramaltin.place(x = 30 ,y = 45)
goldvalue = tk.Label(windows, text=data,font="arial 12", bg="yellow")
goldvalue.pack()
goldvalue.place(x = 30 ,y = 65)


dolar = tk.Label(windows, text="Dolar", font="arial 12", bg="yellow")
dolar.pack()
dolar.place(x = 200 ,y = 45)
dolarvalue = tk.Label(windows, text=data1,font="arial 12", bg="yellow")
dolarvalue.pack()
dolarvalue.place(x = 200 ,y = 65)



euro = tk.Label(windows, text="Euro", font="arial 12", bg="yellow")
euro.pack()
euro.place(x = 30 ,y = 115)
eurovalue = tk.Label(windows, text=data2,font="arial 12", bg="yellow")
eurovalue.pack()
eurovalue.place(x = 30,y = 135)

sterlin = tk.Label(windows, text="Sterlin", font="arial 12", bg="yellow")
sterlin.pack()
sterlin.place(x = 200 ,y = 115)
sterlinvalue = tk.Label(windows, text=data3,font="arial 12", bg="yellow")
sterlinvalue.pack()
sterlinvalue.place(x = 200 ,y = 135)


bist = tk.Label(windows, text="Bist100", font="arial 12", bg="yellow")
bist.pack()
bist.place(x = 30 ,y = 185)
bistvalue = tk.Label(windows, text=data4,font="arial 12", bg="yellow")
bistvalue.pack()
bistvalue.place(x = 30 ,y = 205)

bitcoin = tk.Label(windows, text="Bitcoin", font="arial 12", bg="yellow")
bitcoin.pack()
bitcoin.place(x = 200 ,y = 185)
bitcoinvalue = tk.Label(windows, text=data4,font="arial 12", bg="yellow")
bitcoinvalue.pack()
bitcoinvalue.place(x = 200 ,y = 205)
windows.mainloop()