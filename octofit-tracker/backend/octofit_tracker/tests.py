from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', team='Alpha')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Alpha')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Alpha')
        self.assertEqual(team.name, 'Alpha')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity='Running')
        self.assertEqual(activity.user, 'test@example.com')
        self.assertEqual(activity.activity, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Alpha', score=100)
        self.assertEqual(leaderboard.team, 'Alpha')
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.description, 'Upper body')
        self.assertEqual(workout.difficulty, 'Easy')
