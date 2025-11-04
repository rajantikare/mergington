from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Sample data
        users = [
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["tony@marvel.com", "steve@marvel.com"]},
            {"name": "dc", "members": ["bruce@dc.com", "clark@dc.com"]},
        ]
        activities = [
            {"user": "tony@marvel.com", "activity": "Running", "duration": 30},
            {"user": "steve@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "bruce@dc.com", "activity": "Swimming", "duration": 25},
            {"user": "clark@dc.com", "activity": "Flying", "duration": 60},
        ]
        leaderboard = [
            {"team": "marvel", "points": 150},
            {"team": "dc", "points": 170},
        ]
        workouts = [
            {"name": "Super Strength", "suggested_for": "dc"},
            {"name": "Iron Endurance", "suggested_for": "marvel"},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
