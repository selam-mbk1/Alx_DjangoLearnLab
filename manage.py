#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
>>>>>>> c9cf000212ed4bd006de7e5f9c4c4bdb67b2dd19
>>>>>>> 9414b0d6d48e336e656ff5118cd041d6c8ea0a3d
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
