
#base for SolData pull
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time
import csv

#set wd
path_in = 'E:/Path.../' #read tx data in
path_out = 'D:/Path.../' #write csv of signers to

#tx data
tx_id = []

with open(path_in + 'data.csv', encoding="utf-8") as csvinput:
    reader = csv.reader(csvinput, skipinitialspace=True)
    for row in reader:
        if row[4] == '1': #i applied a filter on column 5
            tx_id.append(row[0]) #grab all tx ids column 1 in csv
        else:
            pass

tx_id.pop(0) #remove first element what is TxHash the col header 

print("TxHash Count: ",len(tx_id))

#webscrape
solscan = "https://solscan.io/tx/" #we'll add tx here

i = 0
signer = [] #then instead of making a new list called signer add this column to the data frame

for i in range(len(tx_id)):

    #url
    FinalURL = solscan + tx_id[i]

    #web scrape
    driver = webdriver.Chrome()
    driver.get(FinalURL)
    time.sleep(5)

    web_data = driver.page_source
    #print(FinalURL)

    #pull all attribute data
    soup =bs(web_data, "html.parser")
    #print(soup)

    for a in soup.find_all("a", href=True, limit=3):
        
        if "/account/" in a['href']:
            signer.append([tx_id[i], "|", a['href'].replace("/account/","")])
            print ("signer: ", a['href'].replace("/account/",""))

    #iterate
    i += 1
    print(i,"/",len(tx_id))

df = pd.DataFrame(signer)
df.to_csv(path_out + "signers.csv") #this will need to be update to a dataframe






