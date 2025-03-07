from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from users.models import User  # Import the custom user model

class Command(BaseCommand):
    help = "Create test users and assign them to groups"

    def handle(self, *args, **kwargs):
        # Define users and their groups
        users_data = [
            {"username": "student1", "email": "student1@example.com", "password": "password123", "group": "Students"},
            {"username": "student2", "email": "student2@example.com", "password": "password123", "group": "Students"},
            {"username": "teacher1", "email": "teacher1@example.com", "password": "password123", "group": "Teachers"},
            {"username": "teacher2", "email": "teacher2@example.com", "password": "password123", "group": "Teachers"},
        ]

        for user_data in users_data:
            # Create the user
            user, created = User.objects.get_or_create(
                username=user_data["username"],
                email=user_data["email"]
            )
            if created:
                user.set_password(user_data["password"])
                user.save()
                self.stdout.write(f"User '{user_data['username']}' created.")
            else:
                self.stdout.write(f"User '{user_data['username']}' already exists.")

            # Assign the user to the group
            try:
                group = Group.objects.get(name=user_data["group"])
                user.groups.add(group)
                self.stdout.write(f"User '{user_data['username']}' added to group '{user_data['group']}'.")
            except Group.DoesNotExist:
                self.stdout.write(f"Group '{user_data['group']}' does not exist.")

        self.stdout.write("User creation and group assignment completed.")
        