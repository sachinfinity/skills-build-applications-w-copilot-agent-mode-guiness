import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        for user_data in data['users']:
            User.objects.create(**user_data)

        # Populate teams
        for team_data in data['teams']:
            Team.objects.create(**team_data)

        # Populate activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data.pop('user_email'))
            Activity.objects.create(user=user, **activity_data)

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            team = Team.objects.get(name=leaderboard_data.pop('team_name'))
            Leaderboard.objects.create(team=team, **leaderboard_data)

        # Populate workouts
        for workout_data in data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))