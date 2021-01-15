from django.urls import path
from .views import *
app_name="priceapp"

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('contact/', ContactView.as_view(), name= 'contact'),
  path('about/', AboutView.as_view(), name='about'),
  path('categories/', CategoriesView.as_view(), name='categories'),
  path('product/<slug:slug>/', ProductDetailView.as_view(), name='productdetail')

]
