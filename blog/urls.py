from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.AllPostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('read-later/', views.ReadLaterView.as_view(), name='read-later')
]

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
