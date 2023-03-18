
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:02:34 2023
@author: Muhammad Mahmoud
"""


import requests as rs
from bs4 import BeautifulSoup as bs
import pandas as pd
import time as t
import urllib.request as urlReq
import requests

# list for month + all
List_Company=['0..all','1..Mffco','2..Kabbani','3..Egypt','4..Hub'
            ,'5..Smart','6..Carpiture','7..American']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#df = pd.read_excel("Datafurniture.xls")
#url="https://github.com/MuhammadMemo/BenchmarkingFurniture/blob/6e044ecf25f743ee036dd804d3afc96e0f48c673/BenchmarkingFurniture/Datafurniture.xls"

#file=requests.get(url)
#df = pd.read_excel(file)
#FinalDatadf=pd.DataFrame(file)
FinalDatadf=pd.DataFrame()

Products = []
Price = []
PriceBeforDiscount=[]
CampanyList = []
CategoryList = []
FlagPrice=0
Img = []
imgList = []
imgUrl = []

#Mathod Get ElMalik data
def ElMalik(url, headers, campany, category):
    
    for g in range(len(url)):
        #Get Campany ,Category name
        campanyName = campany[g]
        categoryName = category[g]
        #Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')
        #Filter Products in HTML
        filter_Products = soup.find_all("div", class_='products')

        for i in filter_Products:
            #Loop Get Product name
            for p in i.find_all("h3", class_='heading-title product-name'):
                Products.append(p.text)
                 #Get category,campany name
                CampanyList.append(campanyName)
                CategoryList.append(categoryName)

                #Loop Get Price
            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                PriceBeforDiscount.append(0)
                Price.append(c.text.strip())
                 #Loop Get Images name
            #for g in i.find_all('img'):
            #   Img.append(g['src'])
              
        # Sleep before Next URL
        t.sleep(10)
    #    for u in range(len(img)):
    #       opener = urlReq.build_opener()
    #       opener.addheaders = [('User-Agent', 'MyApp/1.0')]
    #       urlReq.install_opener(opener)
    #       imgUrl="https:" + img[u]
    # #     urlReq.urlretriev(imgUrl,str(u)+".jpg"+ Campany +"/"+ Category + "/" +"Name")
    #       imgList.append(imgUrl)
        
        AllData = {'Campany': CampanyList, 'Category': CategoryList,
                   'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount} 
    
        DFElMalik = pd.DataFrame(AllData)
  
   #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()
 
    return DFElMalik

    # Mathod Get Mffco data
def Mffco(url, headers, campany, category):
    # Get Campany ,Category name
    campanyName = campany
    categoryName = category
    url=url
    # Get Page HTML
    page = rs.get(url=url, headers=headers)
    soup = bs(page.content, 'html.parser')

    # Filter Products in HTML
    filter_Products = soup.find_all("div", class_='product_container')
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("h3", class_='title'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campanyName)
            CategoryList.append(categoryName)
        # Loop Get Price
        global FlagPrice
        for c in i.find_all(class_='woocommerce-Price-amount amount'):
            if (FlagPrice == 0):
                    PriceBeforDiscount.append(c.text)
                    FlagPrice=1
            else:
                Price.append(c.text)
                FlagPrice=0
        #Loop Get Images name
        #for g in i.find_all('img'):
        #    Img.append(g['src'])
    # Sleep before Next URL
    t.sleep(10)
# Image Download
        #  
    # t.sleep(100)
#    for u in range(len(img)):
#       opener = urlReq.build_opener()
#       opener.addheaders = [('User-Agent', 'MyApp/1.0')]
#       urlReq.install_opener(opener)
#       imgUrl="https:" + img[u]
# #     urlReq.urlretriev(imgUrl,str(u)+".jpg"+ Campany +"/"+ Category + "/" +"Name")
#       imgList.append(imgUrl)
        
    AllData = {'Campany': CampanyList, 'Category': CategoryList,
                'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount}  
#global FinalDatadf
    DFMffco = pd.DataFrame(AllData)
  
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()
    return DFMffco
 
#def getElMalikData():
      #CampanyElMalik = dfElMalik['Campany']
      #CategorElMalik = dfElMalik['Category']
      #urlElMalik = dfElMalik['URL']
      #kdf=ElMalik(urlElMalik, headers, CampanyElMalik, CategorElMalik)
      #FinalDatadf=FinalDatadf.append(df,ignore_index=True)

def FilterData(campany):
    if campany!='' :
        df = pd.read_excel("Datafurniture.xls")
        dfCampany = df[df['Campany'] == campany]
        dfCampany.reset_index(inplace=True)

        campanyName = dfCampany['Campany']
        categoryName = dfCampany['Category']
        urls = dfCampany['URL']
           
    if campany=='' : 
        print(0)
        exit()
    elif campany=='Mffco' : 
        for g in range(len(urls)):
              dfmffco=  Mffco(urls[g], headers, campanyName[g], categoryName[g]) 
              dfmffco=dfmffco.append(dfmffco,ignore_index=True)
              dfmffco.to_excel("h:\Product_Details.xlsx")
              break
    elif campany=='':
        # getElMalikData()
            print(2)
    elif campany=='':
        # getElMalikData()
            print(3)
    elif campany=='':
        # getElMalikData()
            print(4)
    elif campany=='':
        # getElMalikData()
            print(5)
    elif campany=='':
        # getElMalikData()
            print(6)
    elif campany=='':
        # getElMalikData()
            print(7)

    

def main():

    #List_Company=['0..all','1..Mffco','2..Kabbani','3..Egypt','4..Hub'
    #        ,'5 Smart','6..Carpiture','7..American']
    for c in List_Company:
           print('Press:',c)
           
    while True :
       Campany = int(input('Please enter an Campany Number :\n'))
       if Campany==0 : 
            print(0)
       elif Campany==1 : 
          FilterData('Mffco')
       elif Campany==2:
            # getElMalikData()
              print(2)
       elif Campany==3:
            # getElMalikData()
              print(3)
       elif Campany==4:
            # getElMalikData()
              print(4)
       elif Campany==5:
            # getElMalikData()
              print(5)
       elif Campany==6:
            # getElMalikData()
              print(6)
       elif Campany==7:
            # getElMalikData()
              print(7)
       else :
            break
        #Save Data In Excel
     #  FinalDatadf.to_excel("h:\Product_Details.xlsx")
        
  
    print('Done')

   

if __name__ == "__main__":
    main()
   
   
