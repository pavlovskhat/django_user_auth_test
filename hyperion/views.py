from django.shortcuts import render
from . models import Band
from django.contrib.auth.decorators import login_required


def home(request):
	all_blogs = Band.objects.all()
	return render(
		request,
		"hyperion/home.html",
		{"blogs": all_blogs}
	)


def about(request):
	return render(request, "hyperion/about.html")


@login_required()
def blog(request, pk):
	selected_blog = Band.objects.get(pk=pk)
	return render(
		request,
		"hyperion/blog.html",
		{"blog": selected_blog}
	)
