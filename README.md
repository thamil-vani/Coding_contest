# Venmurasu_Coding_Contest
Top 10 longest words in the venmurasu novel

# Prerequisites and Recommendations:
Programming Language :  Python 

Preferred OS         :  Windows

Preferred IDE        :  Anaconda

# Libraries needed to install:
Refer requirements.txt file

tkinter          -   for interactive GUI

PIL              -   for background images and icons

datetime         -   used in GUI

Open-Tamil       -   for processing Tamil Words

gtts             -   google text to speech (for pronouncing tamil words)

playsound        -   for playing audio file

BeautifulSoup    -   for scraping websites

ssl              -   for secure connection

urllib           -   for sending requests

# Running the code:

There are totally five python files which are uploaded.

1.user_defined_library_package.py     ---> 	No need to run this file. This script is an user defined library we included for our project.

2.web scraping and extraction.py        ---> 	This script is for scraping the url and the contents from the website.
		        	To avoid scraping everytime we run the project, the scraped contents are stored in a file.
				
     Blog contents     ---> 	blogs/1937 scraped files ---> Download it from the google drive link
     URLs              ---> 	venmurasu_blog_url_list.txt file

	Since the contents are stored in a file, there is no need to run this script.

3.filtering_tamil_words.py  ---> 	It opens each file stored under blogs folder and creates a new file with only tamil words(comma separated).

     Tamil words file  --->	venmurasu_tamil_word_file_complete.txt ---> Download it from the google drive link ( contains all tamil words ) 
				venmurasu_tamil_word_file_13.txt       ( contains tamil words with length >= 13)

	Since the contents are stored in a file, there is no need to run this script.

4.venmurasu_contest_main.py --->	This is the main code of the project. It takes words from the file and based on their length it appends the words in a dictionary.
				The length of the word will be the key and words will be appended in a list inside a dictionary which is the value. This makes the sorting faster. 
				While running this project, it asks for the number of words to be displayed. The input is not limited to 10,one can view as many words as he wants.
				The output is printed in the output console and is also stored in a file.

 sorted_words_file.txt --->	Stores the sorted words along with their length.

5.venmurasu_added_features.py     --->	This script contains all the additional features that we have added for this project.
				
				1. Interactive GUI using tkinter.
				2. Text to speech option which pronounces tamil words. (Requires Internet Connection) 
				3. Classification of letters (displays the number of uyir,mei,uyirmei,ayutha,sanskrit,vallinam,mellinam and idaiyinam letters in a word)
 


# Contributors:

1. Thamil Vani .S (CSE) 
2. Aishwarya Lakshmi .B (IT)
3. Narmatha .R (CSE)

# License:

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
