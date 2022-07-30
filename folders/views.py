from django.shortcuts import render, redirect, get_object_or_404
from folders.forms import FoldersForm
from folders.models import Folders

def index(request):
    return render(request, 'folders/index.html')

def about(request):
    return render(request, 'folders/about.html')

def base(request):
    return render(request, 'folders/base.html')

def folderR(request):
    folder = Folders.objects.filter(title = 'Р')
    return render(request, 'folders/folderR.html', {'folder': folder})

def folderI(request):
    folder = Folders.objects.filter(title = 'И')
    return render(request, 'folders/folderI.html', {'folder': folder})

def folderD(request):
    folder = Folders.objects.filter(title = 'Д')
    return render(request, 'folders/folderD.html', {'folder': folder})

def folderDCH(request):
    folder = Folders.objects.filter(title= 'ДЧ')
    return render(request, 'folders/folderDCH.html', {'folder': folder})

def folderU(request):
    folder = Folders.objects.filter(title = 'У')
    return render(request, 'folders/folderU.html', {'folder': folder})

def create(request):
    error = " "
    if request.method == 'POST':
        form = FoldersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Ошибка, вы ввели неправильные данные, попробуйте ещё раз'
    form = FoldersForm()
    context = {'error': error, 'form': form}
    return render(request, 'folders/create.html', context)


def detail(request, folders_id):
    folder = get_object_or_404(Folders, pk= folders_id)
    return render(request, 'folders/detail.html', {'id': folders_id, 'folder': folder})

def delete(request, folders_id):
    folder = get_object_or_404(Folders, pk = folders_id)
    if request.method == "POST":
        folder.delete()
        return redirect('index')


  