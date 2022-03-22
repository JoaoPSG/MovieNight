#libraries
import time
import numpy as np
import pandas as pd

import imdb
import requests
import json

# for the images
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format



#IMDB search for the add_movie
def get_imdb(searched_movie):
    ia = imdb.IMDb()
    movie = ia.search_movie(searched_movie)
    return movie

def roll_movie():
    movie_list = pd.read_csv('movie_list.csv')
    lucky_movie = movie_list.iloc[np.random.randint(0, movie_list.shape[0]), 0]
    
    print('The Lucky Movie iiiiissss:')
    for i in range(3):
        print('.')
        time.sleep(1)
        
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
    print(fireworks)
    print(lucky_movie)
    
    
def roll_food():
    food_list = pd.read_csv('food_list.csv')
    selected_food = food_list.iloc[np.random.randint(0, food_list.shape[0])]
    
    print('You are gonna eaaat:')
    for i in range(3):
        time.sleep(1)
        print('.')
        
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
    movie_list = movie_list.append(pd.Series([search_results[result_index]['title'], 'no path'], index=['Title', 'Path']), ignore_index=True)
    movie_list.to_csv('movie_list.csv', index=False)
    print('Done!')
    
    
def add_food():
    food = input('Food: ')
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
                
                
    food_list = pd.read_csv('movie_list.csv')
    food_list = food_list.append(pd.Series([food_list], index=['Food']), ignore_index=True)
    food_list.to_csv('food_list.csv', index=False)
    print('Done!')
    
    
def __init__():
    cprint(figlet_format('Movie', font='slant'), attrs=['bold'])
    cprint(figlet_format('    Night', font='slant'), attrs=['bold'])
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
            print('add_food()')
        elif a == '5':
            print('Goodbye!')
            time.sleep(1.5)
            break
        else:
            print('Sorry, I did not ger it :(')
            
            
            
__init__()