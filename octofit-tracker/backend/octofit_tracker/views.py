from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'users': 'https://super-tribble-69ww5xj67pqw2rxqq-8000.app.github.dev/users/',
        'teams': 'https://super-tribble-69ww5xj67pqw2rxqq-8000.app.github.dev/teams/',
        'activities': 'https://super-tribble-69ww5xj67pqw2rxqq-8000.app.github.dev/activities/',
        'leaderboard': 'https://super-tribble-69ww5xj67pqw2rxqq-8000.app.github.dev/leaderboard/',
        'workouts': 'https://super-tribble-69ww5xj67pqw2rxqq-8000.app.github.dev/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer