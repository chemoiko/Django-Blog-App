from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm


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

