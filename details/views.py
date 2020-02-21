from django.shortcuts import render, get_object_or_404
from .models import profile
def pro(request, user_id):
    prolist = get_object_or_404(profile, pk=user_id)
    context = {
        'prolist': prolist,
    }
    return render(request, 'profile.html', context)