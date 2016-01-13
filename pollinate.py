import numpy

import cv2

# Hi Natalie! Let's get started!

# step 1: load the image!
img = cv2.imread('data/wtd.jpg')

# step 2: load the location data (what location does this image represent?)

# step 3: convert to greyscale for the edge detection
#         colour could be important (identifying trees? blue tarps = target communities?)
#         but for edge detection greyscale is fine
grey = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

# step 4: analyse the image.
#         algorithm 1: target communities are more complex/more finely structured than formal housing
#         (Kit and Ludeke paper)
edges = cv2.Canny(grey, 100, 200)
cv2.imwrite("data/edges.bmp", edges)
window_size = 20
filter = numpy.ones([window_size, window_size], numpy.float32) / window_size / window_size

filtered = cv2.filter2D(edges, 1, filter)

cv2.imwrite("data/filtered.bmp", filtered)

# step 5: use the analysis to classify points into target/not target communities
#         for our complexity measure maybe what I would do is use a window filter (or split the image into tiles)
#         that counts/sums the edges surrounding a point
#         more edges = more complex structures = target community?

thresh = 75
ret, thresholded = cv2.threshold(filtered.astype(numpy.uint8), thresh, 255, cv2.THRESH_BINARY)
cv2.imwrite("data/thresholded.bmp", thresholded)

# step 6: merge adjacent target communities into larger groups?

# step 7: plot the target communities on the map
#         for this we need the location data for the original image
#         this will tell us how to convert (x, y) in pixels -> (lat, lon) on the map

# step 8: output as kml
#         we can attach whatever data we want to the points
#         as well as set their colour and icon on the map
