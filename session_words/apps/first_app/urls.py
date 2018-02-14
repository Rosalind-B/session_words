from django.conf.urls import url
import views

urlpatterns = [
    url(r'^session_words/', views.index),
    url(r'^session_words/post_word', views.post_word),
    # url(r'^session_words/add_word', views.process),  
]