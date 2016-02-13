from django.views import generic
from django.shortcuts import render


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


def faq(request):
	return render(request, "faq.html", {})


def term(request):
	return render(request, "term.html", {})
