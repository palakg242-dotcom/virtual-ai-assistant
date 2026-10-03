"""
datetime_utils.py
------------------
Small wrapper functions around Python's built-in datetime module.
Covers FR-03 (date) and FR-04 (time) from the project brief.
"""

import datetime


def get_current_time():
    """Return the current time, formatted for display."""
    now = datetime.datetime.now()
    return now.strftime("It's currently %I:%M %p.")


def get_current_date():
    """Return today's date, formatted for display."""
    now = datetime.datetime.now()
    return now.strftime("Today's date is %B %d, %Y.")


def get_current_hour():
    """Return just the hour (0-23). Used by ai_concepts.py for the
    rule-based activity recommedation (FR-13)."""
    return datetime.datetime.now().hour