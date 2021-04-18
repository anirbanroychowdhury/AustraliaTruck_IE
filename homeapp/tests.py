from django.test import TestCase

# Create your tests here.

dd = 'No goods-carrying vehicle over 4.5 tonnes GVM can pass this sign without a permit from VicRoads or from the local council, unless the following exemptions apply: \r\n» the driver travels beyond the sign in any other lane, or \r\n» the driver of the truck is loading or unloading at a location beyond the no truck sign and no suitable alternative route to the location exists \r\n» the driver is escorted by a police officer or an authorised officer of the corporation.'

dd= dd.replace("\r\n", "")
print(dd)

from django.test import TestCase

# Create your tests here.

import austruckie.DatabaseControler as db

# Connect to the database
dbConn = db.func_ConnectToDB()

db.func_displayDatabase()