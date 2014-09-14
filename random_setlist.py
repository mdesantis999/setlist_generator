#!/usr/bin/python

import random

#name of the file with all songs, 1 song per line
songsource = 'songlist.txt'

#number of sets desired
numsets = 4

#legnth of each set
setlength = 8

#always start with position 0
currentsong = 0

lastsong = 0

#open the file
with open(songsource) as f:

        allsongs = f.read().splitlines()

#randomize the order of songs
random.shuffle(allsongs)

#create the setlists
for l in range(1, numsets):

        print "SET " + str(l)

        lastsong = currentsong + setlength

        for s in range(currentsong, lastsong):

                print allsongs[s]

                currentsong = lastsong

