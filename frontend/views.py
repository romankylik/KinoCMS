from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def baners(request):
    context = {
        'title': "Baners",
    }
    return render(request, 'frontend/index.html', context=context)
