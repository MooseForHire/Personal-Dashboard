from django.shortcuts import render, redirect

#flash messages -> message.warning, message.error
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#Register view
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



#Login
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)


