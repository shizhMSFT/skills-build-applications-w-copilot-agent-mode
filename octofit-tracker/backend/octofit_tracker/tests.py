from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-08-14')
        self.assertEqual(str(activity), 'Test User - Run')
    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        workout = Workout.objects.create(name='Test Workout')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'Test Workout')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(str(leaderboard), 'Test Team - 50 pts')
