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

num_setlists = num_setlists - 1


#input number of songs per set    #python lists start at 0

num_songs = input('Enter number of songs per set: ')

num_songs = num_songs - 1


#initialize the setlist profile

profile = { 'fast': .40, 'medium': .30, 'slow': .30 }

num_fast = num_songs * profile.get('fast')

num_medium = num_songs * profile.get('medium')

num_slow = num_songs * profile.get('slow')

print int(num_fast), int(num_medium), int(num_slow)





#==BUILD THE SETS==#



#dump the list of all songs
#print yaml.safe_load(allsongs)
