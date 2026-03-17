from django.shortcuts import render

def home_view(request):
    # This is like your FastAPI return, but it sends an HTML file
    return render(request, 'home.html')