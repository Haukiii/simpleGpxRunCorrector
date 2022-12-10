# Import packages
import gpxpy
import numpy as np

# Read gpx-file
gpxFile = "yourfile.gpx"
gpx_file = open(gpxFile, 'r')
gpx      = gpxpy.parse(gpx_file)

# Calculate speeds between points
speed = []

for track in gpx.tracks:
  for segment in track.segments:
    for point_no, point in enumerate(segment.points):
        speed.append(point.speed_between(segment.points[point_no - 1]))

# Upper limit is defined as 3x the 75% quantile, this can be tweaked according to the GPS errors encountered
upperLimit = 3*(np.quantile(speed, q = 0.75))

# Find elements above the threshold
indices = [
    index for index, item in enumerate(speed)
    if item > upperLimit
]

pointsRemoved = 0

while len(indices) > 0:
    gpxpy.gpx.GPXTrackSegment.remove_point(gpx,indices[0])
    pointsRemoved = pointsRemoved + 1
    # Calculate speeds between points
    speed = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point_no, point in enumerate(segment.points):
                speed.append(point.speed_between(segment.points[point_no - 1]))

    indices = [
        index for index, item in enumerate(speed)
        if item > upperLimit
    ]

print(pointsRemoved)

# Write the corrected GPX file
outputFile = gpxFile[:-4] + "_corrected.gpx"
with open(outputFile, "w") as f:
    f.write( gpx.to_xml())