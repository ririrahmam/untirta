"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from faperta.views import Faperta
from feb.views import Feb
from fh.views import Fh
from fisip.views import Fisip
from fk.views import Fk
from fkip.views import Fkip
from ft.views import Ft
from pascasarjana.views import Pascasarjana
from profil.views import Profil
from faperta.views import hapus_dosen, hapus_mahasiswa, hapus_staf, tambah_dosen, tambah_mahasiswa, tambah_staf, ubah_dosen, ubah_mahasiswa, ubah_staf
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', Faperta, name="faperta"),
    path('feb/', Feb, name="feb"),
    path('fh/', Fh, name="fh"),
    path('fisip', Fisip, name="fisip"),
    path('fk', Fk, name="fk"),
    path('fkip', Fkip, name="fkip"),
    path('ft', Ft, name="ft"),
    path('pascasarjana', Pascasarjana, name="pascasarjana"),
    path('profil', Profil, name="profil"),
    path('', views.index),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('tambah-staf/', tambah_staf, name='tambah_staf'),
    path('staf/ubah/<int:id_staf>', ubah_staf, name='ubah_staf'),
    path('staf/hapus/<int:id_staf>', hapus_staf, name='hapus_staf'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
]
