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
        if request.POST['passIn'] == 'AustruckMA14':
            # Password was correct, display the main page
            global accessOK
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

    # ------------------------------------------------
    # General Rules list extraction
    generalRulesResult = db.func_SendSQL(dbConn, "SELECT RuleText, SignPictureURL FROM ruleandregulation where Truck=1")
    if type(generalRulesResult) is not Err:
        Rule_List = func_GeneralRules(generalRulesResult)
    else:
        Rule_List = ["NONE", ""]
    # ------------------------------------------------
    # Trucks types extraction form database to be added to the combobox
    db_truck_types = db.func_SendSQL(dbConn, "SELECT TypeName, ID FROM truckstype order by ID")
    if type(db_truck_types) is Err:
        db_truck_types = ["NONE"]

    # Create the truck types combobox items
    truck_types = []
    for i in range(0, len(db_truck_types)):
        if request.method == 'POST' and request.POST['Truck'] == str(db_truck_types[i][1]):
            truck_types.append("<option selected='selected' value='" + str(db_truck_types[i][1]) + "'>" + str(db_truck_types[i][0]) + "</option>")
        else:
            truck_types.append("<option value='"+ str(db_truck_types[i][1]) +"'>"+ str(db_truck_types[i][0]) +"</option>")

    # License Types extraction form database to be added to the combobox
    db_License_types = db.func_SendSQL(dbConn, "SELECT LicenseTypeName, LicenseTypeID FROM licensetype order by LicenseTypeID")
    if type(db_License_types) is Err:
        db_License_types = ["NONE"]

    # Create the License combobox items
    License_types = []
    for i in range(0, len(db_License_types)):
        if request.method == 'POST' and request.POST['License'] == str(db_License_types[i][1]):
            License_types.append("<option selected='selected' value='"+ str(db_License_types[i][1]) +"'>"+ str(db_License_types[i][0]) +"</option>")
        else:
            License_types.append("<option value='"+ str(db_License_types[i][1]) +"'>"+ str(db_License_types[i][0]) +"</option>")

    if request.method != 'POST':
        # Get request or empty POST, simply display the normal page with the form
        # Render the final result
        return render(request, "VicRulesSpacific.html", {"TruckTypes": truck_types, "LicenseTypes": License_types, \
                                                         "NormalRules": Rule_List})

    else:
        # request method is  'POST':

        # Check the match between Licence type and the truck type
        if (int(request.POST['License']) ==1 and int(request.POST['Truck']) > 2) or \
                (int(request.POST['License']) == 2 and int(request.POST['Truck']) > 3):
            db_Spasifci_List = ["<p style='color:Tomato;'> Your license level does not allow you to drive this type of cars!</p>", '']
        else:
            # Perpear the SQL for the user choice
            theSQL = "SELECT `RuleText`, SignPictureURL FROM `ruleandregulation` WHERE `Truck`<=%(TruckType)s AND `Truck`>1"
            # Prepear the Paramters
            parameters = {"TruckType":request.POST['Truck'], "LicenseType":request.POST['License']}
            # Send the SQL
            db_Spasifci_List = db.func_SendSQL(myDBin=dbConn, SQLStatment=theSQL, parameters=parameters)

            # Check the sql reuslts
            if type(db_Spasifci_List) is not Err:
                # No error, clean data
                db_Spasifci_List = func_GeneralRules(db_Spasifci_List)

            if db_Spasifci_List == []:
                db_Spasifci_List = ["No Specific rules was found", ""]

            dbConn.close()

        # Runder the final result
        return render(request, "VicRulesSpacific.html", {"SpasficRules": db_Spasifci_List, "NormalRules":Rule_List, \
                                                         "TruckTypes": truck_types, "LicenseTypes": License_types})

def func_GeneralRules(db_Rule_List):
    # General Rules list extraction
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

    HTML_rule = []

    for oneRule in db_Rule_List:
        #         <div class='card' style='width: 18rem;'>
        #             <img class='card-img-top' src='...' alt='Card image cap'>
        #             <div class='card-body'>
        #                 <h5 class='card-title'>Card title</h5>
        #                 <p class='card-text'>Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        #                 <a href='#' class='btn btn-primary'>Go somewhere</a>
        #             </div>
        #         </div>

        htmlRule = "<div class='card'><div class='card-body'>"

        # Check if the rule has an image
        if oneRule[1] != "" and oneRule[1] != None:
            # Add the picture src if it is there
            htmlRule = htmlRule + "<img src='" + str(oneRule[1]) + "'>"

        # Add the rule text in format
        htmlRule = htmlRule + "<p class='card-text'>&nbsp;&nbsp;" + oneRule[0] + "</p></div></div>"
        HTML_rule.append(htmlRule)

    return HTML_rule
