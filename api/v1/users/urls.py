from django.urls import path, include, re_path
from graphene_django.views import GraphQLView
from users.schema import schema
from . import views

app_name = "api_v1_users"

urlpatterns= [
    re_path(r"^graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    re_path(r"^enter/details", views.signup_enter_details),
    
]