import os,sys
from imdb import imdb
from Helper import Helper
from filemode import main
def modes():
    try:
        if len(sys.argv) == 2:
            if sys.argv[1]=='-g':
                graphicalmode()
            else:
                raise     
        elif len(sys.argv)==3:
            if sys.argv[1]=='-f' and sys.argv[2]:
                path=sys.argv
            else:
                raise
        else:
            raise
    except:
         print ("\n\n  usage :  python main.py {option}  \n\nOptions\n\n1.for file mode : -f path\\to\\movies\\folder \n2.for graphical mode: -g ")
                    
def graphicalmode():
	""" user interactive terminal based results"""
	mov_name=Helper.get_movie_name_user()
	#category=Helper.get_search_categories() currently designed only for movies
	url=Helper.prepare_search(mov_name,'tt') #'tt' is to search in movies titles
	req=Helper.get_request(url)    
	soup=Helper.make_soup(req.content)
	titles=imdb.soup_titles(soup)
	title_link=Helper.select_title(titles)
	results=imdb.soup_movie_page(title_link)
	if results:
		print_all(results)


	
def filemode(folderpath):
    """search the current folder for movies and stores the webpage"""
    try:
        dir_path=folderpath
        if os.path.exists(dir_path):
            """Check which files already exists -currently not implemented
            imdb_fol_path=os.path.join(dir_path,"imdb")
                already_present=[]
            if os.path.exists(imdb_fol_path):
                        collect_files(imdb_fol_path)
            filenames=[]
            """
            main(dir_path)
        else:
            print ("Folder does not exists")
	
    except:
        print("Error Occured while loading the folder")        
	#for content in os.listdir(dir_path):
		
def print_all(results):
	print '\n'
	print "Name : ",results["name"]
        print '\n'
	print "Rating :",results["rating"]
	print '\n'
	print "Content Rating : ",results["content_rating"]
	print '\n'
	print "Time :",results["running_time"]
	print '\n'
	print "Story : ",results["storyline"]
	print '\n'
	print "Genre : ",results["genre"]
	print '\n'
	print "Credits\n",results["credits"]
	print '\n'


if __name__=="__main__":
	modes()
	
