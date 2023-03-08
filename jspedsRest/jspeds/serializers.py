from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import models
from .models import Application, PatAppCrossRef

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CrossRefSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = PatAppCrossRef
        fields = ['app_no', 'publication_number', 'patent_number']

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['app_no',  
                'peds_date',
                'filing_date',  
                'art_unit',  
                'examiner',  
                'first_inventor', 
                'entity_category',   
                'conf_no', 
                'app_status', 
                'app_status_date', 
                'file_loc',  
                'title',  
                'fitf',  
                'app_type',  
                'applicant_ref',  
                'applicant',  
                'assignee',  
                'law_firm_name',  
                'publication_number',  
                'publication_date',  
                'patent_number',  
                'grant_date', 
                'pta_amount',  
                'terminal_disclaimer',  
                'continuing_app',  
                'related_for',  
                'ipOfficeCode',  
                'nationalSubclass',  
                'nationalClass',  
                'law_firms',  
                'practitioners',  
                'inventors',  
                'metadata',  
                'pros_hist',  
                'pta_bag',  
                'assignment',  
                'content']