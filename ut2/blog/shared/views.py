from django.shortcuts import render


def shared_list(request):

    return render(request, 'index.html')
