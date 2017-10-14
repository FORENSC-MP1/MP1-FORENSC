
from django.shortcuts import render, get_object_or_404,redirect
from .models import Filesig, information
from .forms import infoForm

# This is the sample tutorial created during FORENSC class AY1718 of DLSU CCS CT
from queue import Queue
import time
from threading import Thread
import os
import sys

os.system('cls') # Clear Screen
q = Queue(10)
import threading


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
            all_filesigs = Filesig.objects.all()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #insert the data carve function
        print("CARVE ME")
        informData = information.objects.all()
        return render(request, 'datacarver/carvermenu.html', {'informData': informData, })

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

def carverMenu(request):

    return render(request, 'datacarver/carvermenu.html',context)

def worker():
    while True:
        #print("Waiting for image\n")
        item = q.get()
        #print("get Item\n")
        if item is None:
            q.task_done()
            break
        #print("PROCESSING ",item[4],"\n")
        save(item[0],item[1],item[2],item[3],item[4])
        q.task_done()
	
def save(startfile, size, imagectr, pathtosave,filetype):
    image = open(pathtosave+":\\"+filetype.replace(".","")+"\\" + str(imagectr) + filetype,"wb")
    drive.seek(startfile)
    image.write(drive.read(size))
    image.close()
    
def carverMain(request):
    informData = information.objects.last()
    filetocarve = Filesig.objects.filter(status="1")
    for file in filetocarve:
        print(file.filetype)
    print(informData.dircopy,informData.dirsave)
    
    try:
        path = informData.dircopy
        pathtosave = informData.dirsave
        drive = open("\\\\.\\"+path+":", 'rb') # opens the drive D folder in windows. Use /dev/sdb for linux and /dev/disk1 for Mac
        newpath = pathtosave+":\\jpg" #pathtosave+":\\"+ filetype.replace(".", "")
        if not os.path.isdir(newpath):
            os.mkdir(newpath)
        
            
        
    except KeyboardInterrupt:
        print ("Program interrupted. Ctrl+C pressed. Exiting.")
        sys.exit()
    except IOError as e:
        print(e)
        sys.exit()
    print("HELasddasdaO")
    return render(request, 'datacarver/carvermain.html')