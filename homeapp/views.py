from django.shortcuts import render

import austruckie.DatabaseControler as db
import austruckie.ErrorReporting as Err

# Create your views here.
accessOK = False

# Open the home page. This is called after the password check
def home_view(request, *args, **kwargs):
    if accessOK:
        return render(request,"home.html",{})
    else:
        return render(request, "AccessPage.html", {})

# This is to render the access page html form the Templete
def passwordasking(request):
    return render(request, "AccessPage.html", {})

# This is a POST handler method that accept in the password and check it
def requestAccess(request):
    if request.method == 'POST':
        # The request type is POST, so check the paramters
        if request.POST['passIn'] == 'haddoken':
            # Password was correct, display the main page
            accessOK = True
            return render(request,"home.html",{})
        else:
            # The password is wornge, or the request is worng, simply rerender the page
            return render(request, "AccessPage.html", {})

def check_list(request, *args, **kwargs):
    return render(request,"checklist.html",{})

def about_us(request, *args, **kwargs):
    return render(request,"aboutus.html",{})

def rules(request):

    # Connect to the database
    dbConn = db.func_ConnectToDB()

    # Trucks types extraction
    db_truck_types = db.func_SendSQL(dbConn, "SELECT TypeName, ID FROM truckstype")
    truck_types = ["<option value='2'>General</option>"]
    for i in range(0, len(db_truck_types)):
        truck_types.append("<option value='"+ str(db_truck_types[i][1]) +"'>"+ str(db_truck_types[i][0]) +"</option>")

    # License Types extraction
    db_License_types = db.func_SendSQL(dbConn, "SELECT LicenseTypeName, LicenseTypeID FROM licensetype")
    License_types = ["<option value='Null'>General</option>"]
    for i in range(0, len(db_License_types)):
        License_types.append("<option value='"+ str(db_License_types[i][1]) +"'>"+ str(db_License_types[i][0]) +"</option>")

    # ------------------------------------------------
    # General Rules list extraction
    db_Rule_List = db.func_SendSQL(dbConn, "SELECT RuleText FROM ruleandregulation where Truck=2")
    Rule_List = func_cleanData(db_Rule_List)
    # For loop to replace the enter chara with HTML tag and clear some unwanted chars
    for i in range(0, len(Rule_List)):
        tempstr = str(Rule_List[i])
        tempstr = tempstr.replace("\\r\\n", "<br> - ")
        tempstr = tempstr.replace("Â»", " ")
        Rule_List[i] = tempstr

    # ------------------------------------------------
    # Espical Rule request
    Spasfic_Rule = []
    # Check if any thing was passed
    if request.method == 'POST':
        # Perpear the SQL
        theSQL = "SELECT `RuleText` FROM `ruleandregulation` WHERE `Truck`=%(TruckType)s AND `License`=%(LicenseType)s"
        # Prepear the Paramters
        parameters = {"TruckType":request.POST['Truck'], "LicenseType":request.POST['License']}
        # Send the SQL
        db_Spasifci_List = db.func_SendSQL(myDBin=dbConn, SQLStatment=theSQL, parameters=parameters)
        # Check the sql reuslts
        if type(db_Rule_List) is not Err:
            # No error, clean data
            Spasfic_Rule = func_cleanData(db_Spasifci_List)
            # For loop to replace the enter chara with HTML tag and clear some unwanted chars
            for i in range(0, len(Spasfic_Rule)):
                tempstr = str(Spasfic_Rule[i])
                tempstr = tempstr.replace("\\r\\n", "<br> - ")
                tempstr = tempstr.replace("Â»", " ")
                Spasfic_Rule[i] = tempstr

    dbConn.close()



    # Runder the final result
    return render(request, "VicRules.html",{"TruckTypes" : truck_types, "LicenseTypes" : License_types, \
                                            "RuleList" : Rule_List, "SpasficRules": Spasfic_Rule })

# This is just a help funcion for the rule() funcion
# It is used for cleaning data from extra staff that database add to its result array
def func_cleanData(inData, StaticDataIn=[]):

    # Clean the income data
    for i in range(0, len(inData)):
        StaticDataIn.append(str(inData[i][0]).strip())

    return StaticDataIn