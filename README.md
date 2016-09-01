# ImdbScraper
A Python program to fetch information about movies from IMDB

Do you face this problem where you have lots of movies and you have no idea which moview to watch first. then, this script is going to solve your problem 
<br>
this script scrapes data from imdb for any particular movie and show the information almost instantly.
<br>
you can also just specify a root folder of your movies directory and script will automatically crawl through every movie and store all information in a directory.

##  How To Use
At this Moment the module can be run in any of two mode:

1. Graphical Mode :
  <br>
  usage:
    1. navigate to ImdbScraper Folder. <br>
    2. type "python main.py -g" <br>
	  Details : 
	  This mode is user interactive a user can enter any particular movie name and the results would be shown.Currently, it is working only on Movies searches.if you wish you can contrubute to expand it to tv shows and celebrity name.
2. File Mode :
  <br>
	usage:
	1. navigate to ImdbScraper Folder. <br>
 	2. type "python main.py -f valid/folder_path/to_search" <br>
	Details:
	This mode takes folder path as an argument,search all the video files in that folder or sub folders and dwonloads a webpage for all of the movies it founds.on can contribute to make the module multithreaded   
