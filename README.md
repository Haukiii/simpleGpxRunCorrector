# Simple .gpx corrector script
This script identifies points in .gpx-files that are likely tracking errors due to e.g. high buildings and deletes these points. Outliers are identified by deviation from the median speed of the activity. The script, therefore, works best on steady activity tracks like walks or runs. 

It only removes outliers on the top end. Removing outliers where the speed is 0 or close to it would not actually remove them because the deleted points would still go into the calculation at 0. 
