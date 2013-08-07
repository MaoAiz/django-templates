# Create your views here.
from django.shortcuts import render_to_response


def home(request):
	if request.method == "GET" and "m" in request.GET:
		template = request.GET.get("m")
	else:
		template = "menu1.html"
	return render_to_response(template)