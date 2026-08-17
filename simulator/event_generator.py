import random
import uuid
from datetime import datetime


# Cognistream Projects
projects = [
    "Cognistream Platform",
    "Cognistream Analytics",
    "Cognistream API",
    "Cognistream Dashboard"
]


# Activity Definitions
activity_details = {
    "Coding": ("VS Code", False),
    "Debugging": ("VS Code", False),
    "Code Review": ("GitHub", False),
    "Git Commit": ("Git", False),
    "Testing": ("VS Code", False),
    "Meeting": ("Microsoft Teams", True),
    "Slack": ("Slack", True),
    "Email": ("Outlook", True),
    "Break": ("System", False),
    "Idle": ("System", False)
}


# Developer Behavior Patterns
behavior_patterns = {

    "Focused": {
        "activities": [
            "Coding",
            "Coding",
            "Coding",
            "Debugging",
            "Testing",
            "Git Commit"
        ]
    },

    "Normal": {
        "activities": [
            "Coding",
            "Coding",
            "Debugging",
            "Testing",
            "Git Commit",
            "Slack",
            "Email"
        ]
    },

    "Interrupted": {
        "activities": [
            "Coding",
            "Slack",
            "Email",
            "Meeting",
            "Coding",
            "Slack",
            "Email",
            "Meeting"
        ]
    }
}


def generate_event(developer_id, behavior):
    """
    Generate a single Cognistream developer activity event.
    """

    activity = random.choice(
        behavior_patterns[behavior]["activities"]
    )

    application, interruption = activity_details[activity]

    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "developer_id": developer_id,
        "activity_type": activity,
        "application": application,
        "project": random.choice(projects),
        "duration_seconds": random.randint(30, 600),
        "interruption": interruption,
        "context_switch": interruption,
        "behavior_pattern": behavior,
        "session_id": str(uuid.uuid4())[:8]
    }

    return event
