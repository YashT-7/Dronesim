import time
import argparse
from flyt_python import api

drone = api.navigation(timeout=120000)

# at least 3sec sleep time
time.sleep(3)

#arguments
parser = argparse.ArgumentParser(description='Process a float value.')
parser.add_argument('side', metavar='side_length', type=float, help='side length of the square')
args = parser.parse_args()

side_length = args.side

print "taking off at 10m"
drone.take_off(10.0)

print 'flying in triangle', side_length
drone.position_set(side_length, 0, 0, relative=True)
drone.position_set(-side_length/2, side_length *0.866, 0, relative=True)
drone.position_set(-side_length/2, -side_length *0.866, 0, relative=True)

print "landing"
drone.land(False)
print 'Section A Task 2 completed'

# shutdown the instance
drone.disconnect()