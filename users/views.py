from django.shortcuts import render, redirect

#flash messages -> message.warning, message.error
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm


#Creating a register view
def register(request):
    
    #Form submitted as post request? (ie - will data be posted to db?)
    if request.method == 'POST':

        #Create a new registration form, POST data
        form = UserRegisterForm(request.POST)

        #Is the form valid? Back end checks. Handled by UserCreation
        if form.is_valid():

            #Save the user
            form.save()
            username = form.cleaned_data.get('username')

            #flash message
            messages.success(request, f'Account created for {username}! Please log in!')

            #redirect to login so the user can log in
            return redirect('login')
    
    #Return form on failure 
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


