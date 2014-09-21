#!/usr/bin/python

import yaml

import random


#open the list of all songs

allsongs = open("songlist.yml", 'r')

songbook = yaml.safe_load(allsongs)

allsongs.close()

songs = songbook.keys()

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


#build a list of song tempos


#==BUILD THE SETS==#



#dump the list of all songs
#print yaml.safe_load(allsongs)
