#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "security_panel.settings")

import sys
import django
import datetime
from django.utils.timezone import localtime
django.setup()

from datacenter.models import Visit, Passcard


def print_passcard(passcard):
    print(f'owner_name: {passcard.owner_name}')
    print(f'passcode: {passcard.passcode}')
    print(f'created_at: {passcard.created_at}')
    print(f'is_active: {passcard.is_active}')


def get_duration(visit):
    if visit.leaved_at:
        visit_end_time = visit.leaved_at
    else:
        visit_end_time = localtime()
    return datetime.timedelta(
        days=visit_end_time.day-visit.entered_at.day,
        hours=visit_end_time.hour-visit.entered_at.hour,
        minutes=visit_end_time.minute-visit.entered_at.minute
    )


def if_visit_long(visit, minutes=60):
    return get_duration(visit) >= datetime.timedelta(minutes=minutes)


def main():
    """Run administrative tasks."""
    """passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print(f'all passcards: {len(passcards)}')
    print(f'active passcards: {len(active_passcards)}')
    print_passcard(passcards[0])"""
    datetime_now = datetime.datetime.now()
    localtime_now = localtime()
    all_visits = Visit.objects.all()
    '''active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for active_visit in active_visits:
        print(f'{active_visit.passcard.owner_name} зашел в хранилище, время по москве:')
        print(active_visit.entered_at)
        print()
        print('Находится в хранилище:')
        print(datetime.timedelta(
            days=localtime_now.day-active_visit.entered_at.day,
            hours=localtime_now.hour-active_visit.entered_at.hour,
            minutes=localtime_now.minute-active_visit.entered_at.minute
            ))'''
    '''guard = Passcard.objects.all()[0]
    guard_visits = Visit.objects.filter(passcard=guard.id)
    print(guard_visits)'''
    print(len(all_visits))
    long_visits = [x for x in all_visits if if_visit_long(x, 1000)]
    print(long_visits)
    print(len(long_visits))
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
