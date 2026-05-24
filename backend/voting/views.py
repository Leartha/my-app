from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ballot, Vote
from .serializers import BallotSerializer, VoteSerializer


@api_view(["GET", "POST"])
def ballot_list(request):
    if request.method == "GET":
        ballots = Ballot.objects.all().order_by("-created_at")
        serializer = BallotSerializer(ballots, many=True)
        return Response(serializer.data)

    serializer = BallotSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def ballot_detail(request, pk):
    try:
        ballot = Ballot.objects.get(pk=pk)
    except Ballot.DoesNotExist:
        return Response({"error": "Ballot not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = BallotSerializer(ballot)
    return Response(serializer.data)


@api_view(["POST"])
def cast_vote(request, pk):
    try:
        ballot = Ballot.objects.get(pk=pk)
    except Ballot.DoesNotExist:
        return Response({"error": "Ballot not found."}, status=status.HTTP_404_NOT_FOUND)

    if ballot.status == "closed" or timezone.now() > ballot.end_date:
        return Response({"error": "Ballot is closed."}, status=status.HTTP_400_BAD_REQUEST)

    # Session-based duplicate prevention
    session_key = f"voted_ballot_{pk}"
    if request.session.get(session_key):
        return Response({"error": "You have already voted in this ballot."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = VoteSerializer(data=request.data, context={"ballot": ballot})
    if serializer.is_valid():
        serializer.save(ballot=ballot)
        request.session[session_key] = True
        return Response({"message": "Vote cast successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def ballot_results(request, pk):
    try:
        ballot = Ballot.objects.get(pk=pk)
    except Ballot.DoesNotExist:
        return Response({"error": "Ballot not found."}, status=status.HTTP_404_NOT_FOUND)

    votes = Vote.objects.filter(ballot=ballot)
    results = {option: 0 for option in ballot.options}
    for vote in votes:
        if vote.option in results:
            results[vote.option] += 1

    return Response({
        "ballot": ballot.title,
        "status": ballot.status,
        "total_votes": votes.count(),
        "results": results,
    })
