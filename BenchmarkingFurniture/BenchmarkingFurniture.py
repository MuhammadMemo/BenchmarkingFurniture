

from tkinter import Variable
import requests as rs
from bs4 import BeautifulSoup as bs
import pandas as pd
import time as t
import urllib.request as urlReq
import datetime as dt

# list for Company + all
List_Company={"All Company":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
            ,"Smart" : 5,"Carpiture" :6 ,"American" : 7,"ElMalik" : 8}
MesgAfterURL="waiting.... \n"

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

# TO-DO ..Method Get Mffco data
def Mffco(url, headers, campany, category):
    # TO_DO Loop in urls 
    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='product_container')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h3", class_='title'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
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

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get Kabbani data
def Kabbani(url, headers, campany, category):

    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='grid grid--uniform grid-products grid--view-items')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all(class_='grid-view-item__title'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
            # Loop Get Price
            for c in i.find_all(class_='product-price__price regular'):
                     PriceBeforDiscount.append(c.text)
            for c in i.find_all(class_='product-price__price product-price__sale'):
                     Price.append(c.text)

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

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get Egypt data
def Egypt(url, headers, campany, category):

    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='shop-product-content tab-content')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("div", class_='product-title'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
            # Loop Get Price
            global FlagPrice
            #for c in i.find_all("div",class_='product-price'):
            #    if (FlagPrice == 0):
            #         PriceBeforDiscount.append(c.text)
            #         FlagPrice=1
            #    else:
            #        Price.append(c.text)
            #        FlagPrice=0
            p=[]
            for c in i.find_all("div", class_="product-price"):
                 p.append(c.text)

            PriceBeforDiscount = [item.split()[0] for item in p]
            Price = [item.split()[2] for item in p]

            #Price = [item.split()[1] for item in p]

                # Price=PriceBeforDiscount.split("EGP")

            #for c in i.find_all("span"):
            #         Price.append(c.text)
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

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get Hub data
def Hub(url, headers, campany, category):

    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("div" ,id="layerednav-list-products")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("strong", class_='product name product-item-name'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
            # Loop Get Price

            for c in i.find_all("span" ,class_='old-price'):
                     PriceBeforDiscount.append(c.text)
            for c in i.find_all("span" ,class_='special-price'):
                     Price.append(c.text)
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

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get Smart data
def Smart(url, headers, campany, category):

    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("ul", class_='products columns-4')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
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

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()
    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get Carpiture data
def Carpiture(url, headers, campany, category):
    for g in range(len(url)):
        # Get Campany ,Category name
        print (campany[g], category[g]," Downloading...","\n")
        # Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')

        # Filter Products in HTML
        filter_Products = soup.find_all("div", id="mf-shop-content", class_="mf-shop-content")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h2",class_='woo-loop-product__title'):
                Products.append(p.text.strip())
                    # Get category,campany name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])
            # Loop Get Price
            global FlagPrice
            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                if (FlagPrice == 0):
                     Price.append(c.text)
                     FlagPrice=1
                else:
                    PriceBeforDiscount.append(c.text)
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

    df = pd.DataFrame(AllData)
    df=df.drop_duplicates(keep='first')

    print("Downloded  ",len(Products),"  Products")
    #clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get American data
def American(url, headers, campany, category):
    for g in range(len(url)):
        print (campany[g], category[g]," Downloading...","\n")
        #Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')
        #Filter Products in HTML
        filter_Products = soup.find_all(class_='products columns-tablet-2 columns-mobile-2 rey-wcGap-default rey-wcGrid-default columns-4')

        for i in filter_Products:
            #Loop Get Product name
            for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
                Products.append(p.text)
                #Repeat campany,category name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])

             #Loop Get Price
            for c in i.find_all(class_='price'):
                Price.append(c.text.strip())
                PriceBeforDiscount.append(c.text.strip())

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

    # Associate data from lists to dictionary
    AllData = {'Campany': CampanyList, 'Category': CategoryList,
                'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount}

    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
    # TO-DO clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df
# TO-DO ..Method Get ElMalik data
def ElMalik(url, headers, campany, category):
    for g in range(len(url)):
        print (campany[g], category[g]," Downloading...","\n")
        #Get Page HTML
        page = rs.get(url=url[g], headers=headers)
        soup = bs(page.content, 'html.parser')
        #Filter Products in HTML
        filter_Products = soup.find_all("div", class_='products')

        for i in filter_Products:
            #Loop Get Product name
            for p in i.find_all("h3", class_='heading-title product-name'):
                Products.append(p.text)
                #Repeat campany,category name
                CampanyList.append(campany[g])
                CategoryList.append(category[g])

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

    # Associate data from lists to dictionary
    AllData = {'Campany': CampanyList, 'Category': CategoryList,
                'Products': Products, 'Price': Price,'PriceBeforDiscount':PriceBeforDiscount} 
    
    df = pd.DataFrame(AllData)
    print("Downloded  ",len(Products),"  Products")
   # TO-DO clear All variables
    CampanyList.clear()
    CategoryList.clear()
    Products.clear()
    Price.clear()
    PriceBeforDiscount.clear()
    Img.clear()
    AllData.clear()

    print(MesgAfterURL)
    t.sleep(10)
    return df

def getFilter():

    values = List_Company.values()
    while True :

        for k,v in List_Company.items():
               print("Press.",str(v),"->",str(k))
        try:
             campany = int(input('Please enter an Campany Number :\n'))
             if campany in values :
                break
             else:
                print('Sorry... Campany Number.is not invalid..! :')
        except :
               print("Oops... data.is not Correct..! :")
    return campany


def LoadDate(campany):

    keys = List_Company.keys()

    df = pd.read_excel( "C:\\Users\\ism01\\source\\repos\\MuhammadMemo\\BenchmarkingFurniture\\BenchmarkingFurniture\\Datafurniture.xls")
    #df = pd.read_excel("Datafurniture.xls")
    dfcampany=pd.DataFrame()
    dfFinal=pd.DataFrame()
    #Loop in Campany

    for indx in  range(1 ,len(List_Company)) :

        #TO-DO Filter Data base on Campany Number
        if campany!= 0 : campanyname =list(keys)[campany]
        else: campanyname =list(keys)[indx]

        #Get Company Name Data base on filter
        dfcampany = df[df['Campany'] == campanyname]
        dfcampany.reset_index(inplace=True)
        campanyName = dfcampany['Campany']
        categoryName = dfcampany['Category']
        urls = dfcampany['URL']

        if campanyname=='Mffco':
            dfFinal= pd.concat([dfFinal,Mffco(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany!= 0 :
                return dfFinal 
        elif campanyname=='Kabbani':
            dfFinal= pd.concat([dfFinal,Kabbani(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany!= 0 :
                return dfFinal 
        elif campanyname=='Egypt':
            dfFinal= pd.concat([dfFinal,Egypt(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany!= 0 :
                return dfFinal 
        elif campanyname=='Hub':
            dfFinal= pd.concat([dfFinal,Hub(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany !=0 :
               return dfFinal
        elif campanyname=='Smart':
            dfFinal= pd.concat([dfFinal,Smart(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany !=0 :
               return dfFinal 
        elif campanyname=='Carpiture':
            dfFinal= pd.concat([dfFinal,Carpiture(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany !=0 :
                return dfFinal
        elif campanyname=='American':
            dfFinal= pd.concat([dfFinal,American(urls, headers, campanyName, categoryName)],ignore_index=True)
            if campany !=0 :
               return dfFinal
        elif campanyname=='ElMalik':
               dfFinal= pd.concat([dfFinal,ElMalik(urls, headers, campanyName, categoryName)],ignore_index=True)
               if campany!= 0 : 
                  return dfFinal 
    return dfFinal

def ExportData(df):
    print("Data Exporting....")
    df.to_excel("c:\\Product_Details.xlsx")
    print("Finished")
    
def main():
    print("Hello in the Benchmarketing Project...Pleass Select one or all to download Company data from website:\n")
    while True :
       campany = getFilter()
       StartTime=dt.datetime.now()
       df = LoadDate(campany)
       print(df)
       ExportData(df)
       EndTime=dt.datetime.now()
       print("Start Time: ", StartTime ,"End Time:" , EndTime)

       restart = input('\nWould you like to restart? Enter yes.... or press any key to exit.\n')
       if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()