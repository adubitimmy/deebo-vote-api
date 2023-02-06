from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Candidates, Vote, RequestForm

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = ("id","candidates_name","manifesto", "portfolio")
        extra_kwargs = {
            "candidates_name":{"required":False},
            "manifesto":{"required":False},
            "portfolio":{"required":False}
        }
        
        def create(self, validated_data):
            new_candidate = Candidates.objects.create(
                candcandidates_name = str(validated_data["candidates"]).title(),
                manifesto = str(validated_data["manifesto"]).lower(),
                portfolio = str(validated_data["portfolio"]).lower(),
            )
            try:
                return new_candidate
            except Exception as exc:
                raise exc 
            
            
            
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id","nationality", "location", "state_of_origin", "pvc_collected")
        extra_kwargs = {
            "nationality":{"required":False},
            "location":{"required":False},
            "state_of_origin":{"required":False},
            "pvc_collected":{"required":False}
        }
        
        def create(self, validated_data):
            new_vote = Vote.objects.create(
                nationality = str(validated_data["nationality"]),
                location = str(validated_data["location"]),
                state_of_origin = str(validated_data["state_of_origin"]),
                pvc_collected = str(validated_data["pvc_collected"])
            )
            try:
                return new_vote 
            except Exception as exc:
                return exc 
            
class RequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForm
        fields = ("id", "poll_category", "poll_title", "full_name", "email", "additional_information")
        extra_kwargs = {
            "poll_category":{"required":False},
            "poll_title":{"required":False},
            "full_name":{"required":False},
            "email":{"required":False},
            "additional_information":{"required":False}, 
        }
        def create(self, validated_data):
            new_request_form = RequestForm.objects.create(
                poll_category = str(validated_data["poll_category"]),
                poll_title = str(validated_data["poll_title"]),
                full_name = str(validated_data["full_name"]),
                email = str(validated_data["email"]),
                additional_information = str(validated_data["additional_information"])
            )
            try:
                return new_request_form 
            except Exception as exc:
                return exc 
        
        def update(self, instance, validated_data):
            candidate = instance 
            if validated_data["candidates_name"]:
                candidates_name = validated_data["candidates_name"]
                candidate.candidates_name = candidates_name
            if validated_data["manifesto"]:
                manifesto = validated_data["manifesto"]
                candidate.manifesto = manifesto
            if validated_data["portfolio"]:
                portfolio = validated_data["portfolio"]
                candidate.portfolio = portfolio
                
                candidate.save()
                return candidate