# -*- coding: utf-8 -*-
"""
This is a bot that will give you the definition of a word in any subreddit you chose.
Must call upon the bot with !wordBot

Created on Fri Jul 20 19:53:51 2018

@author: Dalton
"""

import praw
from PyDictionary import PyDictionary
from nltk.corpus import wordnet


print('Logging Into Reddit...')
    #Create Bot with login and private key - username - password
reddit = praw.Reddit(user_agent=', client_id='', client_secret='',
        username='', password='')
print('Logged in')
    
    # dictionary and word check
dictionary = PyDictionary()



# the subreddits you want your bot to live on
subreddit = reddit.subreddit('books')

# phrase to activate the bot
keyphrase = '!wordBot'



# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            if wordnet.synsets(word):
                # get meaning as object, get the index of a sentence and reply it
                words = dictionary.meaning(word)
                reply = [item[0] for item in words.values()]
                comment.reply(word + ': '  + reply[0] .format(comment.author))
                print('posted')
            else:
                reply = 'This is not a word.'
                comment.reply(reply)
                print('posted')
        except:
            print('to frequent')
    
    
    
    
    

