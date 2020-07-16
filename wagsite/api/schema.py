from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType

from api import graphene_wagtail

from home.models import HomePage

from django.db import models


class ArticleNode(DjangoObjectType):
    class Meta:
        model = HomePage
        only_fields = ['id', 'banner_title',
                       'banner_subtitle', 'banner_image', 'banner_cta']


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleNode)

    @graphene.resolve_only_args
    def resolve_articles(self):
        return HomePage.objects.live()


schema = graphene.Schema(query=Query)
