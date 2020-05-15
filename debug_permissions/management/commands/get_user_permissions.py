from __future__ import print_function
from django.core.management.base import BaseCommand
from goerr import err
from introspection.inspector import inspect


class Command(BaseCommand):
    help = 'Get a list of user and group permissions for a given user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options["username"]
        user_perms, group_perms, app_perms = inspect.user_perms(username)
        if err.exists:
            err.new(self.handle, "No user, aborting")
            err.throw()
            return
        # user perms
        perms = user_perms
        if len(perms) > 0:
            print("# User permissions for user", username + ":")
            for perm in perms:
                print("-", perm)
        else:
            print("# No user permissions found for", username)
        # group perms
        perms = group_perms
        sup, staff, active, date_joined = inspect.user_info(username)
        if len(perms) > 0:
            print("# Group permissions for user", username + ":")
            for perm in perms:
                print("-", perm)
        else:
            if sup is False:
                print("# No group permissions found for", username)
        # Modules perms
        if len(app_perms) > 0:
            print("# Modules that the user", username, "has permissions for:")
            for app in app_perms:
                print("-", app)
        else:
            if sup is False:
                print("# The user", username, "has permissions for no modules")
        if sup is True:
            print("The user is superuser and have all permissions")
        else:
            if staff is True:
                print("User is staff (joined at", str(date_joined) + ")")
            else:
                print("User joined at", str(date_joined))
        if active is False:
            print("This user is inactive")
