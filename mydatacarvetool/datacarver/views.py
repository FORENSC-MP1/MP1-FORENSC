
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
    editid = None
    editfile = None

    if request.method == 'GET':
        filesig_id = request.GET.get('filesigid')
        delete_id = request.GET.get('Yes')
        selectfileid = request.GET.get('selectfileid')
        editid = request.GET.get('editid')
    if filesig_id != None:
        deletefilesig = get_object_or_404(Filesig, pk=filesig_id)

    if delete_id != None:
        deletefilesig = get_object_or_404(Filesig, pk=delete_id)
        deletefilesig.delete()
        return redirect("/datacarver/")
    if selectfileid != None:
        selectfile = get_object_or_404(Filesig, pk=selectfileid)
    if editid != None:
        editfile = get_object_or_404(Filesig, pk=editid)



    context = {
        'all_filesigs': all_filesigs,
        'deletefilesig': deletefilesig,
        'selectfile': selectfile,
        'editfile': editfile,

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

        for fileid in filecarve:
            filetocarve = get_object_or_404(Filesig, pk=fileid)
            filetocarve.status = 1
            filetocarve.save()

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



def editfile(request):

    trail = ''
    editid = None
    print("HI")
    if 'editid' in request.POST:
        editid = request.POST['editid']
        print(editid)
    if 'header' in request.POST:
        head = request.POST['header']
    if 'trailer' in request.POST:
        trail = request.POST['trailer']
    if 'filetype' in request.POST:
        ftype = request.POST['filetype']
        if editid != None:
            newfilesig = get_object_or_404(Filesig, pk=editid)
            newfilesig.header = head
            newfilesig.trailer = trail
            newfilesig.filetype = ftype
            newfilesig.save()
    return redirect("/datacarver/")

