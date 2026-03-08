from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task
from .ai_engine import predict_duration, get_ai_subtasks

# --- AUTHENTICATION VIEWS ---

def register_view(request):
    """Allows new users to create an account and auto-logs them in."""
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        # Check if user already exists
        if User.objects.filter(username=u).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})
        
        user = User.objects.create_user(username=u, password=p)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')

def login_view(request):
    """Authenticates existing users."""
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'login.html')

def logout_view(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    return redirect('login')


# --- TASK MANAGEMENT VIEWS ---

@login_required(login_url='login')
def dashboard(request):
    """
    Displays the list of tasks. 
    Currently shows all tasks; can be filtered by user later.
    """
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'tasks': tasks})

@login_required(login_url='login')
def create_task(request):
    """
    The heart of the app: 
    1. Collects user input.
    2. Calls ML model for duration prediction.
    3. Calls Gemini API for sub-task generation.
    4. Saves to SQLite database.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        complexity = int(request.POST.get('complexity'))

        # --- AI ENGINE INTERACTION ---
        
        # 1. Scikit-learn: Predict hours based on complexity (1-5)
        predicted_hrs = predict_duration(complexity)
        
        # 2. Gemini API: Generate 3 technical steps
        ai_steps = get_ai_subtasks(title)

        # Save to Database
        Task.objects.create(
            title=title,
            description=description,
            complexity=complexity,
            estimated_hours=predicted_hrs,
            sub_tasks=ai_steps
        )
        return redirect('dashboard')

    return render(request, 'create_task.html')