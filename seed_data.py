#!/usr/bin/env python3
"""
seed_data.py - Populate sample contacts for demonstration
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.phonebook import Phonebook
from storage.database import DatabaseStorage

SAMPLE_CONTACTS = [
    {"name": "Alice Johnson",  "phone": "9876543210", "email": "alice@example.com",  "group": "Work",   "tags": ["manager","vip"],      "favorite": True,  "notes": "Team lead"},
    {"name": "Bob Smith",      "phone": "8765432109", "email": "bob@example.com",    "group": "Friend", "tags": ["college","chess"],     "favorite": False, "notes": "Met at uni"},
    {"name": "Carol Williams", "phone": "7654321098", "email": "carol@family.net",   "group": "Family", "tags": ["sister"],              "favorite": True,  "address": "12 Oak Lane"},
    {"name": "Dave Brown",     "phone": "6543210987",                                "group": "Work",   "tags": ["developer","remote"],  "favorite": False},
    {"name": "Eve Davis",      "phone": "5432109876", "email": "eve@startup.io",     "group": "Work",   "tags": ["client","vip"],        "favorite": True,  "notes": "Key account"},
    {"name": "Frank Miller",   "phone": "4321098765",                                "group": "Friend", "tags": ["gym"],                 "favorite": False},
    {"name": "Grace Lee",      "phone": "3210987654", "email": "grace@example.com",  "group": "Family", "tags": ["cousin"],              "favorite": False, "address": "45 Maple Ave"},
    {"name": "Henry Wilson",   "phone": "2109876543",                                "group": "Other",  "tags": ["neighbor"],            "favorite": False},
    {"name": "Iris Chen",      "phone": "1098765432", "email": "iris@design.co",     "group": "Work",   "tags": ["designer","freelance"],"favorite": True},
    {"name": "Jack Taylor",    "phone": "9988776655",                                "group": "Friend", "tags": ["school","cricket"],    "favorite": False, "notes": "Childhood friend"},
]

def seed():
    storage = DatabaseStorage()
    pb = Phonebook(storage)

    added = 0
    for data in SAMPLE_CONTACTS:
        try:
            pb.add_contact(**data)
            added += 1
            print(f"  [+] {data['name']}")
        except Exception as e:
            print(f"  [~] {data['name']}: {e}")

    print(f"\nSeeded {added} sample contacts.")

if __name__ == "__main__":
    seed()
