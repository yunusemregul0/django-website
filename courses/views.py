from datetime import date,datetime
from django.shortcuts import get_object_or_404, render
from .models import Course, Category
from django.core.paginator import Paginator

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page',1)
    courses = paginator.get_page(page)

    print(paginator.count)
    print(paginator.num_pages)

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': courses,
        'seciliKategori': slug
    })

