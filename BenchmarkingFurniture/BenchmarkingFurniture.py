


from msilib.schema import Class
import requests as rs
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

import time as t
import urllib.request as urlReq
import datetime as dt


class CompanyBenchmarking:

    def __init__(self):
        print("# Hello in the Benchmarketing Project# \nPleass Select one or all to download Company data from website:\n")
        # list for Company + all
        self.__ListOfCompany={"All Company":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
                    ,"Smart" : 5,"Carpiture" :6 ,"American" : 7,"ElMalik" : 8}
        # list for Category + all
        self.__ListOfCategory ={'All Category':0, 'MASTER BEDROOMS' :1 ,'TEEN BEDROOMS':2
                         ,'KIDS BEDROOMS':3,'DINING ROOMS':4,'Antrehat':5,'Salon':6,'Corner':7}

        #Public headers To Pass All Methods
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

        #Public Variables
        self.__Products = []
        self.__Price = []
        self.__PriceBeforDiscount=[]
        self.__CampanyList = []
        self.__CategoryList = []
        self.__FlagPrice=0
        self.__Img = []
        self.__imgList = []
        self.__imgUrl = []
        self.__CampanyList=[]
        self.__CategoryList=[]

        self.__campany,self.__category = self.__getFilter__()

        self.__StartTimememe=dt.datetime.now()

        self.__campany,self.__category,self.__url =self.__getFilterData__(self.__campany,self.__category)

        self.__df = self.__dataLoding__(self.__campany,self.__category,self.__url)

        self.__DataFrame=self.__dataCleaning__(self.__df)

        self.__EndTime=dt.datetime.now()

        print("Start Time: ", self.__StartTimememe ,"End Time:" , self.__EndTime)


    # TO-DO ..Method To Get Mffco data
    def __MffcoFormat__(self,soup, campany, category):

        filter_Products = soup.find_all("div", class_='product_container')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h3", class_='title'):
                 self.__Products.append(p.text.strip())
                    # Get category,campany name
                 self.__CampanyList.append(campany)
                 self.__CategoryList.append(category)
            # Loop Get Price

            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                if (self.__FlagPrice == 0):
                        self.__PriceBeforDiscount.append(c.text)
                        self.__FlagPrice=1
                else:
                    self.__Price.append(c.text)
                    self.__FlagPrice=0
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


        print("Downloded  ",len(self.__Products),"  Products\n")
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)
        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO ..Method To Get Kabbani data
    def __KabbaniFormat__(self,soup, campany, category):

        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='grid grid--uniform grid-products grid--view-items')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all(class_='grid-view-item__title'):
                self.__Products.append(p.text.strip())
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)
            # Loop Get Price
            for c in i.find_all(class_='product-price__price regular'):
                        self.__PriceBeforDiscount.append(c.text)
            for c in i.find_all(class_='product-price__price product-price__sale'):
                        self.__Price.append(c.text)

        print("Downloded : ",len(self.__Products),"  Products\n")

        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)

        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO ..Method To Get Egypt data
    def __EgyptFormat__(self,soup, campany, category):

        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='shop-product-content tab-content')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("div", class_='product-title'):
                self.__Products.append(p.text.strip())
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)
            # Loop Get Price
            p=[]
            for c in i.find_all("div", class_="product-price"):
                    p.append(c.text)
            self.__PriceBeforDiscount = [item.split()[0] for item in p]
            self.__Price = [item.split()[2] for item in p]

        print("Downloded : ",len(self.__Products),"  Products\n")

        AllData = {'Campany': self.C__ampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)
        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO ..Method To Get Hub data
    def __HubFormat__(self,soup, campany, category):

        # Filter Products in HTML
        filter_Products = soup.find_all("div" ,id="layerednav-list-products")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("strong", class_='product name product-item-name'):
                self.__Products.append(p.text.strip())
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)
            # Loop Get Price

            for c in i.find_all("span" ,class_='old-price'):
                        self.__PriceBeforDiscount.append(c.text)
            for c in i.find_all("span" ,class_='special-price'):
                        self.__Price.append(c.text)

        print("Downloded : ",len(self.__Products),"  Products\n")

        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)

        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()


        return df
    # TO-DO ..Method To Get Smart data
    def __SmartFormat__(self,soup, campany, category):

        # Filter Products in HTML
        filter_Products = soup.find_all("ul", class_='products columns-4')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
                self.__Products.append(p.text.strip())
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)

            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                if (self.__FlagPrice == 0):
                        self.__PriceBeforDiscount.append(c.text)
                        self.__FlagPrice=1
                else:
                        self.__Price.append(c.text)
                        self.__FlagPrice=0

        print("Downloded : ",len(self.__Products),"  Products\n")
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)

        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO ..Method To Get Carpiture data
    def __CarpitureFormat__(self,soup, campany, category):

        # Filter Products in HTML
        filter_Products = soup.find_all("div", id="mf-shop-content", class_="mf-shop-content")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h2",class_='woo-loop-product__title'):
                self.__Products.append(p.text.strip())
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)
            # Loop Get Price
            global FlagPrice
            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                if (FlagPrice == 0):
                        self.__Price.append(c.text)
                        FlagPrice=1
                else:
                    self.__PriceBeforDiscount.append(c.text)
                    FlagPrice=0

        print("Downloded : ",len(self.__Products),"  Products\n")
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}  

        df = pd.DataFrame(AllData)

        #clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO .Method To Get American data
    def __AmericanFormat__(self,soup, campany, category):

        #Filter Products in HTML
        filter_Products = soup.find_all(class_='products columns-tablet-2 columns-mobile-2 rey-wcGap-default rey-wcGrid-default columns-4')

        for i in filter_Products:
            #Loop Get Product name
            for p in i.find_all("h2", class_='woocommerce-loop-product__title'):
                self.__Products.append(p.text)
                #Repeat campany,category name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)

                #Loop Get Price
            for c in i.find_all(class_='price'):
                self.__Price.append(c.text.strip())
                self.__PriceBeforDiscount.append(c.text.strip())


        print("Downloded : ",len(self.__Products),"  Products\n")
        # Associate data from lists to dictionary
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount}

        df = pd.DataFrame(AllData)

        # TO-DO clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()


        return df
    # TO-DO ..Method To Get ElMalik data
    def __ElMalikFormat__(self,soup, campany, category):

        filter_Products = soup.find_all("div", class_='products')

        for i in filter_Products:
            #Loop Get Product name
            for p in i.find_all("h3", class_='heading-title product-name'):
                self.__Products.append(p.text)
                #Repeat campany,category name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)

                #Loop Get Price
            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                self.__PriceBeforDiscount.append(c.text.strip())
                self.__Price.append(c.text.strip())
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
        print("Total Downloded : ",len(self.__Products),"  Products\n")
        # Associate data from lists to dictionary
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount':self.__PriceBeforDiscount} 
    
        df = pd.DataFrame(AllData)

       # TO-DO clear All variables
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        self.__Img.clear()
        AllData.clear()

        return df
    # TO-DO Get Filter From user
    def __getFilter__(self):

        valuesCompany = self.__ListOfCompany.values()
        valuesCategory = self.__ListOfCategory.values()
        while True :
            for k,v in self.__ListOfCompany.items():
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
            for k1,v1 in self.__ListOfCategory.items():
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
    def __getFilterData__(self,campany,category):

        keysCompany = self.__ListOfCompany.keys()
        keysCategory = self.__ListOfCategory.keys()

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
    def __dataLoding__(self,campanyName,categoryName,urls):
    # Select Company Method
        dfFinal=pd.DataFrame()
        # TO_DO Loop in urls 
        for g in range(len(urls)):
            # TO_DO Connect urls 
            page = rs.get(url=urls[g], headers=self.headers)
            # Get Page HTML
            soup = bs(page.content, 'html.parser')
            if page.status_code == 404 :
                print("Connection is Not Found!")
                break
            if page.status_code != 200:
                print("Cconnection Error UnKnown!")
                break
            else :
                print ("Connection is OK \n","Downloading...",campanyName[g], categoryName[g],"\n")
            # Filter Products in HTML
            if campanyName[g]=='Mffco':
                dfFinal= pd.concat([dfFinal,self.__MffcoFormat__(soup ,campanyName[g], categoryName[g])])
            elif campanyName[g]=='Kabbani':
                dfFinal= pd.concat([dfFinal,self.__KabbaniFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Egypt':
                dfFinal= pd.concat([dfFinal,self.__EgyptFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Hub':
                dfFinal= pd.concat([dfFinal,self.__HubFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Smart':
                dfFinal= pd.concat([dfFinal,self.__SmartFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Carpiture':
                dfFinal= pd.concat([dfFinal,self.__CarpitureFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='American':
                dfFinal= pd.concat([dfFinal,self.__AmericanFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='ElMalik':
                dfFinal= pd.concat([dfFinal,self.__ElMalikFormat__(soup, campanyName[g], categoryName[g])])

            page.close()
            print("The Connection Has been Closed\n","Waiting.... \n")
            t.sleep(5)

            print("Data Cleaning....\n","Waiting.... \n")
            df = self.__dataCleaning__(dfFinal)

        return df

    def __dataCleaning__(self,df):

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
        #df['Price'] = df['Price'].str.replace('.00', '', regex=True)
        #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('.00', '', regex=True)
        #df['Price'] = df['Price'].str.replace('\D', '', regex=True)
        #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\D', '', regex=True)

        #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\W', '', regex=True)
        #df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.replace('\s', '', regex=True)

        #df['Price']=df['Price'].replace(['EGP','LE ',','],'', regex=True)
        return df

    def DisplayData(self):
        print(self.__DataFrame)

    def ExportData(self):
        print("Data Exporting....")
        df= self.__DataFrame
        df.to_excel("c:\\ProductDetails.xlsx")
        print("Finished!")



def main():
    DataCompany= CompanyBenchmarking()
    while True :
       DataCompany.DisplayData()
       DataCompany.ExportData()
       restart = input('\nWould you like to restart? Enter yes.... or press any key to exit.\n')
       if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()