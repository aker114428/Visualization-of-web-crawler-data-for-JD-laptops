from selenium import webdriver
import time
import pymongo
import random
import os,sys
from bson import json_util
#对云数据库的连接
client = pymongo.MongoClient("mongodb+srv://bigData-test:xKl0BOD0oQl3egAp@cluster0.nbnp7oi.mongodb.net/?retryWrites=true&w=majority")
dbname = client['db']
collection_name = dbname['BigData-test']
print(dbname.list_collection_names())
#初始页面，设置为商品的第一页
urls = ["https://search.jd.com/Search?keyword=%E8%BD%BB%E8%96%84%E6%9C%AC&wq=%E8%BD%BB%E8%96%84%E6%9C%AC&pvid=1d8b9cbbec1d466d8050a75a986e93ea&page=1&s=56&click=0"]
next_page_num = 1
chrome_driver = webdriver.Chrome()
chrome_driver.get(urls[-1])
chrome_driver.implicitly_wait(10)
time.sleep(1)
#对商品链接的爬取
while next_page_num <= 200:
    cur_page = urls[-1].split('&page=')[1]
    cur_page_num = cur_page[0:len(cur_page.split('&')[0])]
    next_page = cur_page.replace(cur_page_num,str(int(cur_page_num)+2),1)
    next_page_num = int(next_page.split('&')[0])
    js="var q=document.documentElement.scrollTop=10000"
    chrome_driver.execute_script(js)
    time.sleep(5)
    goods_list = chrome_driver.find_elements("css selector",'.goods-list-v2 .gl-item .p-img a')
    filename = "jd_goods_list_thinBook.html"
    with open(filename,'a+',encoding='utf-8')as f:
        for good in goods_list:
            f.write(str(good.get_attribute('href'))+'\n')
    next_url = urls[-1][:-len(str(cur_page))] + str(next_page)
    urls.append(next_url)
    chrome_driver.get(next_url)
    chrome_driver.implicitly_wait(10)
    print("link is:" + urls[-1])
    print("current page: "+next_page)
    time.sleep(5)

#对于游戏本信息的爬取及处理
os.chdir(sys.path[0])
with open('jd_goods_list_gameBook.html','r',encoding='utf-8')as f:
    with open("BigData_gameBook.json",'a+',encoding='utf-8') as f2:
        url_list = f.readlines()
        upload_list = []
        count = 0
        for next_url in url_list:
            if(count>=4460):
                time.sleep(random.randint(3,5))
                chrome_driver.implicitly_wait(10)
                chrome_driver.get(next_url)
                js="var q=document.documentElement.scrollTop=10000"
                chrome_driver.execute_script(js)
                chrome_driver.implicitly_wait(10)
                time.sleep(random.randint(5,10))
                good_imformation = chrome_driver.find_elements("class name",'Ptable-item')
                good_information_dict = dict()
                for i in good_imformation:
                    new_dict = dict()
                    #print(i.find_element("tag name",'h3').is_displayed())
                    main_title = i.find_element("tag name",'h3').get_attribute('innerText')
                    new_dict[main_title] = dict()
                    main_content = i.find_elements("class name",'clearfix')
                    for j in main_content:
                        sub_title = j.find_element("tag name",'dt').get_attribute('innerText')
                        sub_content = j.find_elements("tag name",'dd')[-1].get_attribute('innerText')
                        new_dict[main_title][sub_title] = sub_content
                    good_information_dict.update(new_dict)
                f2.write(json_util.dumps(good_information_dict, indent=4, ensure_ascii=False))
                #upload_list.append(good_information_dict)
                count = count + 1
                print("gameBook:"+str(count))
                if len(upload_list)>=5:
                    print("upload")
                    #collection_name.insert_many(upload_list)
                    upload_list.clear()
                    time.sleep(10)
                if (count/10)%1 == 0:
                    print("long time sleep")
                    time.sleep(60)
            
            else:
                count = count + 1
                print("gameBookskip: "+str(count))
            if(count == 4460):
                print("configuration time 30s")
                time.sleep(30)
#对于轻薄本信息的爬取及处理
with open('jd_goods_list_thinBook.html','r',encoding='utf-8')as f:
    with open("BigData_thinBookbbb.json","a+",encoding='utf-8') as f2:
        url_list = f.readlines()
        upload_list = []
        count = 0
        for next_url in url_list:
            if(count>=1753):
                time.sleep(random.randint(3,5))
                chrome_driver.implicitly_wait(10)
                chrome_driver.get(next_url)
                js="var q=document.documentElement.scrollTop=10000"
                chrome_driver.execute_script(js)
                chrome_driver.implicitly_wait(10)
                time.sleep(random.randint(5,10))
                good_imformation = chrome_driver.find_elements("class name",'Ptable-item')
                good_information_dict = dict()
                for i in good_imformation:
                    new_dict = dict()
                    #print(i.find_element("tag name",'h3').is_displayed())
                    main_title = i.find_element("tag name",'h3').get_attribute('innerText')
                    new_dict[main_title] = dict()
                    main_content = i.find_elements("class name",'clearfix')
                    for j in main_content:
                        sub_title = j.find_element("tag name",'dt').get_attribute('innerText')
                        sub_content = j.find_elements("tag name",'dd')[-1].get_attribute('innerText')
                        new_dict[main_title][sub_title] = sub_content
                    good_information_dict.update(new_dict)
                f2.write(json_util.dumps(good_information_dict, indent=4, ensure_ascii=False))
                #upload_list.append(good_information_dict)
                count = count + 1
                print("url:"+next_url)
                print("thinBook:"+str(count))
                if len(upload_list)>=5:
                    print("thinBook upload")
                    #collection_name.insert_many(upload_list)
                    upload_list.clear()  
                    time.sleep(10)
                if (count/10)%1 == 0:
                    print("long time sleep")
                    time.sleep(30)
            
            else:
                count = count + 1
                print("thinBookskip: "+str(count)) 
            

            


