from django.http import HttpResponse

def index(request):
    text = """<h1>cucucs</h1>"""
    return HttpResponse(text)