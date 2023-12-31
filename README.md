
# Data Extraction and NLP using Python


## How I approached the Solution:
In this project, I delved into the exploration of Data Extraction and Natural Language Processing using Python .

Upon a thorough examination of the objectives, I implemented the task in the following steps:

#### Working with the URLs

- The list of URLs provided was saved into a python file urls.py
 
####	Performing web scraping

- The extraction of data from the given URLs in the form of text was done by scrapper.py, created specifically to work with the title and text content. The process was executed using the ‘BeautifulSoup’ library in Python.
- The extracted data was henceforth, stored in the dataset folder in a sequential manner in the form of individual text files named as blackassign0001.txt…… blackassign0100.txt

####	Filtration of extracted data

- This process was formulated in the analysis.py file. Using the files from the dataset, the extracted data was split into tokens. The stopwords were filtered from these tokens. 

####	Performing sentimental analysis

- In the implementation of Natural Language Processing, the MasterDictionary folder was used. In this, the positive and negative words were segregated into separate text files. The availability of these words in my extracted data was checked and analyzed in accordance with the required variables in analysis.py .
- The result of all the variables was calculated henceforth.




       1.	POSITIVE SCORE
       2.	NEGATIVE SCORE
       3.	POLARITY SCORE
       4.	SUBJECTIVITY SCORE
       5.	AVG SENTENCE LENGTH
       6.	PERCENTAGE OF COMPLEX WORDS
       7.	FOG INDEX
       8.	AVG NUMBER OF WORDS PER SENTENCE
       9.  COMPLEX WORD COUNT
       10. WORD COUNT
       11. SYLLABLE PER WORD
       12. PERSONAL PRONOUNS
       13. AVG WORD LENGTH

####	The final output

- The output is displayed in a spreadsheet with the name as output.xlsx file. The Screenshot for the given output.xlsx is given below.


![App Screenshot](https://resumezcaler.blob.core.windows.net/sahilresume/excel.png)

## How To Run the .py file to generate the Output: -
 Step1- Install all the dependencies that have been mentioned in the next pages.

 Step2- Install all the required folder for the data analysis from the google drive   Test Assignment folder i.e. MasterDictionary and StopWords. 

Step3- Save all the python files in the same folder i.e. Scrapper.py, urls.py and  
            analysis.py and make sure all these python scripts and above folder are 
            stored in same place

Step4- As the URL’s are already saved in the urls.py file you just have to open the 
            Scrapper.py file.

Step5- After, Opening the Scrapper.py file make sure to import urls from urls.py 
            file.

Step6- When the scrapper.py file would have been interpreted it would result in the 
            creation of 100 text files so make sure to create an folder named “dataset”
            in the same folder as scrapper.py

Step7- Now, Open the analysis.py file and make sure all the paths attached to the 
            file are in correct format this file will run the analysis on all the 100 text 
            files that have been created by scrapper.py

Step8- Create an folder named Excel in the same folder as all other files 

Step9- After the analysis.py has finished its work the excel file would be generated 
            in the folder named Excel this Excel file would contain all the Output 
            variables that were required by given data


## All the Dependencies required for the Python Scripts are: - 
#### Python Standard Library:
- os: Operating system interfaces.
- string: String manipulation operations.
- nltk: Natural Language Toolkit. Used for tokenization and other natural language processing tasks.
- pyphen: Used for hyphenation.
- re: Regular expression operations.
- pandas: Data manipulation library.
- openpyxl: Module for reading/writing Excel files (used by Pandas).

#### External Files/Modules:
- urls: A custom module or file named urls is referenced. This module likely contains a list or data structure named urls that is used in the code. Make sure this file is available.

#### External Data Files:
- The code assumes the existence of certain folders like 'StopWords-20231230T095444Z-001/' and 'MasterDictionary-20231230T095444Z-001/'. Ensure that these folders and their contents are present or adjust the paths accordingly.

#### External Excel Writer Engine: 
- The code uses the xlsxwriter engine for writing Excel files with Pandas. If not already installed, you may need to install it using:

        pip install XlsxWriter

#### Note: 
Ensure that the NLTK data is downloaded by uncommenting the following lines:

      nltk.download('punkt')  # Download the punkt tokenizer data
      nltk.download('words')  # Download the words corpus
To install the required Python packages, you can use the following command:

       pip install nltk pyphen pandas openpyxl XlsxWriter

