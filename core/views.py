from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def Contact(request):
    cn1 = {'contact': 'active'}
    return render(request, 'core/Contact.html', cn1)
    