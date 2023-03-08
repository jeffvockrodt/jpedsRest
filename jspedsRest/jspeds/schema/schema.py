from graphql_jwt.decorators import login_required
from graphql_jwt import ObtainJSONWebToken, Verify, Refresh
from graphene_django import DjangoObjectType
import graphene
from jspeds.models import Application 
from jspeds.serializers import AppSerializer
import json

def strip(query): 
    query=query.replace(' ', '')
    query=query.replace('-', '')
    query=query.replace(',', '')
    query=query.replace('/', '')
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

class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application
        fields = '__all__'
        
class Query(graphene.ObjectType): 
    app_data = graphene.List(ApplicationType, app_no=graphene.String())

    @login_required
    def resolve_app_data(root, info, **kwarg):
        app_no=app_validate(kwarg.get('app_no'))
        queryset = Application.objects.raw("SELECT * FROM peds WHERE app_no=%s", [app_no])
        # print(queryset)
        return queryset

    pat_data = graphene.List(ApplicationType, pat_no=graphene.String())
    
    @login_required
    def resolve_pat_data(root, info, **kwarg):
        pat_no=pat_validate(kwarg.get('pat_no'))
        queryset = Application.objects.raw("SELECT * FROM peds WHERE patent_number=%s", [pat_no])
        # print(queryset)
        return queryset

    pub_data = graphene.List(ApplicationType, pub_no=graphene.String())
    
    @login_required
    def resolve_pub_data(root, info, **kwarg):
        pub_no=pub_validate(kwarg.get('pub_no'))
        queryset = Application.objects.raw("SELECT * FROM peds WHERE publication_number=%s", [pub_no])
        # print(queryset)
        return queryset


schema = graphene.Schema(query=Query)



        # fields = ('app_no',  
        #         'peds_date',
        #         'filing_date',  
        #         'art_unit',  
        #         'examiner',  
        #         'first_inventor', 
        #         'entity_category',   
        #         'conf_no', 
        #         'app_status', 
        #         'app_status_date', 
        #         'file_loc',  
        #         'title',  
        #         'fitf',  
        #         'app_type',  
        #         'applicant_ref',  
        #         'applicant',  
        #         'assignee',  
        #         'law_firm_name',  
        #         'publication_number',  
        #         'publication_date',  
        #         'patent_number',  
        #         'grant_date', 
        #         'pta_amount',  
        #         'terminal_disclaimer',  
        #         'continuing_app',  
        #         'related_for',  
        #         'ipOfficeCode',  
        #         'nationalSubclass',  
        #         'nationalClass',  
        #         'law_firms',  
        #         'practitioners',  
        #         'inventors',  
        #         'metadata',  
        #         'pros_hist',  
        #         'pta_bag',  
        #         'assignment',  
        #         'content')




