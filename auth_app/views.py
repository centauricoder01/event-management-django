from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "Login successful!")
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'auth_app/login.html')

def signupUser (request):
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])  # Hash the password
                user.save()
                return JsonResponse({'success': True, 'message': 'Signup successful!'})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            form = SignupForm()
            
        return render(request, 'auth_app/signup.html',  {'form': form})

def logoutUser(request):
    return "User logout"