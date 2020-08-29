from bs4 import BeautifulSoup
from tamil import utf8

def tamil_words(count):
        f=open("blogs/venmurasu_blog_{}.txt".format(count),'rb') #opening files which have blog contents
        html = f.read()
        soup = BeautifulSoup(html, "html.parser") #parsing the contents
        
        for anchor in soup('a'): #removing the anchor tags
            anchor.decompose()
            
        for strong in soup('strong'): #removing the strong tag(which is usually title)
            strong.decompose()
        
        word = soup.find_all('p') #finding the novel contents
                
        word_list = []
        for i in range(len(word)):
            w=word[i].get_text()
            a=w.split(" ")       #splitting the contents based on space and storing it in a list
            word_list.extend(a)
            
        temp_list_1=[]    
        for val in word_list:
            a=utf8.has_tamil(val) #Only those words which have tamil letters are added to this list..english letters are eliminated
            if a:
                temp_list_1.append(val)
                
        temp_list_2=[]
        for line in temp_list_1:
            #Removing special characters
            line=line.replace("!","\n").replace(".","\n").replace("?","\n").replace(";","\n").replace(":","\n").replace(",","\n").replace("“","\n").replace("”","\n").replace("‘","\n").replace("’","\n").replace("…","\n").replace("===========================================================","\n").replace("\xa0",'\n')                                     
            temp_list_2.append(line)
                
        tamil_list=[]
        for val in temp_list_2:
            val=val.split("\n")         #Splitting based on new line and storing in a new list
            tamil_list.extend(val)
        #avoid_list contains words which need not be included for sorting as they are not a part of novel but is present in the list    
        avoid_list=[u'பின்னூட்டங்கள்', u'மூடப்பட்டுள்ளது', u'உங்கள்', u'மின்னஞ்சல்', u'இங்கே', u'கொடுத்து', u'அதன்', u'வழி', u'பதிவுகளைப்', u'பெறவும்', u'பின்', u'தொடர']
            
        file=open("venmurasu_tamil_word_file_13.txt",'a',encoding='utf8') 
        #words with length>=13 are stored in the above file for faster sorting
        #all words with length>0 are stored in venmurasu_tamil_word_file_complete.txt
        for val in tamil_list:
            if val is not '' :
              if val not in avoid_list:
                  letters = utf8.get_letters(val) #encoding to get correct letters
                  length = len(letters) #finding the length of the word
                  if length>=13:   #length>0 is stored in venmurasu_tamil_word_file_complete.txt
                      file.write(val)
                      file.write(',') #writing the words into the file (comma separated)
        file.close()
             
for count in range(1937): #1937 files
    tamil_words(count) 