from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()

    return render(request, "MyApp1/index.html", {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        })

def about(request):
    return render(
        request,
        "MyApp1/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django",
        }
    )


# Create your views here.
#def index(request):
#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django!</title></head><body>"
#    html_content += "<strong>Hello, Django</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)

