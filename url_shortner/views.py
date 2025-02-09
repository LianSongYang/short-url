from django.shortcuts import render

def short_url_view(request):
    return render(request, "shorturl.html")
