###### Made by Tomas Pasiecznik

# Text Mining Project
In this project, I conducted text mining using RapidMiner on data collected by a focused web crawler I created with Python. While doing this project, I also developed a frequency-based indexer and a position-based indexer that utilized Beautiful Soup and NLTK.

# Focused Web Crawler | Information
The web crawler I created takes Wikipedia links about a particular topic chosen by the
user as seed URLs. In addition to this, it takes terms related to the topic for adding better context
to the crawler. I made the web crawler use both a page limit and a location on the hard drive set
by the user to store the output of the program in a folder called “crawler_output”.
  
 The crawler itself takes the seed URLs and terms that are passed in and begins by putting
the seed URLs into a queue. Various functions are then defined and used for queue traversal
inside a while loop. The crawler takes the first seed URL from the queue and uses BeautifulSoup
to get the page content, a function was created for this. The main text and title are cleaned and
analyzed for relevance. If a page’s main text contains 2 or more of the relevant terms, the visited
page’s title and URL will be saved into lists, and an HTML file will be output with the HTML
code of that URL. The reason for saving both the title and the URL into lists is because some
URLs contained the same title, so the program will check both lists when deciding if a URL has
already been crawled. All HTML files that are output by the program are saved to the
“crawler_output” folder. Some titles contained forward or back slashes, which caused errors
when saving the HTML files. To fix this, I made the program replace any forward or back
slashes in the titles with an underscore. Once a page has been saved successfully, the crawler
then checks if the page limit has been reached. If it has, it will break from the loop at this point.
Otherwise, the page’s main text will be analyzed for outgoing URLs. These outgoing URLs are
then cleaned, reformatted, and put into the queue to be traversed by the while loop. This process
will continue until the enough pages are saved to reach the page limit. Once the page limit is hit,
the program will exit the while loop and output a new file called “crawled_urls.txt” with all the
saved URLs.
  
Sometimes, a connection error may occur when running the crawler. If this occurs, one
can simply delete the “crawler_output” folder from their computer and restart the program until
it does not happen. This is not an issue with the program, instead it is an issue with Wikipedia’s
connection to the crawler.  
## Number of Pages Crawled
In my source code, I set up the web crawler to output a total of 500 unique pages. The
files generated by the web crawler were output to a folder called “Assignment2” located on my
desktop. The web crawler lets users set a limit to the number of pages the want to save during the
crawling process. 

# Frequency-Based Indexer | Information
This program produces a frequency-based inverted index in a plain text file as well as a second plain
text file containing all of the unique terms in the index. I began by importing all the packages
needed for the program. BeautifulSoup assists with obtaining the text from each document. NLTK
assists with tokenizing the text from each document. I found that NLTK needed some more package
downloads to work the way I wanted it to, so I have included these lines in the program as well. I
used natsort to order my documents which had numbered titles from the WebCrawler I made in
the previous assignment. Finally, I decided to also use OrderedDict to alphabetically order the
index prior to output.
  
For this example, the user would have to input 500 crawled webpages. To do this, I set up
the “input_path” variable which should lead to the folder which contains the 500 .html files. I
also set up the “output_path” variable for users to set where they would like the indexer to output
its text files. The indexer function itself takes the “input_path” and “output_path” as “source”
and “destination” respectively. Once the index is initialized, the files paths for each document are
prepared and put into a queue. A while loop is then used to traverse this queue and analyze each
.html document individually.
  
When a document is being analyzed in the “while” loop, its path is removed from the
queue and stored in the “path” variable. At this point, the document’s text is extracted using
BeautifulSoup and then cleaned. All symbols, numbers, and non-English characters are removed
and replaced with spaces. The reasoning behind removing the numbers from the text is because,
as I was creating the indexer, I noticed much of the data was full of numbers that had no clear
meaning behind it. In addition to this, non-English symbols were found in the text which needed
to be removed. After the text cleaning process is done, it is sent to the next stage of this program
where the text is then tokenized using NLTK. Stop word removal subsequently occurs for more
accurate results. The tokens are then parsed and accurately placed into the index through a
process where, since this is a frequency-based inverted index, if a token is already in the index,
the frequency of that token will simply increase by one. Otherwise, if the token is not in the
index yet, the token will be added as a new key and the frequency will be initialized with a value
of 1. This process will repeat until the document queue is empty and some counters, which are
used extensively throughout my program in different ways, will increase each time the while
loop finishes.
  
Once the document queue is empty, the program will jump out of the while loop and
move on to the file output. Prior to output, the index is put into alphabetical order using
OrderedDict. Once that is completed, the “frequency-based-index.txt” file is created, and the
index is written to the file in an easy-to-read format. To finish it off, the program creates the
“unique_terms.txt” file which counts and displays all the unique terms in the index. Overall, the
final product works perfectly with the output from the Web Crawler I made in the previous
assignment. 

# RapidMiner Analysis - Document Clustering
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Process.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Process%20Documents%20From%20Files.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Vector.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20n-Grams%20Max%20Length.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Select%20Attributes.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Filter%20Tokens.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Text%20Directories.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Different%20Parameter%20Result.png "Screenshot")
![Screenshot](/Document%20Clustering/RESULTS%20-%20Document%20Clustering%20-%20Graph.png "Screenshot")
![Screenshot](/Document%20Clustering/RESULTS%20-%20Document%20Clustering%20-%20ExampleSet.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20k-Means%20Parameters.png "Screenshot")
![Screenshot](/Document%20Clustering/RESULTS%20-%20Document%20Clustering%20-%20Cluster%20Model.png "Screenshot")
![Screenshot](/Document%20Clustering/Document%20Clustering%20-%20Different%20Parameter%20Graph.png "Screenshot")
![Screenshot](/Document%20Clustering/RESULTS%20-%20Document%20Clustering%20-%20Centroid%20Table.png "Screenshot")

# RapidMiner Analysis - Keyword Clustering
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")

# RapidMiner Analysis - Association Rule Mining
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")
![Screenshot](/Banner "Screenshot")


