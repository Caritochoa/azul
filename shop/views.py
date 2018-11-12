from django.shortcuts import render

# Create your views here.


def index_call(request):
	return render(request, "index.html", {})


def grilla_call(request):
	return render(request, "grilla.html", {})


def contacto_call(request):
	return render(request, "contacto.html", {})

def detalle_call(request):
	return render(request, "detalle.html", {})




