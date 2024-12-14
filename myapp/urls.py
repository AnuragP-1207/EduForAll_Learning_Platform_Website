from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),    
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('about', views.about, name='about'),
    path('tutorials', views.tutorials, name='tutorials'),
    path('tutorials2', views.tutorials2, name='tutorials2'),
    path('tutorials3', views.tutorials3, name='tutorials3'),
    path('tutorials4', views.tutorials4, name='tutorials4'),
    path('tutorials5', views.tutorials5, name='tutorials5'),
    path('tutorials6', views.tutorials6, name='tutorials6'),
    path('python', views.python, name='python'),
    path('django', views.django, name='django'),
    path('blog', views.blog, name='blog'),
    path('community', views.community, name='community'),
    path('courses', views.courses, name='courses'),
    path('contact', views.contact, name='contact'),
    path('quizes', views.quizes, name='quizes'),
    path('quizesdjango', views.quizesdjango, name='quizesdjango'),
    path('quizesdjangob', views.quizesdjangob, name='quizesdjangob'),
    path('quizesapi', views.quizesapi, name='quizesapi'),
    path('quizescs50', views.quizescs50, name='quizescs50'),
    path('quizesscipy', views.quizesscipy, name='quizesscipy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    
    # Add other URLs as needed

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)