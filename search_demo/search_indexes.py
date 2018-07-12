# _*_ coding: utf-8 _*_
from haystack import indexes
from .models import UserProfile, Event

class SearchIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return UserProfile

    def index_queryset(self, using=None):
        return self.get_model().objects.all()