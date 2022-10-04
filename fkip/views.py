from multiprocessing import context
from re import S
from telnetlib import DO
from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def Fkip(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip.html', context)