import random
import math
import sys
import numpy as np
from PIL import Image, ImageDraw

def cartesianProduct(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def drawBox(position, color, gameDisplay):
  gameDisplay.rectangle([(position[0]*15, position[1]*15), (((position[0]+1)*15)-1, ((position[1]+1)*15)-1)], color)

def drawTriangle(position, color, gameDisplay):
  basePixel = (position[0] * 15, position[1] * 15)
  gameDisplay.polygon([(basePixel[0]+7, basePixel[1]), (basePixel[0], basePixel[1]+14), (basePixel[0]+14, basePixel[1]+14)], color)

def generateSimHabitat(carnivores):
  #Do Calculations
  smallCarnivore = random.randint(0, carnivores)
  largeCarnivore = carnivores - smallCarnivore
  
  smallHerbivoresForLarge = random.randint(0, largeCarnivore)
  smallHerbivore = (smallCarnivore * 2) + (smallHerbivoresForLarge * 4)
  largeHerbivore = (largeCarnivore-smallHerbivoresForLarge) * 2
  
  treesForSmall = random.randint(0, smallHerbivore)
  herbaceousPlantsForSmall = random.randint(0, smallHerbivore-treesForSmall)
  grassesForSmall = smallHerbivore-herbaceousPlantsForSmall-treesForSmall
  treesForLarge = random.randint(0, largeHerbivore)
  herbaceousPlantsForLarge = random.randint(0, largeHerbivore-treesForLarge)
  grassesForLarge = largeHerbivore-herbaceousPlantsForLarge-treesForLarge
  trees = treesForSmall + (treesForLarge * 2)
  herbaceousPlants = (herbaceousPlantsForSmall * 2) + (herbaceousPlantsForLarge * 4)
  grasses = (grassesForSmall * 4) + (grassesForLarge * 8)
  
  water = (trees * 3) + (herbaceousPlants * 2) + (grasses * 1)
  
  decomposers = grasses + herbaceousPlants + trees + largeHerbivore + smallHerbivore + largeCarnivore + smallCarnivore
  print()
  print("Number of Decomposers:", decomposers)
  print("Number of Water:", water)
  print("Number of Trees:", trees)
  print("Number of Herbaceous Plants:", herbaceousPlants)
  print("Number of Grasses:", grasses)
  print("Number of Small Herbivores:", smallHerbivore)
  print("Number of Large Herbivores:", largeHerbivore)
  print("Number of Small Carnivores:", smallCarnivore)
  print("Number of Large Carnivores:", largeCarnivore)
  
  numberOfSquaresNeeded = int(sum([decomposers, water, trees, herbaceousPlants, grasses, smallHerbivore, largeHerbivore, smallCarnivore, largeCarnivore])*1.3)
  print(numberOfSquaresNeeded)
  pixelsPerBox = 15
  pixelsDimension = math.ceil(numberOfSquaresNeeded ** 0.5) * pixelsPerBox
  print(pixelsDimension)
  numberOfSquaresNeeded = int((pixelsDimension / pixelsPerBox) ** 2)
  print(numberOfSquaresNeeded)

  #Generate Image
  black = (0,0,0)
  white = (255,255,255)
  red = (255,0,0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  brown = (200, 100, 100)
  darkGreen = (0, 150, 0)
  yellow = (255, 255, 0)
  
  img = Image.new("RGB", (pixelsDimension, pixelsDimension), color = white)
  gameDisplay = ImageDraw.Draw(img)  
  
  dimension = np.array([i for i in range(int(numberOfSquaresNeeded ** 0.5))])
  print('done')
  squareCoords = cartesianProduct(dimension, dimension)
  np.random.shuffle(squareCoords)
  
  print(1)
  index = 0
  for i in range(decomposers):
    drawBox(squareCoords[index], brown, gameDisplay)
    index += 1
  print(2)
  for i in range(water):
    drawBox(squareCoords[index], blue, gameDisplay)
    index += 1
  print(3)
  for i in range(trees):
    drawBox(squareCoords[index], darkGreen, gameDisplay)
    index += 1
  print(4)
  for i in range(grasses):
    drawBox(squareCoords[index], green, gameDisplay)
    index += 1
  print(5)
  for i in range(herbaceousPlants):
    drawTriangle(squareCoords[index], green, gameDisplay)
    index += 1
  print(6)
  for i in range(smallHerbivore):
    drawTriangle(squareCoords[index], yellow, gameDisplay)
    index += 1
  print(7)
  for i in range(largeHerbivore):
    drawBox(squareCoords[index], yellow, gameDisplay)
    index += 1
  print(8)
  for i in range(smallCarnivore):
    drawTriangle(squareCoords[index], red, gameDisplay)
    index += 1
  print(9)
  for i in range(largeCarnivore):
    drawBox(squareCoords[index], red, gameDisplay)
    index += 1
  print(10)
  print('Saving PNG')
  img.save(f"SimHabitat_{carnivores}.png")

generateSimHabitat(int(input('Number of carnivores: ')))