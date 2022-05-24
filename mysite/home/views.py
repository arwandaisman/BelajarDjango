from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#    return HttpResponse("halaman home tanpa template")
#def index(req):
#    return render(req, 'home/index.html')

def about(req):
    return render(req, 'about/about.html')


def index(request):
	context = {
		'heading':'Home',
	}

	if request.method == 'POST':
		print("ini adalah method post")
		context['nama'] = request.POST['nama']
		context['alamat'] = request.POST['alamat']
	else:
		print("ini adalah method get")

	return render(request, 'home/index.html', context)