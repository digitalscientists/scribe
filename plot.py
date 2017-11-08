import matplotlib.pyplot as plt
import sys
import os
import xml.etree.ElementTree as ET

fig = plt.figure()
ax = fig.add_subplot(111)
#os.getcwd() + '/' + 
file_path = sys.argv[1]
tree = ET.parse(file_path)
root = tree.getroot()
stroke_sets = root.findall('StrokeSet')
for stroke_set in stroke_sets:
  for stroke in stroke_set.findall('Stroke'):
    x_points = []
    y_points = []
    for point in stroke.findall('Point'):
      x_points.append(int(point.attrib['x']))
      y_points.append(int(point.attrib['y']))
    p = ax.plot(x_points, y_points)

ax.set_xlabel('x-points')
ax.set_ylabel('y-points')
plt.gca().set_aspect('equal', adjustable='box')
plt.gca().invert_yaxis()
plt.show()

# plot to see capture data seems to confirm captured data is correct