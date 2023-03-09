import django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.db.models import RawSQL
# Create your views here.
from .models import Application, PatAppCrossRef
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from jspeds.serializers import UserSerializer, GroupSerializer, AppSerializer, CrossRefSerializer
from django.db import connection
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from graphql_jwt.decorators import login_required
from graphene_django.views import GraphQLView
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import mixins
from rest_framework.authentication import SessionAuthentication
from graphene_django.views import GraphQLView

from django.views.decorators.csrf import csrf_exempt
from django.views import View
from graphene_django.views import GraphQLView
from graphql.execution import ExecutionResult
from graphql import GraphQLError
from jspedsRest.schema import schema


def strip(query): 
    query=query.replace(' ', '')
    query=query.replace('-', '')
    query=query.replace(',', '')
    return query 

def pub_validate(pubNo): 
    pubNo = strip(pubNo)
    if 'US' not in str(pubNo):
        pubNo = 'US' + pubNo
    if 'A1' not in pubNo:
        pubNo = pubNo + 'A1'
    return pubNo

def pat_validate(patNo): 
    patNo = strip(patNo)
    return patNo

def app_validate(appNo): 
    appNo = strip(appNo)
    return appNo

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AppViewSet(viewsets.ModelViewSet): 
    model = Application
    serializer_class = AppSerializer

    @login_required
    def get_queryset(self):
        query = app_validate(self.kwargs['pk'])
        queryset = Application.objects.raw("SELECT * FROM peds WHERE app_no=%s", [query])
        serializer = AppSerializer(queryset, many=True)
        return serializer.data

class PatViewSet(viewsets.ModelViewSet): 
    model = Application
    serializer_class = AppSerializer

    @login_required
    def get_queryset(self): 
        query = pat_validate(self.kwargs['pk'])
        queryset = Application.objects.raw("SELECT * FROM peds WHERE patent_number=%s", [query])
        serializer = AppSerializer(queryset, many=True)
        return serializer.data

class PubViewSet(viewsets.ModelViewSet): 
    model = Application
    serializer_class = AppSerializer

    @login_required
    def get_queryset(self): 
        query = pub_validate(str(self.kwargs['pk']))
        queryset = Application.objects.raw("SELECT * FROM peds WHERE publication_number=%s", [query])
        serializer = AppSerializer(queryset, many=True)
        return serializer.data

class PatCrossRefViewSet(viewsets.ModelViewSet):
    model = PatAppCrossRef
    serializer_class = CrossRefSerializer

    @login_required
    def get_queryset(self): 
        query = pat_validate(self.kwargs['pk'])
        queryset = Application.objects.raw("SELECT * FROM peds WHERE patent_number=%s", [query])
        serializer = CrossRefSerializer(queryset, many=True)
        return serializer.data

class PubCrossRefViewSet(viewsets.ModelViewSet):
    model = PatAppCrossRef
    serializer_class = CrossRefSerializer
    
    @login_required
    def get_queryset(self): 
        query = pub_validate(str(self.kwargs['pk']))
        queryset = Application.objects.raw("SELECT * FROM peds WHERE publication_number=%s", [query])
        serializer = CrossRefSerializer(queryset, many=True)
        return serializer.data

def redirect_view(request):
    if request.user.is_authenticated:
        return redirect("/graphql")
    else:
        return redirect("/admin")
    
# class TokenLoginRequiredMixin(mixins.LoginRequiredMixin):

#     """A login required mixin that allows token authentication."""

#     def dispatch(self, request, *args, **kwargs):
#         """If token was provided, ignore authenticated status."""
#         http_auth = request.META.get("HTTP_AUTHORIZATION")

#         """Check for a passing JWT <token> in headers"""
#         if http_auth and "JWT" in http_auth:
#             pass

#         elif not request.user.is_authenticated:
#             return self.handle_no_permission()

#         return super(mixins.LoginRequiredMixin, self).dispatch(
#             request, *args, **kwargs)

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

#     """This view supports both token and session authentication."""

#     authentication_classes = [
#         SessionAuthentication,
#         ]

