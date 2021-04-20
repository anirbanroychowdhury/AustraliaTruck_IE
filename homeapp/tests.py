from django.test import TestCase

# Create your tests here.

import austruckie.DatabaseControler as db

first = ["a", "b", "c"]
second = [1,2,3]
mylist = zip(first , second)

dbConn = db.func_ConnectToDB()

# General Rules list extraction
db_Rule_List = db.func_SendSQL(dbConn, "SELECT RuleText, SignPictureURL FROM ruleandregulation where Truck=1")

# Return is a tuple, convert to list so that we can edit it
db_Rule_List = list(db_Rule_List)

# For loop to replace the enter chara with HTML tag and clear some unwanted chars
for i in range(0, len(db_Rule_List)):
    # Get the rule text part
    db_Rule_List[i] = list(db_Rule_List[i])
    tempstr = str(db_Rule_List[i][0])
    # Clean
    tempstr = tempstr.replace("\\r\\n", "<br> - ")
    tempstr = tempstr.replace("Â»", " ")
    tempstr = tempstr.replace("'", "")
    tempstr = tempstr.replace("]", "")
    tempstr = tempstr.replace("[", "")
    # Update
    db_Rule_List[i][0] = tempstr

RuleText = []
RulePictures = []

for oneRule in db_Rule_List:
   RuleText.append(oneRule[0])
   RulePictures.append(oneRule[1])

db_Rule_List = zip(RuleText, RulePictures)
for one in db_Rule_List:
    print(type(one), one)

