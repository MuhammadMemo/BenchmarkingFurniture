


import requests as rs
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

import time as t
import urllib.request as urlReq
import datetime as dt


# list for Company + all
ListOfCompany={"All Company":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
            ,"Smart" : 5,"Carpiture" :6 ,"American" : 7,"ElMalik" : 8}
# list for Category + all
ListOfCategory ={'All Category':0, 'MASTER BEDROOMS' :1 ,'TEEN BEDROOMS':2
                 ,'KIDS BEDROOMS':3,'DINING ROOMS':4,'Antrehat':5,'Salon':6,'Corner':7}

#Public headers To Pass All Methods
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#Public Variables
Products = []
Price = []
PriceBeforDiscount=[]
CampanyList = []
CategoryList = []
FlagPrice=0
Img = []
imgList = []
imgUrl = []

# TO-DO ..Method To Get Mffco data
def MffcoFormat(soup, campany, category):

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


    print("Downloded  ",len(Products),"  Products\n")
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
# TO-DO ..Method To Get Kabbani data
def KabbaniFormat(soup, campany, category):

    # Filter Products in HTML
    filter_Products = soup.find_all("div", class_='grid grid--uniform grid-products grid--view-items')
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all(class_='grid-view-item__title'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campany)
            CategoryList.append(category)
        # Loop Get Price
        for c in i.find_all(class_='product-price__price regular'):
                    PriceBeforDiscount.append(c.text)
        for c in i.find_all(class_='product-price__price product-price__sale'):
                    Price.append(c.text)

    print("Downloded : ",len(Products),"  Products\n")

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
# TO-DO ..Method To Get Egypt data
def EgyptFormat(soup, campany, category):

    # Filter Products in HTML
    filter_Products = soup.find_all("div", class_='shop-product-content tab-content')
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("div", class_='product-title'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campany)
            CategoryList.append(category)
        # Loop Get Price
        global FlagPrice
        p=[]
        for c in i.find_all("div", class_="product-price"):
                p.append(c.text)
        PriceBeforDiscount = [item.split()[0] for item in p]
        Price = [item.split()[2] for item in p]

    print("Downloded : ",len(Products),"  Products\n")

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
# TO-DO ..Method To Get Hub data
def HubFormat(soup, campany, category):

    # Filter Products in HTML
    filter_Products = soup.find_all("div" ,id="layerednav-list-products")
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("strong", class_='product name product-item-name'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campany)
            CategoryList.append(category)
        # Loop Get Price

        for c in i.find_all("span" ,class_='old-price'):
                    PriceBeforDiscount.append(c.text)
        for c in i.find_all("span" ,class_='special-price'):
                    Price.append(c.text)

    print("Downloded : ",len(Products),"  Products\n")

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
# TO-DO ..Method To Get Smart data
def SmartFormat(soup, campany, category):

    # Filter Products in HTML
    filter_Products = soup.find_all("ul", class_='products columns-4')
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campany)
            CategoryList.append(category)
        global FlagPrice
        for c in i.find_all(class_='woocommerce-Price-amount amount'):
            if (FlagPrice == 0):
                    PriceBeforDiscount.append(c.text)
                    FlagPrice=1
            else:
                Price.append(c.text)
                FlagPrice=0

    print("Downloded : ",len(Products),"  Products\n")
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
# TO-DO ..Method To Get Carpiture data
def CarpitureFormat(soup, campany, category):

    # Filter Products in HTML
    filter_Products = soup.find_all("div", id="mf-shop-content", class_="mf-shop-content")
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("h2",class_='woo-loop-product__title'):
            Products.append(p.text.strip())
                # Get category,campany name
            CampanyList.append(campany)
            CategoryList.append(category)
        # Loop Get Price
        global FlagPrice
        for c in i.find_all(class_='woocommerce-Price-amount amount'):
            if (FlagPrice == 0):
                    Price.append(c.text)
                    FlagPrice=1
            else:
                PriceBeforDiscount.append(c.text)
                FlagPrice=0

    print("Downloded : ",len(Products),"  Products\n")
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
# TO-DO .Method To Get American data
def AmericanFormat(soup, campany, category):

    #Filter Products in HTML
    filter_Products = soup.find_all(class_='products columns-tablet-2 columns-mobile-2 rey-wcGap-default rey-wcGrid-default columns-4')

    for i in filter_Products:
        #Loop Get Product name
        for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
            Products.append(p.text)
            #Repeat campany,category name
            CampanyList.append(campany)
            CategoryList.append(category)

            #Loop Get Price
        for c in i.find_all(class_='price'):
            Price.append(c.text.strip())
            PriceBeforDiscount.append(c.text.strip())


    print("Downloded : ",len(Products),"  Products\n")
    # Associate data from lists to dictionary
    AllData = {'Campany': CampanyList, 'Category': CategoryList,
                'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount}

    df = pd.DataFrame(AllData)

    # TO-DO clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()


    return df
# TO-DO ..Method To Get ElMalik data
def ElMalikFormat(soup, campany, category):

    filter_Products = soup.find_all("div", class_='products')

    for i in filter_Products:
        #Loop Get Product name
        for p in i.find_all("h3", class_='heading-title product-name'):
            Products.append(p.text)
            #Repeat campany,category name
            CampanyList.append(campany)
            CategoryList.append(category)

            #Loop Get Price
        for c in i.find_all(class_='woocommerce-Price-amount amount'):
            PriceBeforDiscount.append(c.text.strip())
            Price.append(c.text.strip())
                #Loop Get Images name
        #for g in i.find_all('img'):
        #   Img.append(g['src'])
              
        # Sleep before Next URL
    #    for u in range(len(img)):
    #       opener = urlReq.build_opener()
    #       opener.addheaders = [('User-Agent', 'MyApp/1.0')]
    #       urlReq.install_opener(opener)
    #       imgUrl="https:" + img[u]
    # #     urlReq.urlretriev(imgUrl,str(u)+".jpg"+ Campany +"/"+ Category + "/" +"Name")
    #       imgList.append(imgUrl)
    print("Total Downloded : ",len(Products),"  Products\n")
    # Associate data from lists to dictionary
    AllData = {'Campany': CampanyList, 'Category': CategoryList,
                'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount} 
    
    df = pd.DataFrame(AllData)

   # TO-DO clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    return df
# TO-DO Get Filter From user
def getFilter():

    valuesCompany = ListOfCompany.values()
    valuesCategory = ListOfCategory.values()
    while True :
        for k,v in ListOfCompany.items():
               print("Press:",str(v),"->",str(k))
        try:
             campany = int(input('Please enter an Campany Number :\n'))
             if campany in valuesCompany :
                break
             else:
                print('Sorry... Campany Number.is not invalid..! :')
        except :
               print("Oops... data.is not Correct..! :")
    while True :
        for k1,v1 in ListOfCategory.items():
            print("Press:",str(v1),"->",str(k1))
        try:
             category=int(input('Please enter an Category Number :\n'))
             if category in valuesCategory :
                break
             else:
                  print('Sorry... Category Number.is not invalid..! :')
        except :
                print("Oops... data.is not Correct..! :")
    return campany,category

# TO-DO Get Filter From data Source
def getFilterData(campany,category):

    keysCompany = ListOfCompany.keys()
    keysCategory = ListOfCategory.keys()

    df = pd.read_excel( "Datafurniture.xls")
    dfcampany=pd.DataFrame()

    if campany!= 0 : 
        campanyname =list(keysCompany)[campany]
        dfcampany = df[df['Campany'] == campanyname]
    else : dfcampany =df

    if category!= 0 : 
        categoryname =list(keysCategory)[category]
        dfcampany = dfcampany[dfcampany['Category'] == categoryname]

    dfcampany.reset_index(inplace=True)
    campanyName = dfcampany['Campany']
    categoryName = dfcampany['Category']
    urls = dfcampany['URL']

    return campanyName,categoryName,urls


# Loding Data Base on Campany,Category Filter
def LoadDate(campanyName,categoryName,urls):
# Select Company Method
    dfFinal=pd.DataFrame()
    # TO_DO Loop in urls 
    for g in range(len(urls)):
        # TO_DO Connect urls 
        page = rs.get(url=urls[g], headers=headers)
        # Get Page HTML
        soup = bs(page.content, 'html.parser')
        if page.status_code == 404 :
            print("Connection is Not Found!")
            break
        else :
            print ("Connection is OK \n","Downloading...",campanyName[g], categoryName[g],"\n")
        # Filter Products in HTML
        if campanyName[g]=='Mffco':
            dfFinal= pd.concat([dfFinal,MffcoFormat(soup ,campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='Kabbani':
            dfFinal= pd.concat([dfFinal,KabbaniFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='Egypt':
            dfFinal= pd.concat([dfFinal,EgyptFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='Hub':
            dfFinal= pd.concat([dfFinal,HubFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='Smart':
            dfFinal= pd.concat([dfFinal,SmartFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='Carpiture':
            dfFinal= pd.concat([dfFinal,CarpitureFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='American':
            dfFinal= pd.concat([dfFinal,AmericanFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)
        elif campanyName[g]=='ElMalik':
            dfFinal= pd.concat([dfFinal,ElMalikFormat(soup, campanyName[g], categoryName[g])],ignore_index=True)

        page.close()
        t.sleep(5)
        print("The Connection Has been Closed\n","Waiting.... \n")
    return dfFinal

def ExportData(df):
    print("Data Exporting....")
    df.to_excel("c:\\ProductDetails.xlsx","r")
    print("Finished!")

def DataCleaning(df):

    #getVals = list([val for val in ini_string if val.isalnum()])
    #result = "".join(getVals)

    df=df.drop_duplicates(keep='first')
   # df['Price']=df['Price'].replace('LE','',inplace=True)

    #df['Price']= df['Price'][df['Price'].str.isalpha()] = ''

   # df['Price'] = df['Price'].str.replace('LE','')
   # df['Price'] = df['Price'].str.replace('EGP','')
   # df['Price'] = df['Price'].str.replace('Special Price','')
   # #df['Price'] = df['Price'].str.replace("ج.م.",'', regex=True)
   # df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('LE','')
   # df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('EGP','')
   # df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('Regular Price','')
   ## df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace("ج.م.","", regex=True)
   # df['Price'] = df['Price'].str.replace(',','')
   # df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace(',','')
   # df['Price'] = df['Price'].str.replace('٬','')
   # df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('٬','')
    
   # #df['Price'] = df['Price'].astype('int')

    #df['PriceBeforDiscount']=df['PriceBeforDiscount'].astype('int')

    #df['Price'] = df['Price'].str.replace('\W', '', regex=True)
    df['Price'] = df['Price'].str.replace('.00', '', regex=True)
    df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('.00', '', regex=True)
    df['Price'] = df['Price'].str.replace('\D', '', regex=True)
    df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\D', '', regex=True)

    #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\W', '', regex=True)
    #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\s', '', regex=True)

    #df['Price']=df['Price'].replace(['EGP','LE ',','],'', regex=True)
    return df

def main():
    print("Hello in the Benchmarketing Project...Pleass Select one or all to download Company data from website:\n")
    while True :
       campany,category = getFilter()
       StartTime=dt.datetime.now()
       campany,category,url =getFilterData(campany,category)
       df = LoadDate(campany,category,url)
       df1 = DataCleaning(df)
       print(df1)
       ExportData(df1)

       EndTime=dt.datetime.now()
       print("Start Time: ", StartTime ,"End Time:" , EndTime)

       restart = input('\nWould you like to restart? Enter yes.... or press any key to exit.\n')
       if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()