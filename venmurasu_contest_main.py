from tamil import utf8,numeral
num=int(input("Enter the number of words to be displayed:")) #input prompt
 
if(num<=12000):
    f=open(r"venmurasu_tamil_word_file_13.txt",'r',encoding='utf8') #this file makes the sorting even faster
else:
    f=open(r"venmurasu_tamil_word_file_complete.txt",'r',encoding='utf8')
    
tamil_list=f.read().split(',') #reading from file and splitting based on comma
f.close()  
word_list=dict() #creating a dictionary
for val in tamil_list:
    letters = utf8.get_letters(val) #encoding to get correct tamil letters
    length = len(letters) #finding the length of letters
    if length!=0:
        key=length
        word_list.setdefault(length,[])
        word_list[length].append(val)#appending the word as value into a list inside a dictionary with length as key
count=num
file=open("sorted_words_file.txt",'a',encoding='utf8') #the sorted words will be appended in this file
i=1
for key in sorted(word_list,reverse=True): #sorting the keys of the dictionary and running a loop
    length=len(word_list[key])
    if count>0:
        print(numeral.num2tamilstr(key),u'எழுத்துக்கள்  :   ' ,key,'\n',i,':  ',end='')
        print(*word_list[key][:count],sep = '\n',end='\n\n') #printing list inside the dictionary
        i+=length
        file.write(str(key))
        file.write(str(word_list[key][:count])[1:-1]) #writing into a file
        count=count-length
        file.write(',')           
file.close()
#Time complexity based on algorithm : O(n) where n is the number of words in the file which is opened to read tamil words