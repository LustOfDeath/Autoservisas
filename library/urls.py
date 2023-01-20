from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis-detail'),
    path('uzsakymai/', views.UzsakymasListView.as_view(), name='uzsakymai'),
    path('uzsakymai/<uuid:pk>', views.UzsakymasDetailView.as_view(), name='uzsakymas-detail'),
    path('search/', views.search, name='search'),
]
