# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:04:42 2019

@author: 0706129
"""

import requests #匯入requests套件
from bs4 import BeautifulSoup
url='https://www.taiwanlottery.com.tw/fooder.asp'

html=requests.get(url) #取得程式碼內容
html.encoding='utf-8'
bs=BeautifulSoup(html.text, 'html.parser')
print('\n')
no1=bs.select('div') #取出class名稱為div串列
no2=no1[2].find('span',{'class':'font_black12'}) #<span>標籤class名稱為font_black12
print(no2.text) #印出text內容
a=no2.text
s=a.split('|') #分隔
print('\n')

import requests
from bs4 import BeautifulSoup
url='https://www.taiwanlottery.com.tw/index_new.aspx'
html=requests.get(url)
bs=BeautifulSoup(html.text, 'html.parser')

while(1):
    try: #例外處理
        choose=input('1.BINGO===BINGO  2.雙贏彩  3.威力彩  4.38樂合彩  5.大樂透\n6.49樂合彩  7.今彩539  8.39樂合彩  9.三星彩  10.4星彩  0.結束\n\n========欲查詢之樂透:')
        #選擇樂透項目,輸入0結束
        if(choose=='0'):
            break
        if(choose=='1'):
            #BINGO===BINGO
            print('BINGO===BINGO:')
            data1=bs.select('.contents_box01') #取出class名稱為.contents_box01串列
            data2=data1[0].find_all('div',{'class':'ball_tx'})  #球:所有<div>標籤class名稱為ball_tx
            print(data2) #印出
            print('-------------------')
            date1=bs.select('.contents_mine_tx01') 
            date2=date1[0].find('span',{'class':'font_black15'}) #抓出時間
            print(date2.text)
            print('開出獎號:',end='')
            for i in range(0,20):
                print(data2[i].text,end='   ') #依序印出
            sup=data1[0].find('div',{'class':'ball_red'})
            print('\n超級獎號:%s' %(sup.text))
            bism=data1[0].find('div',{'class':'ball_blue_BB1'})
            print('猜大小:%s' %(bism.text))
            oddo=data1[0].find('div',{'class':'ball_blue_BB2'})
            print('猜單雙:%s' %(oddo.text))
            print('\n')
            total=0 #中多少個號碼
            i_list={} #存輸入的值
            for a in range(0,20):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,20):
                for i in range(0,20):
                    if int(i_list[a])==int(data2[i].text): #比較輸入值和上方是否一樣==>中+1
                        total+=1
                        break
            tu=input('輸入你猜的超級特獎:') #存輸入超級特獎的值
            if int(tu)==int(sup.text):
                guess=input('輸入你猜的(大/小)&(單/雙):') #存輸入(大/小)&(單/雙)的值
                if(guess==oddo.text):
                    print('=========你中了%d個號碼,超級特獎以及(大/小)&(單/雙)'%total)
                else:
                    print('=========你中了%d個號碼以及超級特獎'%total)
            else:
                guess=input('輸入你猜的(大/小)&(單/雙):') 
                if(guess==oddo.text):
                    print('=========你中了%d個號碼以及(大/小)&(單/雙)'%total)
                else:
                    print('=========你中了%d個號碼'%total)
        if(choose=='2'):
            #雙贏彩
            print('雙贏彩資料:')
            data1=bs.select('.contents_box06') #取出class名稱為.contents_box06串列
            data2=data1[0].find_all('div',{'class':'ball_tx'}) #抓出所有的球
            print(data2)
            print('------------------------')
            date1=bs.select('.contents_mine_tx09') #抓時間
            date2=date1[0].find('span',{'class':'font_black15'})
            print(date2.text)
            print('開出順序:',end='')
            for i in range(0,12):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='') 
            for i in range(12,len(data2)): #大小排序
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,12):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1)) 
            for a in range(0,12):
                for i in range(0,12):
                    if int(i_list[a])==int(data2[i].text): #比較輸入值和上方是否一樣==>中+1
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='3'):
            #威力彩
            data1=bs.select('.contents_box02') #取出class名稱為.contents_box02串列,為串列的第一項
            data2=data1[0].find_all('div',{'class':'ball_tx'})
            print('威力彩綠球資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02') 
            date2=date1[0].find('span',{'class':'font_black15'}) #抓時間
            print(date2.text)
            print('目前頭獎預估金額：',end='')
            time1=bs.select('.top_dollar_tx')
            time2=time1[0].find('div',{'class':'top_dollar'}) #抓金額,為串列的第一項
            print(time2.text)
            print('開出順序:',end='')
            for i in range(0,6):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='')
            for i in range(6,len(data2)):
                print(data2[i].text,end='   ')    
            red=data1[0].find('div',{'class':'ball_red'}) #抓第二區的紅球號碼
            print('\n第二區:(紅球):%s' %(red.text))
            print('\n')
            total=0
            i_list={}
            for a in range(0,6):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,6):
                for i in range(0,6):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            spe=input('輸入你所選的第二區:')
            if int(spe)==int(red.text): #比較輸出的值是否跟上方相等
                print('=========你中了%d個號碼以及第二區'%total)
            else:
                print('=========你中了%d個號碼'%total)
        if(choose=='4'):
            #38樂合彩           
            data1=bs.select('.contents_box02') #取出class名稱為.contents_box02串列,為串列的第「二」項
            data2=data1[1].find_all('div',{'class':'ball_tx'})
            print('38樂合彩資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[1].find('span',{'class':'font_black15'})
            print(date2.text)
            print('開出順序:',end='')
            for i in range(0,6):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='')
            for i in range(6,len(data2)):
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,6):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,6):
                for i in range(0,6):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='5'):
            #大樂透
            data1=bs.select('.contents_box02') #取出class名稱為.contents_box02串列,為串列的第「三」項
            data2=data1[2].find_all('div',{'class':'ball_tx'})
            print('大樂透黃球資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[2].find('span',{'class':'font_black15'})
            print(date2.text)
            print('目前頭獎預估金額：',end='')
            time1=bs.select('.top_dollar_tx') #抓金額,為串列的第「二」項
            time2=time1[1].find('div',{'class':'top_dollar'})
            print(time2.text)
            print('開出順序:',end='')
            for i in range(0,6):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='')
            for i in range(6,len(data2)):
                print(data2[i].text,end='   ')
            red=data1[2].find('div',{'class':'ball_red'})
            print('\n特別號:(紅球):%s' %(red.text))
            print('\n')
            total=0
            i_list={}
            for a in range(0,6):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,6):
                for i in range(0,6):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            spa=input('輸入你所選的特別號')
            if int(spa)==int(red.text):
                print('=========你中了%d個號碼以及特別號:'%total)
            else:
                print('=========你中了%d個號碼'%total)
        if(choose=='6'):
            #49樂合彩
            data1=bs.select('.contents_box02') #取出class名稱為.contents_box02串列,為串列的第「四」項
            data2=data1[3].find_all('div',{'class':'ball_tx'}) 
            print('49樂合彩資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[3].find('span',{'class':'font_black15'})
            print(date2.text)
            print('開出順序:',end='')
            for i in range(0,6):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='')
            for i in range(6,len(data2)):
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,6):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,6):
                for i in range(0,6):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='7'):
            #今彩539
            data1=bs.select('.contents_box03') #取出class名稱為.contents_box03串列,為串列的第一項
            data2=data1[0].find_all('div',{'class':'ball_tx'})
            print('今彩539資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[4].find('span',{'class':'font_black15'})
            print(date2.text)
            print('開出順序:',end='')
            for i in range(0,5):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='') 
            for i in range(5,len(data2)): #大小排序
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,5):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,5):
                for i in range(0,5):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='8'):
            #39樂合彩
            data1=bs.select('.contents_box03') #取出class名稱為.contents_box03串列,為串列的第「二」項
            data2=data1[1].find_all('div',{'class':'ball_tx'})
            print('39樂合彩資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02') #抓時間
            date2=date1[5].find('span',{'class':'font_black15'})
            print(date2.text)
            print('開出順序:',end='')
            for i in range(0,5):
                print(data2[i].text,end='   ')
            print('\n大小順序:',end='')
            for i in range(5,len(data2)):
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,5):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,5):
                for i in range(0,5):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='9'):
            #三星彩
            data1=bs.select('.contents_box04') #取出class名稱為.contents_box04串列,為串列的第一項
            data2=data1[0].find_all('div',{'class':'ball_tx'}) #取出全部球
            print('三星彩資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[6].find('span',{'class':'font_black15'})
            print(date2.text)
            print('中獎號碼:',end='')
            for i in range(0,3):
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,3):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,3):
                for i in range(0,3):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
        if(choose=='10'):
            #四星彩
            data1=bs.select('.contents_box04') #取出class名稱為.contents_box04串列,為串列的第「二」項
            data2=data1[1].find_all('div',{'class':'ball_tx'})
            print('四星彩資料:')
            print(data2)
            print('-------------------')
            date1=bs.select('.contents_mine_tx02')
            date2=date1[7].find('span',{'class':'font_black15'})
            print(date2.text)
            print('中獎號碼:',end='')
            for i in range(0,4):
                print(data2[i].text,end='   ')
            print('\n')
            total=0
            i_list={}
            for a in range(0,4):
                i_list[a]=input('輸入你所選的第%d個號碼:'%(a+1))
            for a in range(0,4):
                for i in range(0,4):
                    if int(i_list[a])==int(data2[i].text):
                        total+=1
                        break
            print('=========你中了%d個號碼'%total)
    except: 
        break #例外發生時執行的程式







  


