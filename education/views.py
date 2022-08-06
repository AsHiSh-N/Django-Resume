from django.shortcuts import render

# Create your views here.
def skills(request):
    sk1 = {'skill': 'active'}
    return render(request, 'education/skills.html', sk1)