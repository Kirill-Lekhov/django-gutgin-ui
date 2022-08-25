from gutginm.views import GeneratorsView

from django.urls import path


urlpatterns = [
	path('generators', GeneratorsView.as_view(), name='generators')
]
