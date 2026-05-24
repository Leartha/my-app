from django.urls import path
from . import views

urlpatterns = [
    path("ballots/", views.ballot_list, name="ballot-list"),
    path("ballots/<int:pk>/", views.ballot_detail, name="ballot-detail"),
    path("ballots/<int:pk>/vote/", views.cast_vote, name="cast-vote"),
    path("ballots/<int:pk>/results/", views.ballot_results, name="ballot-results"),
]
