import graphene
from graphene_django import DjangoObjectType
from .models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'phone', 'email')


class Query(graphene.ObjectType):

    all_profile = graphene.List(ProfileType)

    def resolve_all_profile(root, info):
        return Profile.objects.all()

schema = graphene.Schema(query=Query)