from django.urls import path
from .views import firstfunc, loginfunc, signupfunc, signupfin, loginfin, listfunc, baseshowfunc, logoutfunc, propeditfunc


urlpatterns = [
    path('first/', firstfunc, name='first'),
    path('login/', loginfunc, name='login'),
    path('signup/', signupfunc, name='signup'),
    path('signupfin/', signupfin, name='signupfin'),
    path('loginfin/', loginfin, name='loginfin'),
    path('list/', listfunc, name='list'),
    path('baseshow/', baseshowfunc, name='baseshow'),
    path('logout/', logoutfunc, name='logout'),
    path('propedit/', propeditfunc, name='propedit'),
]
