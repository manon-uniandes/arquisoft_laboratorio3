from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:id>/', views.get_measurement, name='uniqueMeasurement'),
    path('delete/<int:id>/', views.del_measurement, name='deleteMeasurement'),
    path('modify/<int:id>/<slug:entry>/', views.mod_measurement, name='modifyMeasurement'),
]