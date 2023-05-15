from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('arac-olustur', views.arac_olustur, name="arac_olustur"),
    path('arac-listele', views.arac_listele, name="arac_listele"),
    path('arac-duzenle/<int:id>', views.arac_duzenle,name="arac_duzenle"),
    path('arac-sil/<int:id>', views.arac_sil,name="arac_sil"),
    path('upload', views.upload, name="upload_image"),
    path('<slug:slug>', views.details, name="arac_details"),
    path('kategori/<slug:slug>', views.arac_marka_getir, name='arac_marka_getir'),
    path('calisanlar/', views.calisanlar, name='calisanlar'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),

]
