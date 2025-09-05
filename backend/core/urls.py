"""
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
from django.urls import path
from .healthz import healthz




from django.http import JsonResponse
def hello(request):
    return JsonResponse({"message": "Testing API, testing 1 2 3"})





urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz', healthz),
    path("api/hello/", hello),
]
