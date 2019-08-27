# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:25:03 2018

@author: deadp
"""
#import re 
import time 
from bs4 import BeautifulSoup 
import urllib
html = urllib.urlopen('https://harassmap.org/en/reports?page=1').read()
#print html.text
soup = BeautifulSoup(html, 'html.parser')
start_time = time.time()
#table = soup.find('div' , id = 'report-table').find(class_ = 'table table-hover table-bordered table--bordered')
#alltrs = table.find('tbody').findAll('tr',class_='row-link')
#alllinks = table.find('tbody').findAll('tr',class_= 'row-link').get('data-href')
#print alltrs 
Date = []
Text =[]
Types =[] 
pagination_count= soup.find('div',class_='pagination--container mt-4').find('ul',class_='pagination')
listofpages =pagination_count.findAll('li')
numberofpages =int( listofpages[11].a.text)
print listofpages[11].a.text
#print len(pagination_count.findAll('li'))
#print pagination_count
for i in range(numberofpages):
    print "We ARE AT PAGE NUMBER" + str(i+1)
    html = urllib.urlopen('https://harassmap.org/en/reports?page='+str(i+1)).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div' , id = 'report-table').find(class_ = 'table table-hover table-bordered table--bordered')
    alltrs = table.find('tbody').findAll('tr',class_='row-link')

    for a in alltrs:
        date = a.td.text
        Date.append(date)
        link= a.get('data-href')
        print link
    #    print a.tr.td.text
    #for b in alllinks:
    #    link = table.find('tbody').find('tr',class_= 'row-link').get('data-href')
    #    print alllinks
        inpage = urllib.urlopen(link).read()
        soup1 = BeautifulSoup(inpage, 'html.parser')
        text=soup1.find('div',class_='site-content').find('div',class_='report-view').find('div',class_='container')
    #    #print text
        divs = text.findAll('div', attrs={'class':'row'})
        text = divs[2].find('div',class_='col-12 col-md-8').p.text
#        pattern = re.compile(r'\s+')
        text = text.strip()
        text =''.join(text.splitlines())
        print text
        Text.append(text)
    #    
    #    
        categories = soup1.find('div',class_= 'row mt-3 mb-4').find('div',class_='col-12 categories')
        listcategory= categories.findAll('span',class_='category mb-1')
        print len(listcategory)
        listoftypes=[]
        for i in range(len(listcategory)):
            listoftypes.append(listcategory[i].text)
        
        
        listoftypes = '/ '.join(listoftypes)
        print listoftypes 
        Types.append(listoftypes)
#        print Types
        
import pandas as pd 
test_df =pd.DataFrame({ 'Date': Date, 'Text':Text, 'Types':Types}) 
print test_df

test_df.to_csv('harassmap.csv',sep=",", encoding='utf-8', index=False)    
print("--- %s seconds ---" % (time.time() - start_time))

print 'end'