from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f'Account is created for {username}')

    else:        
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

#def login(request):
    return render(request, 'accounts/login.html')

#def logout(request):
    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)    
