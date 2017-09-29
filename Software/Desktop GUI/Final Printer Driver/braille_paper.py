#!/usr/bin/env python

import pygame, sys
from pygame.locals import *
import numpy as np

SPACE = (255, 255, 255)
UNOCCUPIED = (30, 30, 30)
DOT = (0, 0, 0)

#useful game dimensions
TILESIZE  = 5
MAPWIDTH  = 180
MAPHEIGHT = 189

alpha = []
char_cell = {}
tilemap = range(MAPHEIGHT)
for h in range(MAPHEIGHT):
  tilemap[h] = range(MAPWIDTH)
  for w in range(MAPWIDTH):
    tilemap[h][w] = SPACE


#load mapping data from file and then populate a dictionary with it
#also load the alphabets into an array just for testing the celler.
def load_mapping(file):
  global alpha
  global char_cell
  m_f = open(file, 'r')
  c = m_f.readline()
  while c != '':
    char_cell[c[0]] = int(c[2:len(c)-1])
    alpha.append(c[0])
    c = m_f.readline()
    
def celler(xx, yy, cell_id):
  #print "For cell ID = %s" % cell_id
  x = 2 + xx*5
  y = 3 + yy*7
  d = {1 : -2, 2 :  -2, 3 : 0, 4 : 0, 5 : 2, 6 : 2}
  for i in range(1, 7):
    if ((1 << i) & cell_id > 0):
      #print "True :%s" % i
      tilemap[y + d[i]][(x-1) if i%2 != 0 else (x+1)] = DOT

def main(to_be_printed):
  load_mapping(to_be_printed)

  xx = 1
  yy = 1
  for c in alpha:
    #print c
    celler(xx, yy, char_cell[c])
    xx += 1
    if xx == 30:
      yy += 1
      xx = 1

  #set up the display
  pygame.init()
  DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
  keepGoing = True
  i = 0
  while keepGoing:
      for row in range(MAPHEIGHT):
          for column in range(MAPWIDTH):
              pygame.draw.rect(DISPLAYSURF, tilemap[row][column], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          keepGoing = False
      if pygame.key.get_focused():
        kp = pygame.key.get_pressed()
        import time
        time.sleep(5)
        if kp[pygame.K_UP] == 1:
          print "UP is Pressed"

      elif kp[pygame.K_DOWN] == 1:
        print "DOWN is pressed"
      i = i + 1
  pygame.quit()

if __name__ == '__main__':main()