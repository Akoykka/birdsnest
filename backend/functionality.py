# Import Modules
from xml.dom import minidom
from urllib.request import urlopen
import math
import sqlite3

def update_drone_entry(serialNumber, timestamp, distance):
	connection = sqlite3.connect("ndzViolators.db")
	cursor = connection.cursor

	result = cursor.execute("SELECT name FROM sqlite_master WHERE name='violators'")
	if (result.fetchone() == None):
		cursor.execute("CREATE TABLE violators(sn, dist, timestamp, name, phone, email)")

	result = cursor.execute("SELECT sn FROM violators WHERE name=(?)", serialNumber)
	db_entry = result.fetchone()
	if (db_entry == None and distance < 100000):
		create entry
		return
	if (distance < 100000 or db_entry):
		update_timestamp()
		update distance if needed
		return

def update_db_Request():

	openedUrl = urlopen("http://assignments.reaktor.com/birdnest/drones")
	document = minidom.parse(openedUrl)

	drones = document.getElementsByTagName("drone")
	for drone in drones:
		serialNumber = drone.getElementsByTagName("serialNumber")[0]
		posY = drone.getElementsByTagName("positionY")[0]
		posX = drone.getElementsByTagName("positionX")[0]
		timestamp = drone.getElementByTagName("time")[0]
		distance = get_distance_from_center(posY.firstChild.data, posX.firstChild.data)
		update_drone_entry(serialNumber.firstChild.data, timestamp.firstChild.data, distance.firstChild.data)

	remove_expired_entries()

def get_distance_from_center(posY, posX):
	return math.dist([posY, posX], [250000,250000])



		#print(serialNumber.firstChild.data)
		#print(posY.firstChild.data)
		#print(posX.firstChild.data)
		#print("\n")
