from django.shortcuts import render, HttpResponse

# def index(request):
#     return HttpResponse("placeholder to display a list of all blogs")
# # Create your views here.

def create(request):
    return redirect('/')

# def show(request, number):
#     return HttpResponse(f"placeholder to display blog number {number}.")

# def edit(request, number):
#     return HttpResponse(f"placeholder to edit blog {number}.")

# def destroy(request, number):
#     return redirect('/')

def index(request):
    return render(request, "index.html")

def seindu(request):
    return HttpResponse("Hello Seindu")

def hello_name(request, name):
    context = {
        "htmlname": name
    }
    return render(request, "helloname.html", context)