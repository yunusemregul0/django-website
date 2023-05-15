from django.shortcuts import get_object_or_404, redirect, render
from araclar.forms import aracolustur, arabaduzenleme, UploadForm
from araclar.models import araclar, marka, UploadModel
from django.core.paginator import Paginator

import random
import os

def index(request):
    arac = araclar.objects.filter(isActive=1, isHome=1)
    markalar = marka.objects.all()

    return render(request, 'araclar/index.html', {
        'marka': markalar,
        'arac': arac,
    })

def arac_olustur(request):
    if request.method == "POST":
        form = aracolustur(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/araclar")
    else:
        form = aracolustur()
    return render(request, "araclar/arac-olustur.html", {"form":form})

def arac_listele(request):
    arac = araclar.objects.all()
    return render(request, 'araclar/arac-listele.html', {
        'arac': arac
    })

def arac_duzenle(request, id):
    arac = get_object_or_404(araclar, pk=id)

    if request.method == "POST":
        form = arac_duzenle(request.POST, request.FILES, instance=arac)
        form.save()
        return redirect("/arac-listele")
    else:
        form = arac_duzenle(instance=arac)

    return render(request, "araclar/arac-duzenle.html", { "form":form })

def arac_sil(request, id):
    arac = get_object_or_404(araclar, pk=id)

    if request.method == "POST":
        arac.delete()
        return redirect("/arac-listele")

    return render(request, "araclar/arac-sil.html", { "araclar":arac })

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request, "araclar/success.html")
    else:
        form = UploadForm()
    return render(request, "araclar/upload.html",{"form":form})


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        arac = araclar.objects.filter(isActive=True,title__contains=q).order_by("date")
        markalar = marka.objects.all()
    else:
        return redirect("/araclar")

    return render(request, 'araclar/search.html', {
        'marka': markalar,
        'arac': arac,
    })

def details(request, slug):
    arac = get_object_or_404(araclar, slug=slug)

    context = {
        'arac': arac
    }
    return render(request, 'araclar/details.html', context)

def arac_marka_getir(request, slug):  
    arac = araclar.objects.filter(marka__slug=slug, isActive=True).order_by("date")
    markalar = marka.objects.all()
        
    paginator = Paginator(arac, 3)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request, 'araclar/list.html', {
        'marka': markalar,
        'page_obj': page_obj,
        'seciliKategori': slug
    })

def calisanlar(request):
    return render(request, 'araclar/calisanlar.html')

def hakkimizda(request):
    return render(request, 'araclar/hakkimizda.html')