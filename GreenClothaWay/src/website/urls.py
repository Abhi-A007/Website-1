"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from account.views import (
    register_view,
    login_view,
    member_view,
    logout_view,
    profile_view,
    profile_edit_view,
    profile_inserations
)
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inseration.views import (
    insert_view,
)
from marketplace.views import (
    about_view,
    index_view,
    marketplace_view,
    cart_view
)

urlpatterns = [
    path(r'', lambda r: HttpResponseRedirect('index/')),
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('member/', member_view, name="member"),
    path('login/', login_view, name='login'),
    path('about-us/', about_view, name='about'),
    path('index/', index_view, name='index'),
    path('marketplace/', marketplace_view, name='marketplace'),
    path('shoppingcart/', cart_view, name='cart'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile/edit'),
    path('profile/messages/', include('django_messages.urls'), name="messages"),
    path('insert/', insert_view, name='insert'),
    path('profile/inserations/', profile_inserations, name='profile/inserations'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
