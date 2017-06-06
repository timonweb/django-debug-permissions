# Django Debug Permissions
Get a list of all user permissions available in the system

This app adds a single manage.py command that lists all user permissions available in the system.

## Supported versions
Haven't tested it with earlier version, but the app works for sure with:

  * Django: 1.11
  * Python: 3.4+

## Installation

1. Install using PIP:

  `pip install django-debug-permissions`

2. Add **debug_permissions** to INSTALLED_APPS:

  `INSTALLED_APPS += ['debug_permissions']`

## Usage
Run `python manage.py get_all_permissions` and you should get a list of all permissions similar to:

```
account.add_emailaddress
account.add_emailconfirmation
account.change_emailaddress
account.change_emailconfirmation
account.delete_emailaddress
account.delete_emailconfirmation
auth.add_group
auth.add_permission
auth.change_group
auth.change_permission
auth.delete_group
auth.delete_permission
...
sessions.add_session
sessions.change_session
sessions.delete_session
sites.add_site
sites.change_site
sites.delete_site
users.add_user
users.change_user
users.delete_user
```

## Contributors
Tim Kamanin (tim@timonweb.com, http://timonweb.com)

## Cross-promotion:
Checkout these modules if you:
* are tired of locating manage.py and typing `python manage.py` everytime - Django-manage.py-anywhere (https://github.com/timonweb/Django-manage.py-anywhere) will be your saviour;
* want to download database and media dumps via Django admin - Django Database Backup UI (https://github.com/timonweb/django-dbbackup-ui) will help you;