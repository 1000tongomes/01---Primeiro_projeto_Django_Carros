from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def cars_view(request):
    html = '''
    <html>
        <head>
            <title> Meus carros </title>
        </head>
        <body>
            <h1>Carros da PycodeBr</h1>
             <h3>Só carro top!</h3>
        </body>
    </html>
'''
    return HttpResponse(html)