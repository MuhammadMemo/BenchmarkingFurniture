

import requests as rs
from bs4 import BeautifulSoup as bs
import pandas as pd
import time as t
import urllib.request as urlReq


# list for month + all
List_Company={"AllData":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
            ,"Smart" : 5,"Carpiture" :6 ,"American" : 7,"ElMalik" : 8}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#df = pd.read_excel("Datafurniture.xls")
#url="https://github.com/MuhammadMemo/BenchmarkingFurniture/blob/6e044ecf25f743ee036dd804d3afc96e0f48c673/BenchmarkingFurniture/Datafurniture.xls"

#file=requests.get(url)
#df = pd.read_excel(file)
#FinalDatadf=pd.DataFrame(file)

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
    print ("Data Downloading for...",campany, category,url,"\n")
    #Get Page HTML
    page = rs.get(url=url, headers=headers)
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
    print("sleep....\n")
    t.sleep(10)
    return df

# Mathod Get Mffco data
def Mffco(url, headers, campany, category):
    # Get Campany ,Category name
    print ("Data Downloading for...",campany, category,url,"\n")
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
    print("sleep....\n")
    t.sleep(10)
    return df

# Mathod Get Mffco data
def Smart(url, headers, campany, category):
    # Get Campany ,Category name
    print ("Data Downloading for...",campany, category,url,"\n")
    # Get Page HTML
    page = rs.get(url=url, headers=headers)
    soup = bs(page.content, 'html.parser')

    # Filter Products in HTML
    filter_Products = soup.find_all("ul", class_='products columns-4')
    # Loop Get Product name
    for i in filter_Products:
        for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
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
    print("sleep....\n")
    t.sleep(10)
    return df




def getFilter():
   #List_Company={ "all":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
   #         ,"Smart" : 5,"Carpiture" :6 ,"American" : 7}

    
    values = List_Company.values()
    while True :

        for k,v in List_Company.items():
               print("Press.",str(v),"->",str(k))  
        print("Press.","0","->","All\n")
        try:
             campany = int(input('Please enter an Campany Number :\n'))
             if campany in values :
                break
             else:
                print('Sorry... Campany Number.is not invalid..! :')
        except :
               print("Oops... data.is not Correct..! :")

    
  #  #Value= List_Company.values()
  #  if  campany == 0 :
  #          campanyname=list(keys)
  #  else:
  #          campanyname=list(keys)[campany]
  ##indx=list(keys)[campany-1]
    return campany


def LoadDate(campany):

    
    keys = List_Company.keys()
    #values = List_Company.values()
    
      #Value= List_Company.values()
    #if  campany == 0 :
    #        campanyname=list(keys)
    #else:
    #        campanyname=list(keys)[campany]
  # values=campany
    
    df = pd.read_excel( "C:\\Users\\ism01\\source\\repos\\MuhammadMemo\\BenchmarkingFurniture\\BenchmarkingFurniture\\Datafurniture.xls")
    #df = pd.read_excel("Datafurniture.xls")
    dfcampany=pd.DataFrame()
    dfFinal=pd.DataFrame()
    #dfcampny=df
    #print((campany.index()))
    #Loop To Campany Name
    for indx in  range(1,8):

        #TO-DO Filter Data base on Campany Number
        if campany!= 0 : campanyname =list(keys)[campany]
        else: campanyname =list(keys)[indx]

        #Get Company Data base on filter
        dfcampany = df[df['Campany'] == campanyname]
        dfcampany.reset_index(inplace=True)
        campanyName = dfcampany['Campany']
        categoryName = dfcampany['Category']
        urls = dfcampany['URL']

        if campanyname=='Mffco'  : 
            for g in range(len(urls)):
                dfFinal= pd.concat([dfFinal,Mffco(urls[g], headers, campanyName[g], categoryName[g])],ignore_index=True)
            if campany!= 0 :
                return dfFinal 
        elif campanyname=='Kabbani':
                print("Kabbani")
        elif campanyname=='Egypt':

                print("Egypt")
        elif campanyname=='Hub':

                print("Hub")
        elif campanyname=='Smart':
            for g in range(len(urls)):
                dfFinal= pd.concat([dfFinal,Smart(urls[g], headers, campanyName[g], categoryName[g])],ignore_index=True)
            if campany !=0 : break
        elif campanyname=='Carpiture':

                print("Carpiture")
        elif campanyname=='American':

                print("American")
        elif campanyname=='ElMalik':
               for g in range(len(urls)):
                dfFinal= pd.concat([dfFinal,ElMalik(urls[g], headers, campanyName[g], categoryName[g])],ignore_index=True)
               if campany!= 0 : break
    return dfFinal

def ExportData(df):
    print("Data Exporting....")
    df.to_excel("c:\\Product_Details.xlsx")
    print("Finished")
    
def main():
    print("Hello in the Benchmarketing Project...Pleass Select one or all to download Company data from website:\n")
    while True :
       campany = getFilter()
       df = LoadDate(campany)
       print(df)
       ExportData(df)
       restart = input('\nWould you like to restart? Enter yes.... or press any key to exit.\n')
       if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()