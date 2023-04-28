from django.urls import path
from . import views

app_name = 'dinings'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.dining_create, name='dining_create'),
    path('create/<int:dining_pk>', views.dining_update, name='dining_update'),
    path('<int:dining_pk>/reviews/', views.review_create, name='review_create'),
    path('<int:dining_pk>/reviews/<int:review:pk>/', views.review_detail, name='review_detail'),
    path('<int:dining_pk>/reviews/<int:review:pk>/update/', views.review_update, name='review_update'),
]
