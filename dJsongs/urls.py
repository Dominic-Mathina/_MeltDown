"""dJsongs URL Configuration

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users.forms import myAuthenticationForm
from django.urls import path, include
from users.views import dejay_view, reveler_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('songr.urls')),
	path('api/plist/', include('songr.api.urls')),
	path('dejay/', dejay_view.DejaySignUpView.as_view(), name = 'dejay_signup'),
	path('signup/', dejay_view.SignUpView.as_view(), name = 'all_signup'),
	path('accounts/login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
	path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name = 'logout'),
	path('reveler/', reveler_view.RevelerSignUpView.as_view(), name = 'reveler_signup'),
	#path('profile/', dejay_view.upload_song, name = 'dj_profile'), 
]
#, kwargs={'authentication_form': myAuthenticationForm}
# only adding media dir when in DEBUG mode
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
