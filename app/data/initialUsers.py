from datetime import date

USERS = [
    {
        "name": "John Doe",
        "email": "email@email.com",
        "agency": "I&A",
        "date_added": date(2023, 1, 20),
        "super_user": True,
    },
    {
        "name": "Jane Doe",
        "email": "email@email.com",
        "agency": "CBP",
        "date_added": date(2023, 2, 20),
        "super_user": False,
    },
    {
        "name": "John Smith",
        "email": "email@email.com",
        "agency": "ICE",
        "date_added": date(2023, 3, 20),
        "super_user": False,
    },
    {
        "name": "Jane Smith",
        "email": "email@email.com",
        "agency": "I&A",
        "date_added": date(2023, 4, 20),
        "super_user": True,
    },
]
