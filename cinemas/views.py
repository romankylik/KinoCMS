from django.shortcuts import render
def index(request):
    context = {
        'title': "ADMIN Панель",
    }
    return render(request, 'cinemas/index.html', context=context)

def baners(request):
    context = {
        'title': "Baners",
    }
    return render(request, 'cinemas/index.html', context=context)





