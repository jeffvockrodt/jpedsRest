"""jspedsRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from jspeds import views
from jspeds.views import redirect_view, PrivateGraphQLView
from django.contrib import admin
from graphene_django.views import GraphQLView
from jspedsRest.schema import schema
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'app/(?P<app_no>.+)/$', views.AppViewSet, basename='app')

# router.register(r'app', views.render)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('app/<str:app_no>', views.render, name='app'),
    path('app/<str:pk>', views.AppViewSet.as_view({'get':'list'}), name='app'),
    # path('pat/<str:pk>', views.PatViewSet.as_view({'get':'list'}), name='pat'),
    # path('pub/<str:pk>', views.PubViewSet.as_view({'get':'list'}), name='pub'),
    # path('appfrompat/<str:pk>', views.PatCrossRefViewSet.as_view({'get':'list'}), name='pub'),
    # path('appfrompub/<str:pk>', views.PubCrossRefViewSet.as_view({'get':'list'}), name='pub'),    
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', redirect_view, name='index'),
    path('admin/', admin.site.urls),
    # path('api/', include('jspeds.api.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    # path('graphql/', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema)))
    # path('graphql/', csrf_exempt(MyGraphQLView.as_view(graphiql=True)), name='graphql')
]
