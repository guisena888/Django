from django.shortcuts import render
from .models import Professores, Area

# Create your views here.


def post_list(request):
	return render(request, 'blog/post_list.html',{})


def professores(request):
	professores = Professores.objects.all()
	area = Area.objects.all()
	return render(request, 'blog/professores.html', {
		'professores': professores,
		'area':area
	})
