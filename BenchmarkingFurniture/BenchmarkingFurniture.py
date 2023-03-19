
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


# list for month + all
List_Company={ "all":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
            ,"Smart" : 5,"Carpiture" :6 ,"American" : 7}

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
            CampanyList.append(campany)
            CategoryList.append(category)

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
    
    df = pd.DataFrame(AllData)
  
   #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()
 
    return df

# Mathod Get Mffco data
def Mffco(url, headers, campany, category):
    # Get Campany ,Category name

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
            CampanyList.append(campany)
            CategoryList.append(category)
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
    df = pd.DataFrame(AllData)
  
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()
    return df
 

def getFilter():
   #List_Company={ "all":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
   #         ,"Smart" : 5,"Carpiture" :6 ,"American" : 7}

    keys = List_Company.keys()
    values = List_Company.values()

    while True :
        for k,v in List_Company.items():
               print("Press.",str(v),"-->",str(k))
        
        campany = int(input('Please enter an Campany Number :\n'))
        if campany in values:
            break
        else:
             print('Sorry... Campany Number.is not invalid..! :')
    key, value = list(List_Company.items())[campany]
    print(key)
    return key

def LoadDate(campany):
    if campany!='' :
        df = pd.read_excel("Datafurniture.xls")
        dfCampany = df[df['Campany'] == campany]
        dfCampany.reset_index(inplace=True)

        campanyName = dfCampany['Campany']
        categoryName = dfCampany['Category']
        urls = dfCampany['URL']
        dfcampny=pd.DataFrame()   

    if campany=='' : 
        exit()
    elif campany=='Mffco' : 
        for g in range(len(urls)):
            dfcampny=dfcampny.append(Mffco(urls[g], headers, campanyName[g], categoryName[g]),ignore_index=True)
            t.sleep(10)
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
    dfcampny.to_excel("h:\Product_Details.xlsx")

def main():
     
    while True :
       campany = getFilter()
       df = LoadDate(campany)
       print(df)
       restart = input('\nWould you like to restart? Enter yes or press any key to exit.\n')
       if restart.lower() != 'yes':
            break
        #Save Data In Excel
     #  FinalDatadf.to_excel("h:\Product_Details.xlsx")

   

if __name__ == "__main__":
    main()
   
   
