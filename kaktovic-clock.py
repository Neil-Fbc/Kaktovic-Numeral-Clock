#!/usr/bin/env python3

import time
from datetime import datetime

import pygame
import sys

pygame.init()


# screen = pygame.display.set_mode((800, 500))


zero = "";one = "";two = "";three = "";four = "";five = "";six = ""
seven = "";eight = ""   ;nine = "";ten = "";eleven = "";twelve = ""
thirteen = "";fourteen = "";fifteen = "";sixteen = "";seventeen = ""
eightteen = "";nineteen = ""
f = pygame.font.Font("InupiaqNumbers.ttf",64)
print(six);print("");
time.sleep(10)
while True:
 for e in pygame.event.get():
  if e.type == pygame.QUIT:
   pygame.quit()
   sys.exit()
 

 now = datetime.now() 
 hrs = int (now.strftime("%H"))
 min = int (now.strftime("%M"))
 sec = int (now.strftime("%S"))
 # print(min)
 hours = ""
 minutes = ""
 seconds = ""
 s = ""
 # hrs = 23
 # min = 58
 # sec = 39
 if (hrs == 0): hours = zero
 if (hrs == 1): hours = one
 if (hrs == 2): hours = two
 if (hrs == 3): hours = three
 if (hrs == 4): hours = four
 if (hrs == 5): hours = five
 if (hrs == 6): hours = six
 if (hrs == 7): hours = seven
 if (hrs == 8): hours = eight

 if (hrs == 9): hours = nine
 if (hrs == 10): hours = ten
 if (hrs == 11): hours = eleven
 if (hrs == 12): hours = twelve
 if (hrs == 13): hours = thirteen
 if (hrs == 14): hours = fourteen
 if (hrs == 15): hours = fifteen
 if (hrs == 16): hours = sixteen
 if (hrs == 17): hours = seventeen
 if (hrs == 18): hours = eightteen
 if (hrs == 19): hours = nineteen
 if (hrs == 20): hours = one + zero 
 if (hrs == 21): hours = one + one
 if (hrs == 22): hours = one + two 
 if (hrs == 23): hours = one + three 
 
 mn = 0
 if (min == 0): minutes = zero
 if (min == 1): minutes = one
 if (min == 2): minutes = two
 if (min == 3): minutes = three
 if (min == 4): minutes = four
 if (min == 5): minutes = five
 if (min == 6): minutes = six
 if (min == 7): minutes = seven
 if (min == 8): minutes = eight

 
 if (min == 9): minutes = nine
 if (min == 10): minutes = ten
 if (min == 11): minutes = eleven
 if (min == 12): minutes = twelve
 if (min == 13): minutes = thirteen
 if (min == 14): minutes = fourteen
 if (min == 15): minutes = fifteen
 if (min == 16): minutes = sixteen
 if (min == 17): minutes = seventeen
 if (min == 18): minutes = eightteen
 if (min == 19): minutes = nineteen
 s = '%s' % min
 
 if (min > 19 and min <  30): mn = 1
 if (min > 29 and min <  40): mn = 2
 if (min > 39 and min <  50): mn = 3
 if (min > 49 and min <  60): mn = 4
 # print (s[1:2], mn); print (mn)
 
 if (mn == 1 and (s[1:2]) == "0"): minutes = one + zero 
 if (mn == 1 and (s[1:2]) == "1"): minutes = one + one
 if (mn == 1 and (s[1:2]) == "2"): minutes = one + two 
 if (mn == 1 and (s[1:2]) == "3"): minutes = one + three 
 if (mn == 1 and (s[1:2]) == "4"): minutes = one + four
 if (mn == 1 and (s[1:2]) == "5"): minutes = one + five 
 if (mn == 1 and (s[1:2]) == "6"): minutes = one + six 
 if (mn == 1 and (s[1:2]) == "7"): minutes = one + seven 
 if (mn == 1 and (s[1:2]) == "8"): minutes = one + eight
 if (mn == 1 and (s[1:2]) == "9"): minutes = one + nine
 
  
 if (mn == 2 and (s[1:2]) == "0"): minutes = one + ten
 if (mn == 2 and (s[1:2]) == "1"): minutes = one + eleven
 if (mn == 2 and (s[1:2]) == "2"): minutes = one + twelve
 if (mn == 2 and (s[1:2]) == "3"): minutes = one + thirteen
 if (mn == 2 and (s[1:2]) == "4"): minutes = one + fourteen
 if (mn == 2 and (s[1:2]) == "5"): minutes = one + fifteen
 if (mn == 2 and (s[1:2]) == "6"): minutes = one + sixteen
 if (mn == 2 and (s[1:2]) == "7"): minutes = one + seventeen
 if (mn == 2 and (s[1:2]) == "8"): minutes = one + eightteen
 if (mn == 2 and (s[1:2]) == "9"): minutes = one + nineteen
 
 
 if (mn == 3 and (s[1:2]) == "0"): minutes = two + zero
 if (mn == 3 and (s[1:2]) == "1"): minutes = two + one
 if (mn == 3 and (s[1:2]) == "2"): minutes = two + two
 if (mn == 3 and (s[1:2]) == "3"): minutes = two + three
 if (mn == 3 and (s[1:2]) == "4"): minutes = two + four
 if (mn == 3 and (s[1:2]) == "5"): minutes = two + five
 if (mn == 3 and (s[1:2]) == "6"): minutes = two + six
 if (mn == 3 and (s[1:2]) == "7"): minutes = two + seven
 if (mn == 3 and (s[1:2]) == "8"): minutes = two + eight
 if (mn == 3 and (s[1:2]) == "9"): minutes = two + nine
 
  
 if (mn == 4 and (s[1:2]) == "0"): minutes = two + ten
 if (mn == 4 and (s[1:2]) == "1"): minutes = two + eleven
 if (mn == 4 and (s[1:2]) == "2"): minutes = two + twelve
 if (mn == 4 and (s[1:2]) == "3"): minutes = two + thirteen
 if (mn == 4 and (s[1:2]) == "4"): minutes = two + fourteen
 if (mn == 4 and (s[1:2]) == "5"): minutes = two + fifteen
 if (mn == 4 and (s[1:2]) == "6"): minutes = two + sixteen
 if (mn == 4 and (s[1:2]) == "7"): minutes = two + seventeen
 if (mn == 4 and (s[1:2]) == "8"): minutes = two + eightteen
 if (mn == 4 and (s[1:2]) == "9"): minutes = two + nineteen
 
 sc = 0
 s1 = ""
 if (sec == 0): seconds = zero
 if (sec == 1): seconds = one
 if (sec == 2): seconds = two
 if (sec == 3): seconds = three
 if (sec == 4): seconds = four
 if (sec == 5): seconds = five
 if (sec == 6): seconds = six
 if (sec == 7): seconds = seven
 if (sec == 8): seconds = eight

 
 if (sec == 9): seconds = nine
 if (sec == 10): seconds = ten
 if (sec == 11): seconds = eleven
 if (sec == 12): seconds = twelve
 if (sec == 13): seconds = thirteen
 if (sec == 14): seconds = fourteen
 if (sec == 15): seconds = fifteen
 if (sec == 16): seconds = sixteen
 if (sec == 17): seconds = seventeen
 if (sec == 18): seconds = eightteen
 if (sec == 19): seconds = nineteen
 s = '%s' % sec
 
 if (sec > 19 and sec <  30): sc = 1
 if (sec > 29 and sec <  40): sc = 2
 if (sec > 39 and sec <  50): sc = 3
 if (sec > 49 and sec <  60): sc = 4
 
 if (sc == 1 and (s[1:2]) == "0"): seconds = one + zero 
 if (sc == 1 and (s[1:2]) == "1"): seconds = one + one
 if (sc == 1 and (s[1:2]) == "2"): seconds = one + two 
 if (sc == 1 and (s[1:2]) == "3"): seconds = one + three 
 if (sc == 1 and (s[1:2]) == "4"): seconds = one + four
 if (sc == 1 and (s[1:2]) == "5"): seconds = one + five 
 if (sc == 1 and (s[1:2]) == "6"): seconds = one + six 
 if (sc == 1 and (s[1:2]) == "7"): seconds = one + seven 
 if (sc == 1 and (s[1:2]) == "8"): seconds = one + eight
 if (sc == 1 and (s[1:2]) == "9"): seconds = one + nine
 
  
 if (sc == 2 and (s[1:2]) == "0"): seconds = one + ten
 if (sc == 2 and (s[1:2]) == "1"): seconds = one + eleven
 if (sc == 2 and (s[1:2]) == "2"): seconds = one + twelve
 if (sc == 2 and (s[1:2]) == "3"): seconds = one + thirteen
 if (sc == 2 and (s[1:2]) == "4"): seconds = one + fourteen
 if (sc == 2 and (s[1:2]) == "5"): seconds = one + fifteen
 if (sc == 2 and (s[1:2]) == "6"): seconds = one + sixteen
 if (sc == 2 and (s[1:2]) == "7"): seconds = one + seventeen
 if (sc == 2 and (s[1:2]) == "8"): seconds = one + eightteen
 if (sc == 2 and (s[1:2]) == "9"): seconds = one + nineteen
 
 
 if (sc == 3 and (s[1:2]) == "0"): seconds = two + zero
 if (sc == 3 and (s[1:2]) == "1"): seconds = two + one
 if (sc == 3 and (s[1:2]) == "2"): seconds = two + two
 if (sc == 3 and (s[1:2]) == "3"): seconds = two + three
 if (sc == 3 and (s[1:2]) == "4"): seconds = two + four
 if (sc == 3 and (s[1:2]) == "5"): seconds = two + five
 if (sc == 3 and (s[1:2]) == "6"): seconds = two + six
 if (sc == 3 and (s[1:2]) == "7"): seconds = two + seven
 if (sc == 3 and (s[1:2]) == "8"): seconds = two + eight
 if (sc == 3 and (s[1:2]) == "9"): seconds = two + nine
 
  
 if (sc == 4 and (s[1:2]) == "0"): seconds = two + ten
 if (sc == 4 and (s[1:2]) == "1"): seconds = two + eleven
 if (sc == 4 and (s[1:2]) == "2"): seconds = two + twelve
 if (sc == 4 and (s[1:2]) == "3"): seconds = two + thirteen
 if (sc == 4 and (s[1:2]) == "4"): seconds = two + fourteen
 if (sc == 4 and (s[1:2]) == "5"): seconds = two + fifteen
 if (sc == 4 and (s[1:2]) == "6"): seconds = two + sixteen
 if (sc == 4 and (s[1:2]) == "7"): seconds = two + seventeen
 if (sc == 4 and (s[1:2]) == "8"): seconds = two + eightteen
 if (sc == 4 and (s[1:2]) == "9"): seconds = two + nineteen
  
 
 srf = pygame.display.set_mode((300,100))
 srf.blit(f.render(hours,True,(255,0,0)),(20,20))
 srf.blit(f.render(minutes,True,(0,255,0)),(110,20))
 srf.blit(f.render(seconds,True,(0,0,255)),(200,20))
 
 pygame.display.flip()
 srf.blit(f.render(hours,True,(255,255,255)),(20,20))
 srf.blit(f.render(minutes,True,(255,255,255)),(110,20))
 srf.blit(f.render(seconds,True,(255,255,255)),(200,20))
 time.sleep(0.30)
 
   
