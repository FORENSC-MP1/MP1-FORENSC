from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Filesig, information
from django.template import loader

def index(request):
    all_filesigs = Filesig.objects.all()
    context = {
        'all_filesigs': all_filesigs,
    }
    return render(request, 'datacarver/index.html', context)


def detail(request, filesig_id):
    filesig = get_object_or_404(Filesig,pk=filesig_id)
 
    return render(request, 'datacarver/filesigdetail.html', {'filesig':filesig})


def recover(request):
    all_filesigs = Filesig.objects.all()
    context = {'all_filesigs':all_filesigs}
    return render(request, 'datacarver/recover.html', context)

def addfile(request):
    trail=''
    if 'header' in request.POST:
        head = request.POST['header']
        
    if 'trailer' in request.POST:
        trail = request.POST['trailer']
        
    if 'filetype' in request.POST:
        ftype = request.POST['filetype']
        
    Filesig.objects.create(header=head, trailer=trail, filetype=ftype)   
        
    all_filesigs = Filesig.objects.all()
    context = {
        'all_filesigs': all_filesigs,
    }
    return render(request, 'datacarver/index.html', context)
def deletefile(request):
    
    filesig = get_object_or_404(Filesig,pk=filesig_id)
    filesig.delete()
    prevhttp = request.META.get('HTTP_REFERER')
    prevhttp.split("?")[0]
    return HttpResponseRedirect(prevhttp.split("?")[0])