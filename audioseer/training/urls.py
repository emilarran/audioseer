from django.urls import path
from training import views

urlpatterns = [
    # path('', views.ReadFromDataSetView.as_view(), name='read-from-data-set'),
    path('neuralnetwork', views.TrainingView.as_view(), name='neuralnetwork'),
]
