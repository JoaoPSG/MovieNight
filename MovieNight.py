#libraries
import time
import numpy as np
import pandas as pd

import imdb
import requests
import json

# for the images




#global variables

RAPIDAPI_HOST = 'streaming-availability.p.rapidapi.com'
RAPIDAPI_KEY = 'c4bc6b5210msh7c0e4e2664d48bfp159b1ajsne6be12300548'
REQUEST_URL = 'https://streaming-availability.p.rapidapi.com/get/basic'
country = 'br'

#ASCII art

title = """
    __  ___           _    
   /  |/  /___ _   __(_)__ 
  / /|_/ / __ \ | / / / _ \\
 / /  / / /_/ / |/ / /  __/
/_/  /_/\____/|___/_/\___/ 


             _   ___       __    __
            / | / (_)___ _/ /_  / /_
           /  |/ / / __ `/ __ \/ __/
          / /|  / / /_/ / / / / /_
         /_/ |_/_/\__, /_/ /_/\__/
                 /____/
"""

fireworks = """
                                       .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
    """

fork_knife = """
           _
      / )
|||| / /
||||/ /
\__(_/
 ||//
 ||/
 ||
(||      
 ""
    """ 

pirate_flag = """
    ___
    \_/
     |._
     |'."-._.-""--.-"-.__.-'/
     |  \       .-.        (
     |   |     (@.@)        )
     |   |   '=.|m|.='     /
     |  /    .='`"``=.    /
     |.'                 (
     |.-"-.__.-""-.__.-"-.)
     |
     |
     |
"""

# Functions

#IMDB search for the add_movie
def get_imdb(searched_movie):
    ia = imdb.IMDb()
    movie = ia.search_movie(searched_movie)
    return movie


def roll_movie():
    movie_list = pd.read_csv('movie_list.csv', dtype={'movieID': str})
    lucky_movie = movie_list.iloc[np.random.randint(0, movie_list.shape[0]), :]
    
    #rolling movie
    print('The Lucky Movie iiiiissss:')
    for i in range(3):
        print('.')
        time.sleep(1)
        

    print(fireworks)
    print(lucky_movie['Title'])
    for i in range(2):
        print('.')
        time.sleep(0.25)


    # returning the availability
    #----
    def get_movie_availability(imdb_id):
        headers = {
            'X-RapidAPI-Host': 'streaming-availability.p.rapidapi.com', #RAPIDAPI_HOST,
            'X-RapidAPI-Key': 'c4bc6b5210msh7c0e4e2664d48bfp159b1ajsne6be12300548' # RAPIDAPI_KEY
        }
        params = {
            'country': 'br', # country,
            'imdb_id': f'tt{imdb_id}',
            'output_language': 'en'
        }   

        r = requests.get(REQUEST_URL, params=params, headers=headers)
        try:
            movie = r.json()
            movie_availability = movie['streamingInfo']
            return movie_availability
        except:
            return 'piracy time'
    #----
    
    movie_availability = get_movie_availability(lucky_movie['movieID'])

    try:
        netflix_link = movie_availability['netflix']['br']['link']
        netflix_status = True
    except:
        netflix_status = False
    try:
        prime_link = movie_availability['prime']['br']['link']
        prime_status = True
    except:
        prime_status = False

            
    if netflix_status == True:
        print('Netflix link:')
        print("  " + netflix_link)         
    elif prime_status == True:
        print(f'Prime link: {prime_link}')         
    else:
        print('Raise the sails and keep your gun close...')
        for i in range(1):
            print('.')
            time.sleep(0.25)
        print("You're going to The Pirate Bay!" )
        for i in range(1):
            print('.')
            time.sleep(1)
        print(pirate_flag)
        time.sleep(1)
    
def roll_food():
    food_list = pd.read_csv('food_list.csv')
    selected_food = food_list.iloc[np.random.randint(0, food_list.shape[0])]
    
    print('You are gonna eaaat:')
    for i in range(3):
        time.sleep(1)
        print('.')
        
    print(fork_knife)
    print(selected_food['Food'])
    
    
def add_movie():
    searched_movie = input('Title: ')
    search_results = get_imdb(searched_movie)
    result_index = 0
    a = '2'
    while a == '2': 
        print('Is this the movie? ' + search_results[result_index]['title'])
        print("1 -> Yep")
        print("2 -> Nop")
        a = input()
        if a == 1:
            pass
        elif a == '2':
            print(':(')
            print('1 -> Input another name')
            print('2 -> Next movie')
            b = input()

            if b == '1':
                add_movie()
                break
            elif b == '2':
                result_index += 1
            else:
                print('Sorry, I did not understand')
        else:
            pass
                
                
    movie_list = pd.read_csv('movie_list.csv')
    movie_list = movie_list.append(
        pd.Series(
            [search_results[result_index].movieID,
            search_results[result_index]['title']],
            index=['movieID', 'Title']),
        ignore_index=True)
    movie_list.to_csv('movie_list.csv', index=False)
    print('Done!')
    
    
def add_food():
    food = input('Food: ')        
    food_list = pd.read_csv('food_list.csv')
    food_list = food_list.append(pd.Series([food], index=['Food']), ignore_index=True)
    food_list.to_csv('food_list.csv', index=False)
    print('Done!')
    for i in range(2):
        time.sleep(.5)
        print('.')
    print('Add another one?')
    print('1 -> Yes')
    print('2 -> No')
    another = input()

    if another == '1':
        add_food()
    
    
def init():
    print(title)
    while True:
        for i in range(3):
            print('.')
            time.sleep(1)
        print("What do you want to do?")
        print("1 -> Roll a Movie!!")
        print("2 -> Roll FOOOD!!")
        print("3 -> Add movie")
        print("4 -> Add food")
        print('5 -> Exit')
        a = input()
        if a == '1':
            roll_movie()
        elif a == '2':
            roll_food()
        elif a == '3':
            add_movie()
        elif a == '4':
            add_food()
        elif a == '5':
            ## idea: instead print 'Have a good movie!' if movie was rolled
            print('Goodbye!')
            time.sleep(1.5)
            break
        else:
            print('Sorry, I did not ger it :(')
            
            
            
init()