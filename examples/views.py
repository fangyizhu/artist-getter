from django.views.generic.base import View
from django.http import HttpResponse
from ..artist_getter import *
import json

class GetUlanView(View):
	def get(self, request):

		artist_ulan = json.dumps(get_getty_ulan(u"Stieglitz, Alfred"))

		return HttpResponse(artist_ulan, content_type="application/json")

class GetArtistRelationshipsView(View):
	def get(self, request):

		artist_relationships = json.dumps(get_getty_relationship("500024301"))

		return HttpResponse(artist_relationships, content_type="application/json")

class GetArtistNameView(View):
	def get(self, request):

		artist_relationships = json.dumps(get_getty_artist_name("500024301"))

		return HttpResponse(artist_relationships, content_type="application/json")