#!/usr/bin/python

# OrangUtan.py
#
# Class to store details of tracked Orang-Utans.
#
# AMJ
# 23rd November 2004

from math import sqrt

class OrangUtan:
  name = ""
  x = 0                 # X position in forest
  y = 0                 # Y position in forest

  # Constructor

  def __init__ (self, name = "", x = 0, y = 0):
    self.name = name
    self.x = x
    self.y = y

  # String Representation. Format is like "Steve is at (0, 0)".

  def __str__ (self):
    return self.name + " is at (" + str (self.x) + ", " + str (self.y) + ")"

  # Selectors

  def getName (self):
    return self.name

  def getX (self):
    return self.x

  def getY (self):
    return self.y

  # Mutators

  def setName (self, newName = ""):
    self.name = newName

  def setX (self, newX = 0):
    self.x = newX

  def setY (self, newY = 0):
    self.y = newY

  # Movement

  def moveNorth (self):
    self.y = self.y + 1

  def moveSouth (self):
    self.y = self.y - 1

  def moveEast (self):
    self.x = self.x + 1

  def moveWest (self):
    self.x = self.x - 1

  def moveTo (self, newX = 0, newY = 0):
    self.x = newX
    self.y = newY

  # Distance from a Point

  def distanceFrom (self, x, y):
    dx = self.x - x
    dy = self.y - y

    return sqrt (dx * dx + dy * dy)

  # Check for Position. Return True iff at position (x, y).

  def atPosition (self, x, y):
    return self.x == x and self.y == y
