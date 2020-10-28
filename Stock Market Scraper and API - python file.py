#!/usr/bin/env python
# coding: utf-8

# # Visual Analytics - Assignment 2 - Andrea Armani

# ## Disclaimer

# Data are scraped from Wikipedia website at https://en.wikipedia.org/wiki/List_of_S%26P_500_companies .
# According to the Terms and Conditions applied to such website, scraping data for academic purposes is allowed. 

# ## Introduction to the research

# Covid pandemic massively affected the financial stock markets around the world. In the following, I collected about the fluctuations of the **S&P 500** companies, the most important companies in the american stock market. For the sake of simplicity such collection is limited to the US market, however using the same code is possible to retrieve data about companies listed in different stock markets around the world. 
# Other lists that contain the most important companies in different world's region could be find at:<br>
# <br>
# https://en.wikipedia.org/wiki/S%26P/ASX_50 (Australia)<br>
# https://en.wikipedia.org/wiki/S%26P_Asia_50 (Asia)<br>
# https://en.wikipedia.org/wiki/S%26P/TSX_60 (Canada)<br>
# https://en.wikipedia.org/wiki/S%26P_Latin_America_40 (South America)<br>
# <br>
# As for the european markets the S&P listed 350 companies, however there is no available scraping list from which data can be retrieved without infringe Terms and Conditions of websites. 

# ## Utility

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import os.path
from os import path
import requests
import unidecode
import yfinance as yf
from datetime import datetime


# ## Raw Data Folder 

# In this folder there will be the Wikipedia page

# In[57]:


# Folder creation
directory_scraped = "scraped_companies_data"

if not path.isdir(directory_scraped):
    os.mkdir(directory_scraped)


# ## API Data Folder

# This folder will contain the data retrieved through API

# In[56]:


# Folder creation
directory_api_files = "api_history_sep_companies"

if not path.isdir(directory_api_files):
    os.mkdir(directory_api_files)


# ## Scraping function

# In[52]:


# Retrieve an S&P pages in wikipedia
def fetch_sep_lists(root,page_name,directory):
    full_url = root + page_name
    
    true_name = page_name.replace("/",'_')
    #the  name of the file to save to
    file_name = directory+"/"+true_name+".html"
    
    
    page = requests.get(full_url, allow_redirects=True)
    
    
    if not page.status_code == 200:
        return "Some errors occured!"
    else:
        open(file_name, 'wb').write(page.content)


# ## Extracting Function

# It accesses the scraped page and returns a list of tickers.<br>
# Such stickers can be find in the table 'constituents'

# In[53]:


def extract_ticker_sep_america(file_name):
    
    tickers = []
    
    with open(file_name, encoding='utf-8') as fp:
        soup = bs(fp, 'html.parser')
   
    # Select the table with id = constituents
    table = soup.find(id = "constituents")
    
    # Within the tbody
    tbody = table.find('tbody')
    
    # Collect the link of every company
    rows = tbody.findAll('tr')
    rows.pop(0)
    for row in rows:
        #print(row)
        td = row.find('td')
        tickers.append(unidecode.unidecode(td.text.strip()))
    
    return tickers


# In[49]:


# Fetch the S&P page in Wikipedia that contains a list of companies in the Stock Market
root_page = 'https://en.wikipedia.org/wiki/'

american_sep = fetch_sep_lists(root_page,'List_of_S%26P_500_companies',directory_scraped)


# In[58]:


tickers = extract_ticker_sep_america(directory_scraped + '/' + 'List_of_S%26P_500_companies' + '.html')


# In[83]:


d = pd.DataFrame(tickers, columns=['id'])
d.to_csv('american_tickers.csv',index = False)


# After further analysis, yfinance is not capable to handle tickers that contains special characters. Although it's not the case for the american S&P, I tested the API with tickers from different regions that present such problem and it returned an error. 

# In[31]:


final_tickers =[]
for t in tickers:
    if t.isalpha():
        final_tickers.append(t)


