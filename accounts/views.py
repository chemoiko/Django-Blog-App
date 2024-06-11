from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
     form = UserCreationForm(request.POST)
     if form.is_valid():        #checking if form is valid
         form.save()        #if so save, the details to the database
         return redirect('articles:list')      #then redirect user to article list page
     else:
        print(form.errors) 
    else:
         form = UserCreationForm()      #else for the get request return fresh form
     
    return render(request, 'accounts/signup.html', {'form':form})       #this is sending the form to the base layout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user
            return redirect('articles:list')
    else:
         form = AuthenticationForm()      #else for the get request return fresh form
     
    return render(request, 'accounts/login.html', {'form':form})       #this is sending the form to the base layout

