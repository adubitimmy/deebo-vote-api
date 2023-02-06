from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.forms import EmailInput
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend

# swagger docs imports
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

# sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# filter modules

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters


# rest_framework module
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, serializers
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# custom module
from .models import Vote, Candidates, RequestForm
from .serializers import CandidatesSerializer, VoteSerializer, RequestFormSerializer
from voting.permissions import IsOwnerOrReadOnly

# file upload setup for apiviews
from rest_framework.parsers import MultiPartParser, FormParser

# from django rest passwordreset



# sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Using Logger
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

class CreateCandidates(APIView):
    parser_class = (MultiPartParser, FormParser)
    permission_classes = []
    authentication_classes = ()
    def post(self, request, format=None):
        req_input = (
            "candidates_name",
            "manifesto",
            "portfolio"
        )
        
        input_list_dict = request.data
        handler400 = f'All expected fields = {req_input}.'

        try:  # BASIC ASSERTION CHECKS TO ENSURE REQ FIELDS ARE SUPPLIED, AND NOT AS EMPTY
            for each in req_input:
                assert each in input_list_dict.keys(
                ), f' But {each} wasn\'t found!'
                assert input_list_dict[each] != [
                    ""], f" NO VALUE SUPPLIED FOR {each}!"
        except AssertionError as errAssert:
            return Response({"message":f"All expected fields {req_input}, but none was given "}, status=status.HTTP_400_BAD_REQUEST)

        
        new_candidate_serializer = CandidatesSerializer(
            data={
                "candidates_name":input_list_dict["candidates_name"],
                "manifesto":input_list_dict["manifesto"],
                "portfolio":input_list_dict["portfolio"],
            }
        )
        try:
            if new_candidate_serializer.is_valid(raise_exception=True):
                get_new_candidate = new_candidate_serializer.save()
                return Response(new_candidate_serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response({"message":new_candidate_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            handler400 = str(exc)
            return Response({"message":handler400}, status=status.HTTP_400_BAD_REQUEST)            
        

class CandidateDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = ()

    def get(self, request, pk):
        new_candidate = get_object_or_404(Candidates, pk=pk)
        data = CandidatesSerializer(new_candidate).data
        return Response(data)


class CandidateList(generics.ListAPIView):
    queryset = Candidates.objects.all().order_by('id')
    serializer_class = CandidatesSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filer_fields = ('id', 'candidates_name', 'manifesto')
    ordering_fields = ('id', 'candidates_name')
    ordering = ('id')
    search_fields = ('id', 'candidates_name', 'manifesto')
    

class CandidateUpdate(generics.UpdateAPIView):
    queryset = Candidates.objects.all().order_by('id')
    serializer_class = CandidatesSerializer


class DeleteCandidate(generics.DestroyAPIView):
    permission_class = [IsAuthenticated, ]
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer
    


class CreateVote(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    authentication_classes = ()
    def post(self, request, format=None):
        req_input = (
            "nationality",
            "location",
            "state_of_origin",
            "pvc_collected"
        )
        
        input_list_dict = request.data 
        handler400 = f'All expected fields ={req_input}'
        try:
            for each in req_input:
                assert each in input_list_dict.keys(
                ),f'but each wasn\'t found!'
                assert input_list_dict[each] !=[
                ""], f'NO VALUE SUPPLIED FOR {each}'
        except AssertionError as errAssert:
            return Response({"message":f"All expected fields {req_input}, but none was given "}, status=status.HTTP_400_BAD_REQUEST)
        
        new_vote_serializer = VoteSerializer(
            data={
                "nationality":input_list_dict["nationality"],
                "location":input_list_dict["location"],
                "state_of_origin":input_list_dict["state_of_origin"],
                "pvc_collected":input_list_dict["pvc_collected"]
            }
        )
        try:
            if new_vote_serializer.is_valid(raise_exception=True):
                get_new_vote_serializer = new_vote_serializer.save()
                return Response(new_vote_serializer.data, status=status.HTTP_201_CREATED)
        except AssertionError as errAssert:
            handler400 = {"message":"All fields were expected but none was supplied"}
            return Response(handler400, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            handler400 = str(exc)
            return Response({"message":handler400}, status=status.HTTP_400_BAD_REQUEST)

class VoteDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = ()

    def get(self, request, pk):
        new_candidate = get_object_or_404(Vote, pk=pk)
        data = VoteSerializer(new_candidate).data
        return Response(data)


class VoteList(generics.ListAPIView):
    queryset = Vote.objects.all().order_by('id')
    serializer_class = VoteSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filer_fields = ('id', 'location', 'state_of_origin','pvc_collected')
    ordering_fields = ('id', 'state_of_origin','location')
    ordering = ('id')
    search_fields = ('id', 'location', 'state_of_origin','pvc_collected')
    

class VoteUpdate(generics.UpdateAPIView):
    queryset = Vote.objects.all().order_by('id')
    serializer_class = VoteSerializer


class DeleteVote(generics.DestroyAPIView):
    permission_class = [IsAuthenticated, ]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CreateRequestForm(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    authentication_classes = ()
    def post(self, request, format=None):
        req_input = (
            "poll_category",
            "poll_title",
            "full_name",
            "email",
            "additional_information"
        )
        
        input_list_dict = request.data 
        handler400 = f'All expected fields ={req_input}'
        try:
            for each in req_input:
                assert each in input_list_dict.keys(
                ),f'but each wasn\'t found!'
                assert input_list_dict[each] !=[
                ""], f'NO VALUE SUPPLIED FOR {each}'
        except AssertionError as errAssert:
            return Response({"message":f"All expected fields {req_input}, but none was given "}, status=status.HTTP_400_BAD_REQUEST)
        
        new_new_request_form_serializer = RequestFormSerializer(
            data={
                "poll_category":input_list_dict["poll_category"],
                "poll_title":input_list_dict["poll_title"],
                "full_name":input_list_dict["full_name"],
                "email":input_list_dict["email"],
                "additional_information":input_list_dict["additional_information"]
            }
        )
        try:
            if new_new_request_form_serializer.is_valid(raise_exception=True):
                get_new_request_form_serializer = new_new_request_form_serializer.save()
                return Response(new_new_request_form_serializer.data, status=status.HTTP_201_CREATED)
        except  serializers.ValidationError:
            return Response({"message":new_new_request_form_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            handler400 = str(exc)
            return Response({"message":handler400}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RequestFormDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = ()

    def get(self, request, pk):
        new_request_form = get_object_or_404(Vote, pk=pk)
        data = RequestFormSerializer(new_request_form).data
        return Response(data)


class RequestFormList(generics.ListAPIView):
    queryset = Vote.objects.all().order_by('id')
    serializer_class = RequestFormSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filer_fields = ('id', 'poll_title', 'full_name','email')
    ordering_fields = ('id', 'full_name','email')
    ordering = ('id')
    search_fields = ('id', 'poll_title', 'full_name','email')
    

class RequestFormUpdate(generics.UpdateAPIView):
    queryset = Vote.objects.all().order_by('id')
    serializer_class = RequestFormSerializer


class DeleteRequestForm(generics.DestroyAPIView):
    permission_class = [IsAuthenticated, ]
    queryset = RequestForm.objects.all()
    serializer_class = RequestFormSerializer