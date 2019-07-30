from django.contrib import admin
from django.urls import path, include

from myapp.views.CreateUserView import CreateUserView
from myapp.views.authenticate_user import authenticate_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', authenticate_user),
    path('auth/registration/', CreateUserView.as_view()),
    path('', include('myapp.urls'))
]
