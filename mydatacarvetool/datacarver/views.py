from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Filesig
from django.template import loader

def index(request):
    all_filesigs = Filesig.objects.all()
    context = {
        'all_filesigs': all_filesigs,
    }
    return render(request, 'datacarver/index.html', context)


def detail(request, filesig_id):
    try:
        filesig = Filesig.objects.get(pk=filesig_id)

    except Filesig.DoesNotExist:
        raise Http404("File Signature does not exist")

    return render(request, 'datacarver/filesigdetail.html', {'filesig':filesig})


def recover(request):
    all_filesigs = Filesig.objects.all()
    context = {'all_filesigs':all_filesigs}
    return render(request, 'datacarver/recover.html', context)