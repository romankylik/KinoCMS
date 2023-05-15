from django.shortcuts import render

# Create your views here.
def baners(request):
    context = {
        'title': "Baners",
    }
    return render(request, 'frontend/index.html', context=context)
