#!/usr/bin/python

import yaml

import random


#open the list of all songs

allsongs = open("songlist.yml", 'r')

songbook = yaml.safe_load(allsongs)

allsongs.close()

song_titles = songbook.keys()

random.shuffle(songs)


#input number of sets

num_setlists = input('Enter number of sets: ')

#input number of songs per set    

num_songs = input('Enter number of songs per set: ')


#initialize the setlist profile
#TODO: separate this out into a function
#based on total number of songs per set, figure out how
#many are fast, medium or slow based on the percentages in profile

profile = { 'fast': .40, 'medium': .30, 'slow': .30 }

num_fast = int(num_songs * profile.get('fast'))

num_medium = int(num_songs * profile.get('medium'))

num_slow = int(num_songs * profile.get('slow'))


#now we have a problem; the rounded number of each type of song
#doesn't equal the total number of songs in the set. So we have
#to deal with the overage

shortfall = num_songs - (num_fast + num_medium + num_slow)

if shortfall > 0:

  for _ in xrange(shortfall):

    tempos = ['fast', 'medium', 'slow']

    random.shuffle(tempos)

    if tempos[0] == 'fast':

      num_fast = num_fast + 1

    elif tempos[0] == 'medium':

      num_medium = num_medium + 1

    else:

      num_slow = num_slow + 1


#build a profile list of song tempos
#TODO: build a profile list for each set

profile = []

fast = 'fast'

medium = 'medium'

slow = 'slow'

profile.extend([fast] * (num_fast - 2))

profile.extend([medium] * num_medium)

profile.extend([slow] * num_slow)

random.shuffle(profile)

profile.insert(0, 'fast') #first song is fast

profile.insert(len(profile), 'fast') #last song is fast


#==BUILD THE SETS==#

#get the list of all songs
#songbook is the dictionary with attributes
#song_titles is the random sorted list of songs
#profile is the setlist profile

#iterate through the profile and find a song that matches the tempo in the profile
#put the song in the list and take it out of the pool of available songs



#print the setlists
