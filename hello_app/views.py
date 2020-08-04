from django.shortcuts import render


# Create your views here.
def index_view(request):
    # context = {'text': "Hello World"}
    return render(request, 'index.html', {'text': "Hello World"})
