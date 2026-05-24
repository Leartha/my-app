from rest_framework import serializers
from .models import Ballot, Vote


class BallotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballot
        fields = ["id", "title", "description", "options", "start_date", "end_date", "status"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["option"]

    def validate_option(self, value):
        ballot = self.context["ballot"]
        if value not in ballot.options:
            raise serializers.ValidationError("Invalid option for this ballot.")
        return value
