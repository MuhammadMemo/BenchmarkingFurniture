


from ast import List

#import convert_numbers
#from itertools import groupby
#from msilib.schema import Class
import requests as rs
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

import time as t
import urllib.request as urlReq
import datetime as dt



class CompanyBenchmarking:

    def __init__(self,FileExcelLoading:str) -> str:

       # list for Company + all
        self.__ListOfCompany={"All Company":0,"Mffco":1,"Kabbani":2,"Egypt":3,"Hub" : 4
                    ,"Smart" : 5,"Carpiture" :6 ,"American" : 7,"ElMalik" : 8}
        # list for Category + all
        self.__ListOfCategory ={'All Category':0, 'MASTER BEDROOMS' :1 ,'TEEN BEDROOMS':2
                         ,'KIDS BEDROOMS':3,'DINING ROOMS':4,'Antrehat':5,'Salon':6,'Corner':7}

        #Public headers To Pass All Methods
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        df = pd.read_excel(FileExcelLoading)
        #Public Variables
        self.__DataFrame=pd.DataFrame(index=None)
        self.__Products = []
        self.__Price = []
        self.__PriceBeforDiscount=[]
        self.__CampanyList = []
        self.__CategoryList = []

        self.__FlagPrice=0
        self.__Img = []
        self.__imgList = []
        self.__imgUrl = []
        self.__errorConnections=0
        self.__successConnection=0


        self.__HelloMessage__()

        self.__campany,self.__category = self.__getFilterUser__()
        self.__StartTime=dt.datetime.now()
        self.__campany,self.__category,self.__url =self.__getFilterData__(df,self.__campany,self.__category)
        self.__DataFrame ,self.__errorConnections,self.__successConnection= self.__dataLoding__(self.__campany,self.__category,self.__url)
        self.__DataFrame=self.__dataCleaning__(self.__DataFrame)
        self.__EndTime=dt.datetime.now()

        print("Start Time: ", self.__StartTime ,"End Time:" , self.__EndTime,"Error Connections",self.__errorConnections ,"Success Connection",self.__successConnection)
        print("Error Connection : ",self.__errorConnections,"Success Connection : ",self.__successConnection)
    def __HelloMessage__(self)-> None:
        print("# Hello in the Benchmarketing Project# \nPleass Select one or all to download Company data from website:\n")
        print("-" * 40)

    # TO-DO ..Method To Get Mffco data
    def __MffcoFormat__(self,soup, campany, category):
        Product = soup.find_all("h3", class_='title')
        #Loop Get Product name
        for p in Product:
            self.__Products.append(p.text)
            # Get category,campany name
            self.__CampanyList.append(campany)
            self.__CategoryList.append(category)
        #tag = soup.ins
            # Loop Get Price
        for a in soup.select('ins'):
            self.__Price.append(a.find_next('bdi').text)
        for b in soup.select('del'):
            self.__PriceBeforDiscount.append(b.find_next('bdi').text)
        print(len(self.__Products),len(self.__Price),len(self.__PriceBeforDiscount))
        p=  np.repeat(self.__Products, 2).tolist()
        c1=  np.repeat(self.__CampanyList, 2).tolist()
        c2=  np.repeat(self.__CategoryList, 2).tolist()
        self.__Products=p
        self.__CampanyList=c1
        self.__CategoryList=c2

        # Printing the value Queen

        #print(dataList)
        #with open ("C:\\Users\\ism01\\Myfile.csv","w") as myFile:
        #    wr = csv.writing(myFile)
            ##for c in i.find_all("span" ,class_="woocommerce-Price-amount amount"):

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
        #if self.__CategoryList=='Corner' :

        #self.__Price=list(dict.fromkeys( self.__Price))
        #self.__PriceBeforDiscount=list(dict.fromkeys(self.__PriceBeforDiscount))
        print(len(self.__Products),len(self.__Price),len(self.__PriceBeforDiscount))
        print("Downloded  ",len(self.__Products),"  Products\n")
    ##print(len(self.__Price),len(self.__Products),len(self.__PriceBeforDiscount))
        AllData = {'Campany': self.__CampanyList, 'Category': self.__CategoryList,
                    'Products': self.__Products, 'Price': self.__Price,'PriceBeforDiscount': self.__PriceBeforDiscount}  
        df = pd.DataFrame(AllData)
        #clear All variables
        #print(df)
        self.__CampanyList.clear()
        self.__CategoryList.clear()
        self.__Products.clear()
        self.__Price.clear()
        self.__PriceBeforDiscount.clear()
        #p.clear()
        #c1.clear()
        #c2.clear()
        #self.__Img.clear()
        AllData.clear()
        return df
    # TO-DO ..Method To Get Kabbani data
    def __KabbaniFormat__(self,soup, campany, category):
        # Filter Products in HTML
        filter_Products = soup.find_all("div", class_='grid grid--uniform grid-products grid--view-items')
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all(class_='grid-view-item__title'):
                self.__Products.append(p.text)
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
                self.__Products.append(p.text)
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
    # TO-DO ..Method To Get Hub data
    def __HubFormat__(self,soup, campany, category):
        # Filter Products in HTML
        filter_Products = soup.find_all("div" ,id="layerednav-list-products")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("strong", class_='product name product-item-name'):
                self.__Products.append(p.text)
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
                self.__Products.append(p.text)
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
        filter_Products = soup.find_all("ul", class_="products columns-4")
        # Loop Get Product name
        for i in filter_Products:
            for p in i.find_all("h2",class_='woo-loop-product__title'):
                self.__Products.append(p.text)
                    # Get category,campany name
                self.__CampanyList.append(campany)
                self.__CategoryList.append(category)
            # Loop Get Price
            for c in i.find_all(class_='woocommerce-Price-amount amount'):
                if (self.__FlagPrice == 0):
                        self.__Price.append(c.text)
                        self.__FlagPrice=1
                else:
                    self.__PriceBeforDiscount.append(c.text)
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
            for c in  i.find_all("span", class_="woocommerce-Price-amount amount"):
                self.__Price.append(c.text)
                self.__PriceBeforDiscount.append(c.text)
                        #print(c.text)
            for o in self.__Price:
                if o =="174,900 EGP" and  category=="MASTER BEDROOMS":
                        self.__Price.remove(o)
                        self.__PriceBeforDiscount.remove(o)
        print("Downloded : ",len(self.__Products),"  Products\n")
        # Associate data from lists to dictionary
        #print(len(self.__Products),len(self.__Price),len(self.__PriceBeforDiscount))
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
                self.__PriceBeforDiscount.append(c.text)
                self.__Price.append(c.text)
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
    def __getFilterUser__(self):

        valuesCompany = self.__ListOfCompany.values()
        valuesCategory = self.__ListOfCategory.values()
        while True :
            for k,v in self.__ListOfCompany.items():
                   print("Press:",str(v),"->",str(k))
            try:
                 campany = int(input('Please enter an Campany Number :\n'))
                 if campany in valuesCompany :
                    print("_"*40)
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
                    print("_"*40)
                    break
                 else:
                      print('Sorry... Category Number.is not invalid..! :')
            except :
                    print("Oops... data.is not Correct..! :")
        return campany,category

    # TO-DO Get Filter From data Source

    def __getFilterData__(self,df,campany : int,category : int):
        keysCompany = self.__ListOfCompany.keys()
        keysCategory = self.__ListOfCategory.keys()

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

    def __dataLoding__(self,campanyName : List,categoryName : List,urls :List)-> List:
        # TO_DO Loop in urls 
        errorConnection=0
        SuccessConnection=0
        for g in range(len(urls)):
            # TO_DO Connect urls 
            page = rs.get(url=urls[g], headers=self.__headers)
            # Get Page HTML
            soup = bs(page.content, 'html.parser',)
            #html5lib
            if page.status_code == 404 :
                print("Connection is Not Found!",urls[g],campanyName[g], categoryName[g],"\n")
                errorConnection +=1
                continue
            if page.status_code != 200:
                print("Cconnection Error UnKnown!",urls[g],campanyName[g], categoryName[g],"\n")
                errorConnection +=1
                continue
            else :
                print ("Connection is OK :","Downloading...",campanyName[g], categoryName[g],"\n")
                SuccessConnection += 1
            # Filter Products in HTML
            if campanyName[g]=='Mffco':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__MffcoFormat__(soup ,campanyName[g], categoryName[g])])
            elif campanyName[g]=='Kabbani':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__KabbaniFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Egypt':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__EgyptFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Hub':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__HubFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Smart':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__SmartFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='Carpiture':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__CarpitureFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='American':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__AmericanFormat__(soup, campanyName[g], categoryName[g])])
            elif campanyName[g]=='ElMalik':
                self.__DataFrame= pd.concat([self.__DataFrame,self.__ElMalikFormat__(soup, campanyName[g], categoryName[g])])
            page.close()
            print("The Connection Has been Closed\n","Waiting.... \n")
            #t.sleep(5)
        return  self.__DataFrame,errorConnection,SuccessConnection

    def __dataCleaning__(self,df):
        #  TO_DO Remove duplicates
        df.reset_index(inplace=True,drop=True)

        df=df.drop_duplicates(keep='first')
        #  TO_DO Price Cleaning
        removabl=[',','٬','ج.م.']
        for char in removabl:
            df['Price']=df['Price'].astype(str).str.replace(char,'', regex=True)
            df['PriceBeforDiscount']=df['PriceBeforDiscount'].astype(str).str.replace(char,'', regex=True)
        df['Price'] = df['Price'].str.extract(pat='(\d+)', expand=False)
        df['PriceBeforDiscount'] = df['PriceBeforDiscount'].str.extract(pat='(\d+)', expand=False)
        df['PriceBeforDiscount']=df['PriceBeforDiscount'].astype('int')
        df['Price'] = df['Price'].astype('int')
        #  TO_DO Products Cleaning
        df['Products'] = df['Products'].str.strip()
        #  TO_DO Products Category delete for outlier values
        delete=['فوتيه مارفل','كرسى هزاز مودرن']
        for char in delete:
              df = df.loc[~((df['Products']==char))]
             #df.loc[(df.Products == char ), 'Category'] = 'karacey'
        df.reset_index(inplace=True,drop=True)
        #df.rename(index={0: 'index'},inplace=True)
        #df = df.set_index('index',inplace=True)
        #df = df.rename(columns={'': 'index'},inplace=True)
        return df

    def DataDisplay(self):
        pd.set_option('colheader_justify', 'center')
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows', None)
        print(self.__DataFrame)
        print("-" * 40)
        return True

    def DataInfo(self):
        print(self.__DataFrame.info(memory_usage='deep'))
        print("-" * 40)

    def DataStatistic(self):
        pd.set_option('colheader_justify', 'center')
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows', None)
        df1=self.__DataFrame
        df2=self.__DataFrame
        df3=self.__DataFrame
        df4=self.__DataFrame
        df1=df1.groupby(['Campany','Category'])['Price'].describe()
        print(df1)
        print("-" * 40)
        df2=df2.groupby(['Category'])['Price'].describe()
        print(df2)
        print("-" * 40)
        df3=df3.groupby(['Campany'])['Price'].describe()
        print(df3)
        print("-" * 40)
        df4=df4.groupby(['Category','Campany'])['Price'].describe()
        print(df4)
        print("-" * 40)


    def DataExport(self):

        df=self.__DataFrame
        df1=self.__DataFrame.groupby(['Campany','Category'])['Price'].describe()
        df2=self.__DataFrame.groupby(['Category'])['Price'].describe()
        df3=self.__DataFrame.groupby(['Campany'])['Price'].describe()
        df4=self.__DataFrame.groupby(['Category','Campany'])['Price'].describe()
        print("Data Exporting....")
        with pd.ExcelWriter('F:\DataStatistic.xlsx') as writer:
            df.to_excel(writer, sheet_name='Product Details')
            df1.to_excel(writer, sheet_name='Campany and Category')
            df2.to_excel(writer, sheet_name='Category')
            df3.to_excel(writer, sheet_name="Campany")
            df4.to_excel(writer, sheet_name="Category and Campany")

        print("Finished!")
        print("-" * 40)
        return True

    def DataGraph(self):
        df= self.__DataFrame
        #print(df.head())
        Count_Products=df.groupby(['Campany','Category'])['Products'].count()
        agv_Price=df.groupby(['Campany','Category'])['Price'].mean()
        print(Count_Products,agv_Price)

        fig, axs = plt.subplots(1, 3, figsize=(9,5), sharey=True)
        #axs[0].pie(Count_Products, frame=True)
        axs[0].scatter(Count_Products,agv_Price,color='Red' )
        axs[1].bar(Count_Products,agv_Price,color='Blue')
        axs[2].plot(Count_Products,agv_Price,color='Green')

        axs[0].legend((12,14), ('Count_Products', 'agv_Price'),bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0)
        axs[1].legend((12,14), ('Count_Products', 'agv_Price'), loc='upper right')
        axs[2].legend((12,14), ('Count_Products', 'agv_Price'), loc='upper right')

        #axs[3].hist(agv_Price,bins=8, linewidth=0.3,edgecolor="white")
        #fig1, ax1 = plt.subplots()

        #ax1.hist(agv_Price, bins=8, linewidth=0.5, edgecolor="white")

        fig.suptitle('Coun Of Products & agv Of Price')
        # Display
        plt.show()
        plt.draw()

def main():
    while True :
       DataCompany= CompanyBenchmarking("Datafurniture.xls")
       #DataCompany.DataDisplay()
       DataCompany.DataExport()
       #DataCompany.DataStatistic()
       #DataCompany.DataGraph()
       #DataCompany.DataInfo()
       restart = input('\nWould you like to restart? Enter yes.... or press any key to exit.\n')

       if restart.lower() != 'yes':
          break

if __name__ == "__main__":
    main()