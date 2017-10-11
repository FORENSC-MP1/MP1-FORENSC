
from django.shortcuts import render, get_object_or_404,redirect
from .models import Filesig, information
from .forms import infoForm


def index(request):
    all_filesigs = Filesig.objects.all()
    delete_id = None
    selectfileid = None
    deletefilesig = None
    filesig_id = None
    selectfile = None

    if request.method == 'GET':
        filesig_id = request.GET.get('filesigid')
        delete_id = request.GET.get('Yes')
        selectfileid = request.GET.get('selectfileid')
        print("HI",selectfileid)
    if filesig_id != None:
        deletefilesig = get_object_or_404(Filesig, pk=filesig_id)

    if delete_id != None:
        deletefilesig = get_object_or_404(Filesig, pk=delete_id)
        deletefilesig.delete()
        return redirect("/datacarver/")
    if selectfileid != None:
        selectfile = get_object_or_404(Filesig, pk=selectfileid)



    context = {
        'all_filesigs': all_filesigs,
        'deletefilesig': deletefilesig,
        'selectfile': selectfile,

    }
    return render(request, 'datacarver/index.html', context)


def detail(request, filesig_id):
    filesig = get_object_or_404(Filesig,pk=filesig_id)
 
    return render(request, 'datacarver/filesigdetail.html', {'filesig':filesig})


def recover(request):
    filecarve = []

    form = infoForm(request.POST or None)
    if 'file' in request.POST:
        filecarve =  request.POST.getlist('file')

        #for fileid in filecarve:



    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    allfilesigs = Filesig.objects.all()
    context = {'allfilesigs':allfilesigs,
               'form': form,
               }
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

    return redirect("/datacarver/")


