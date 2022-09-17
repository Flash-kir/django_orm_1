#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "security_panel.settings")

import sys
import django
django.setup()

from datacenter.models import Passcard


def print_passcard(passcard):
    print(f'owner_name: {passcard.owner_name}')
    print(f'passcode: {passcard.passcode}')
    print(f'created_at: {passcard.created_at}')
    print(f'is_active: {passcard.is_active}')


def main():
    """Run administrative tasks."""
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print(f'all passcards: {len(passcards)}')
    print(f'active passcards: {len(active_passcards)}')
    print_passcard(passcards[0])
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
