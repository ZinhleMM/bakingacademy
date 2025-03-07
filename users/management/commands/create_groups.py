from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups_permissions = {
            "Students": [
                # Permissions for Students
                "view_user",  # Students can view user profiles
                "view_group",  # Students can view groups
                "view_contenttype",  # Students can view content types
                "view_session",  # Students can view sessions
            ],
            "Teachers": [
                # Permissions for Teachers
                "add_user", "change_user", "delete_user", "view_user",  # Manage users
                "add_group", "change_group", "delete_group", "view_group",  # Manage groups
                "add_permission", "change_permission", "delete_permission", "view_permission",  # Manage permissions
                "add_contenttype", "change_contenttype", "delete_contenttype", "view_contenttype",  # Manage content types
                "add_session", "change_session", "delete_session", "view_session",  # Manage sessions
            ],
        }

        # Create groups and assign permissions
        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f"Group '{group_name}' created.")
            else:
                self.stdout.write(f"Group '{group_name}' already exists.")

            # Assign permissions to the group
            for perm_codename in permissions:
                try:
                    # Find the permission by codename
                    permission = Permission.objects.get(codename=perm_codename)
                    group.permissions.add(permission)
                    self.stdout.write(f"Added permission '{perm_codename}' to group '{group_name}'.")
                except Permission.DoesNotExist:
                    self.stdout.write(f"Permission '{perm_codename}' not found.")

        self.stdout.write("Groups and permissions setup completed.")
