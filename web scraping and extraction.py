#importing necessary libraries
import ssl
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

#establishing a secure connection
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

file=open("venmurasu_blog_url_list.txt",'w') #this file will contain all the urls
def scraping(url,count):
        file2=open("blogs/venmurasu_blog_{}.txt".format(count),'wb') #this file will have all the blog contents
        f = urlopen(url, context=CTX).read() #reading the website contents
        file2.write(f) #writing blog contents into the file
        file2.close() 
        soup=bs(f,'html.parser') #parsing the contents
        try:
            url=soup.find(class_='nav-next')  #finding the next URL
            next_url=url.find('a').attrs['href']
        except:
            return None
        else:        
            if next_url:
                file.write(str(next_url)) #writing urls into the file
                file.write('\n')
            return next_url                    
count=0
#url of first blog.The subsequent urls are scraped and stored in a file
url="https://venmurasu.in/2014/01/01/%E0%AE%B5%E0%AF%86%E0%AE%A3%E0%AF%8D%E0%AE%AE%E0%AF%81%E0%AE%B0%E0%AE%9A%E0%AF%81-%E0%AE%A8%E0%AF%82%E0%AE%B2%E0%AF%8D-%E0%AE%92%E0%AE%A9%E0%AF%8D%E0%AE%B1%E0%AF%81/"
file.write(str(url))
file.write('\n')
while True:
    url=scraping(url,count) #calls the scraping function which returns the next url
    count=count+1 
    if url is None:
        break      
file.close()