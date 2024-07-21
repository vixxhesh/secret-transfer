from django.shortcuts import render, get_object_or_404
from .forms import FileUploadForm, UniqueCodeForm
from .models import FileUpload
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'transfer/home.html')

def send_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = form.save()
            return render(request, 'transfer/send_success.html', {'unique_code': file_upload.unique_code})
    else:
        form = FileUploadForm()
    return render(request, 'transfer/send.html', {'form': form})

def receive_file(request):
    if request.method == 'POST':
        form = UniqueCodeForm(request.POST)
        if form.is_valid():
            unique_code = form.cleaned_data['unique_code']
            files = FileUpload.objects.filter(unique_code=unique_code)
            return render(request, 'transfer/receive_success.html', {'files': files})
    else:
        form = UniqueCodeForm()
    return render(request, 'transfer/receive.html', {'form': form})