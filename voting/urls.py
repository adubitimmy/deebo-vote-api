from django.conf.urls import url
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views
from rest_framework_swagger.views import get_swagger_view
from .apiviews import CreateCandidates
from .apiviews import CandidateDetail, CandidateList, CandidateUpdate, DeleteCandidate
from .apiviews import CreateVote, VoteDetail, VoteList, VoteUpdate, DeleteVote
from .apiviews import CreateRequestForm, RequestFormDetail, RequestFormList, RequestFormUpdate, DeleteRequestForm


app_name = 'DeeboVoting'

schema_view = get_swagger_view(title="EventHost API")

urlpatterns = [
    # Candidate urls
    path("create-candidate/", CreateCandidates.as_view(), name="create-candidate"),
    path("list-candidate/", CandidateList.as_view(), name="list-candidate"),
    path("candidate-detail/<int:pk>/", CandidateDetail.as_view(), name="candidate-detail"),
    path("candidate-update/<int:pk>/", CandidateUpdate.as_view(), name="candidate-update"),
    path("candidate-delete/<int:pk>/", DeleteCandidate.as_view(), name="candidate-delete"),
    
    # Vote urls 
    path("create-vote/", CreateVote.as_view(), name="create-vote"),
    path("list-candidate/", VoteList.as_view(), name="list-vote"),
    path("vote-detail/<int:pk>/", VoteDetail.as_view(), name="vote-detail"),
    path("vote-update/<int:pk>/", VoteUpdate.as_view(), name="vote-update"),
    path("vote-delete/<int:pk>/", DeleteVote.as_view(), name="vote-delete"),
    
    # FormRequest urls 
    path("create-form-request/", CreateRequestForm.as_view(), name="create-vote"),
    path("list-form-requst/", RequestFormList.as_view(), name="list-form-request"),
    path("form-request-detail/<int:pk>/", RequestFormDetail.as_view(), name="form-request-detail"),
    path("form-request-update/<int:pk>/", RequestFormUpdate.as_view(), name="form-request-update"),
    path("form-request-delete/<int:pk>/", DeleteRequestForm.as_view(), name="form-request-delete"),
    
    path(r'swagger-docs/', schema_view),
    
]
