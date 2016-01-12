import cv2

# load a satellite image
# inputs: image file, length, width, location info (scale image distance to real distance, location of image)
# outputs: image object

# break up an image into tiles

# analyse a tile
# input: a tile
# output: a classification

img = cv2.imread('/home/matthewi/Pictures/reignite.png')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey, 100, 200)

cv2.imwrite("edges.bmp", edges)

# list of points -> kml
