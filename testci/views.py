from django.http import HttpResponse

def index(request):
    text = """<h1>Jessicus</h1>"""
    return HttpResponse(text)