# ## Stock Market Historical Data Saving

# For every ticker, it retrieves information about the floating of the market in every specific day from **2019-09-01** up to **2020-09-07**, along with the sector in which the company operates. Finally, it stores such informations in a file

# In[44]:


for ticker in range(208,len(final_tickers)):
    t = yf.Ticker(final_tickers[ticker])
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    if 'sector' in t.info:
        t_historical['sector'] = t.info['sector']
    else:
        t_historical['sector'] = ''
    name = t.info['longName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    t_historical.to_csv(directory_api_files + '/' + "2019-09-01_2020-09-07_" + alphanumeric + '.csv')


# In[44]:


import os
for filename in os.listdir(directory_api_files):
    x = pd.read_csv(directory_api_files + '/' + filename)
    x['Avg'] = (x['Low'] + x['High'])/2
    x.to_csv(directory_api_files + '/' + filename)


# In[60]:


x = pd.read_csv('china indexes.csv')


# In[62]:


l = list(x.id)


# In[45]:


# Folder creation
directory_api_files = "api_history_sep_companies_china"

if not path.isdir(directory_api_files):
    os.mkdir(directory_api_files)


# In[80]:


for ticker in l:
    t = yf.Ticker(ticker)
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    if 'sector' in t.info:
        t_historical['sector'] = t.info['sector']
    else:
        t_historical['sector'] = ''
    t_historical['country'] = t.info['country']
    name = t.info['longName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    for i,row in t_historical.iterrows():
        if row['country'] == 'China' or row['country'] == 'Macau':
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/7.75
            t_historical.at[i,'High'] = t_historical.at[i,'High']/7.75
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/7.75
        elif row['country'] == 'Taiwan':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/28.62
            t_historical.at[i,'High'] = t_historical.at[i,'High']/28.62
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/28.62
        elif row['country'] == 'Singapore':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/1.36
            t_historical.at[i,'High'] = t_historical.at[i,'High']/1.36
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/1.36
        elif row['country'] == 'South Korea':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/148.22
            t_historical.at[i,'High'] = t_historical.at[i,'High']/148.22
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/148.22
    t_historical.to_csv(directory_api_files + '/' + "2019-09-01_2020-09-07_" + alphanumeric + '.csv')


# In[46]:


import os
for filename in os.listdir(directory_api_files):
    x = pd.read_csv(directory_api_files + '/' + filename)
    x['Avg'] = (x['Low'] + x['High'])/2
    x.to_csv(directory_api_files + '/' + filename)


# In[73]:


x = pd.read_csv('european indexes.csv')


# In[74]:


l = list(x.id)


# In[41]:


# Folder creation
directory_api_files = "api_history_sep_companies_europe"

if not path.isdir(directory_api_files):
    os.mkdir(directory_api_files)


# In[78]:


for ticker in l:
    t = yf.Ticker(ticker)
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    if 'sector' in t.info:
        t_historical['sector'] = t.info['sector']
    else:
        t_historical['sector'] = ''
    t_historical['country'] = t.info['country']
    name = t.info['longName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    for i,row in t_historical.iterrows():
        t_historical.at[i,'Close'] = t_historical.at[i,'Close']/0.85
        t_historical.at[i,'High'] = t_historical.at[i,'High']/0.85
        t_historical.at[i,'Open'] = t_historical.at[i,'Open']/0.85
    t_historical.to_csv(directory_api_files + '/' + "2019-09-01_2020-09-07_" + alphanumeric + '.csv')


# In[42]:


import os
for filename in os.listdir(directory_api_files):
    x = pd.read_csv(directory_api_files + '/' + filename)
    x['Avg'] = (x['Low'] + x['High'])/2
    x.to_csv(directory_api_files + '/' + filename)


# In[2]:


# Folder creation
directory_api_files = "api_history_sep_companies_overall_indices"

if not path.isdir(directory_api_files):
    os.mkdir(directory_api_files)


# In[13]:


df = pd.DataFrame()


# In[29]:


for ticker in l:
    t = yf.Ticker(ticker)
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    name = t.info['shortName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    t_historical.to_csv(directory_api_files + '/' + "2019-09-01_2020-09-07_" + alphanumeric + '.csv')


# # Merged Europe + China + USA

# In[68]:


# Folder creation
directory_api_files = "api_history_sep_companies_merged_indexes"

if not path.isdir(directory_api_files):
    os.mkdir(directory_api_files)


# In[4]:


x = pd.read_csv('european indexes.csv')


# In[5]:


l = list(x.id)


# In[6]:


df = pd.DataFrame()


# ## Europe, China

# In[7]:


for ticker in l:
    t = yf.Ticker(ticker)
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    t_historical.drop(columns = ['Dividends','Stock Splits'],inplace = True)
    if 'sector' in t.info:
        t_historical['Sector'] = t.info['sector']
    else:
        t_historical['Sector'] = ''
    t_historical['Country'] = t.info['country']
    t_historical['Company'] = t.info['longName']
    name = t.info['longName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    for i,row in t_historical.iterrows():
        if row['Country'] == 'China' or row['Country'] == 'Macau':
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/7.75
            t_historical.at[i,'High'] = t_historical.at[i,'High']/7.75
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/7.75
        elif row['Country'] == 'Taiwan':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/28.62
            t_historical.at[i,'High'] = t_historical.at[i,'High']/28.62
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/28.62
        elif row['Country'] == 'Singapore':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/1.36
            t_historical.at[i,'High'] = t_historical.at[i,'High']/1.36
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/1.36
        elif row['Country'] == 'South Korea':
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/148.22
            t_historical.at[i,'High'] = t_historical.at[i,'High']/148.22
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/148.22
        else:
            t_historical.at[i,'Close'] = t_historical.at[i,'Close']/0.85
            t_historical.at[i,'High'] = t_historical.at[i,'High']/0.85
            t_historical.at[i,'Open'] = t_historical.at[i,'Open']/0.85
    df = df.append(t_historical)


# In[12]:


df.reset_index(level = 0, inplace = True)


# In[46]:


df.to_csv(directory_api_files+'/companies_europe_asia.csv',index = False)


# ## USA

# In[13]:


x = pd.read_csv('american_tickers.csv')
l = list(x.id)


# In[139]:


df = pd.read_csv(directory_api_files+'/companies_europe_asia.csv')


# In[17]:


df1 = pd.DataFrame()


# In[18]:


for ticker in l:
    t = yf.Ticker(ticker)
    t_historical = t.history(start="2019-09-01", end="2020-09-07", interval="1d")
    t_historical.drop(columns = ['Dividends','Stock Splits'],inplace = True)
    if 'sector' in t.info:
        t_historical['Sector'] = t.info['sector']
    else:
        t_historical['Sector'] = ''
    t_historical['Country'] = t.info['country']
    t_historical['Company'] = t.info['longName']
    name = t.info['longName']
    alphanumeric = ''
    if name.isalpha() == False:
        for character in name:
            if character.isalnum():
                alphanumeric += character
    df1 = df1.append(t_historical)

df1.reset_index(level = 0, inplace = True)


# In[23]:


df_final = df.append(df1)


# In[25]:


df_final.to_csv(directory_api_files + "/companies_stock_price_worldwide.csv",index = False)


# In[8]:


l = ['^GSPC']


# In[7]:


df_comp = pd.DataFrame()


# In[179]:


a = yf.Ticker('^GSPC').history(start="2019-09-01", end="2020-09-07", interval="1d")

a['Index'] = 'S&P 500'


a.drop(['Dividends','Stock Splits'],axis = 1,inplace = True)


# In[180]:


b = pd.read_csv('api_history_sep_companies_overall_indices/Euro Stoxx 50 Historical Data.csv')

b['Index'] = 'STOXX 50 EU'

b.rename(inplace = True, columns = {'Price':'Close'})


# In[181]:


c = yf.Ticker('^HSI').history(start="2019-09-01", end="2020-09-07", interval="1d")

c['Index'] = 'Hang Sang'

c.reset_index(level = 0, inplace = True)

c.drop(['Dividends','Stock Splits'],axis = 1,inplace = True)

c['High'] = c['High'] * 0.13
c['Open'] = c['Open'] * 0.13
c['Low'] = c['Low'] * 0.13
c['Close'] = c['Close'] * 0.13


# In[182]:


for i,r in b.iterrows():
    a_p =datetime.strptime(r['Date'], '%b %d, %Y')
    a_p = a_p.strftime('%Y-%m-%d %H:%M:%S')
    vol = r['Vol.']
    vol = vol.replace('M','')
    vol = vol.replace('-','0')
    vol = float(vol)
    vol = vol*1.17
    vol = int(vol * 1000000)
    high = r['High']
    high = high.replace(',','')
    high = float(high)
    high = high*1.17
    low = r['Low']
    low = low.replace(',','')
    low = float(low)
    low = low*1.17
    opn = r['Open']
    opn = opn.replace(',','')
    opn = float(opn)
    opn = opn*1.17
    close = r['Close']
    close = close.replace(',','')
    close = float(close)
    df = pd.DataFrame([[ a_p,opn,high,low,close,vol,r['Index'] ]] ,
                      columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Index'])
    a = a.append(df)


# In[183]:


a = a.append(c)


# In[185]:


a['Avg'] = (a['High'] + a['Low'])/2


# In[187]:


a.to_csv('api_history_sep_companies_overall_indices/compounded_indexes.csv',index = False)


# In[28]:


resp = pd.DataFrame(columns=['Name','Diff'])


# In[32]:


df_final['Avg'] = (df_final['High'] + df_final['Low'])/2


# In[36]:


temp = df_final.loc[df_final['Date'].isin(['2019-09-06','2020-08-31'])]


# In[59]:


li = []
for i,r in temp.iterrows():
    if i == 0:
        continue
    if temp.iloc[i-1,9] == temp.iloc[i-1,9]:
        li.append([temp.iloc[i,10] / temp.iloc[i-1,10],temp.iloc[i,9]])


# In[60]:


li.sort(reverse = True)


# In[28]:


avges = pd.DataFrame()


# In[82]:


x_za = yf.Ticker('ZAL.DE')
x_historical = x_za.history(start="2019-09-01", end="2020-09-07", interval="1d")

avg_za = (x_historical.High + x_historical.Low)/2

x_eb = yf.Ticker('EBAY')
x_historical = x_eb.history(start="2019-09-01", end="2020-09-07", interval="1d")

avg_eb = (x_historical.High + x_historical.Low)/2

x_am = yf.Ticker('AMZN')
x_historical = x_am.history(start="2019-09-01", end="2020-09-07", interval="1d")

avg_am = (x_historical.High + x_historical.Low)/2

x_ba = yf.Ticker('BABA')
x_historical = x_ba.history(start="2019-09-01", end="2020-09-07", interval="1d")

avg_ba = (x_historical.High + x_historical.Low)/2

x_as = yf.Ticker('ASC.L')
x_historical = x_as.history(start="2019-09-01", end="2020-09-07", interval="1d")

avg_as = (x_historical.High + x_historical.Low)/2

avges['Zalando'] = avg_za

avges['Ebay'] = avg_eb

avges['Asos'] = avg_as

avges['Alibaba'] = avg_ba

avges['Amazon'] = avg_am

normalized_avges=(avges-avges.min())/(avges.max()-avges.min())

normalized_avges.reset_index(level = 0, inplace = True)

normalized_avges.rename(columns = {'index':'Date'},inplace = True)

normalized_avges.fillna(0,inplace = True)

normalized_avges.to_csv(directory_api_files + '/' + 'ecommerce_normalized_companies.csv',index = False)

