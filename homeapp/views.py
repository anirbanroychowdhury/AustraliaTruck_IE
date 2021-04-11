from django.shortcuts import render

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