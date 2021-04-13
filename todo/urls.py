
from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.TaskListView.as_view(), name='list'),
    path('add/', views.TaskCreateView.as_view(), name='add'),
    path('<pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
]
