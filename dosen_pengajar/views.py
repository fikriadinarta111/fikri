from django.shortcuts import render, redirect, get_object_or_404
from .forms import DosenPengajarForm
from .models import DosenPengajarModel
from django.contrib import messages


def pengajar(request):
    context = {
        'title': 'Dosen Pengajar',
        'pengajar_list': DosenPengajarModel.objects.all()
    }
    return render(request, 'pengajar.html', context)


def edit_pengajar(request, pk):
    pengajar = get_object_or_404(DosenPengajarModel, pk=pk)

    if request.method == 'POST':
        form = DosenPengajarForm(
            request.POST, request.FILES, instance=pengajar)
        if form.is_valid():
            form.save()
            return redirect('dosen_pengajar')
    else:
        form = DosenPengajarForm(instance=pengajar)

    # Konteks untuk halaman edit_mahasiswa.html
    context = {
        'title': 'Dosen Pengajar',
        'form': form,
    }

    return render(request, 'edit_pengajar.html', context)


def hapus_pengajar(request, pk):
    pengajar = get_object_or_404(DosenPengajarModel, pk=pk)

    if request.method == 'POST':
        pengajar.delete()
        messages.success(
            request, f'Dosen pengajar "{pengajar.nama}" berhasil dihapus.')
        return redirect('dosen_pengajar')  # Redirect to the 'mahasiswa' view

    return render(request, 'hapus_pengajar.html', {'pengajar': pengajar})


def tambah_pengajar(request):
    if request.method == 'POST':
        form = DosenPengajarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_mahasiswa' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('dosen_pengajar')
    else:
        form = DosenPengajarForm()

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Dosen Pengajar',
        'form': form,
    }
    return render(request, 'tambah_pengajar.html', context)
