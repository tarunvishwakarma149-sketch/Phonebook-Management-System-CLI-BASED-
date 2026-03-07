# PhonebookPro 📒

A hyper-advanced, multi-file contact management system built in Python.

## Features

| Feature | Description |
|---|---|
| 🗄️ SQLite Storage | Persistent database with WAL journaling |
| 🔍 Smart Search | Search by name, phone, email, notes, tags |
| 📋 Groups | Categorize contacts: Family, Work, Friend, Other |
| 🏷️ Tags | Multi-tag support with tag filtering |
| ⭐ Favorites | Mark and list favorite contacts |
| 📞 Call Log | Track call history and call counts |
| 🔀 Merge | Merge duplicate contacts intelligently |
| 📊 Statistics | Visual stats with group charts & top contacts |
| 📤 Export | CSV, JSON, vCard (.vcf) export |
| 📥 Import | CSV and JSON bulk import |
| 🕓 Activity Log | Full audit trail of all changes |
| ✅ Validation | Phone, email, name, group validation |
| 🧪 Tests | 30+ unit tests with pytest |
| 📄 Logging | Rotating file log in data/phonebook.log |

## Project Structure

```
phonebook_pro/
├── main.py                   # Entry point
├── seed_data.py              # Sample data loader
├── core/
│   ├── contact.py            # Contact model + validation
│   └── phonebook.py          # Business logic
├── storage/
│   ├── base.py               # Abstract storage interface
│   ├── database.py           # SQLite backend
│   └── importexport.py       # CSV / JSON / vCard I/O
├── ui/
│   └── cli.py                # Full interactive CLI
├── utils/
│   ├── display.py            # Colors, tables, prompts
│   └── logger.py             # Rotating log setup
├── tests/
│   └── test_phonebook.py     # 30+ unit tests
├── data/                     # Auto-created: DB + logs
└── exports/                  # Auto-created: export files
```

## Quick Start

```bash
# Install test dependencies (optional)
pip install pytest

# Load sample contacts
python seed_data.py

# Run the app
python main.py

# Run tests
python -m pytest tests/ -v
```

## Usage

Once running, navigate the menu with number keys:

```
 1. Add Contact          8. Filter by Group
 2. View All Contacts    9. Filter by Tag
 3. Search Contacts     10. Log a Call
 4. View Contact Detail 11. Merge Contacts
 5. Edit Contact        12. Statistics
 6. Delete Contact      13. Import / Export
 7. Favorites           14. Activity Log
 0. Exit
```

## Contact Fields

- **Name** — Full name (title-cased, validated)
- **Phone** — Primary number (7–15 digits, + prefix OK)
- **Alternate Phones** — Multiple secondary numbers
- **Email** — Optional, validated format
- **Address** — Free text address
- **Group** — Family | Friend | Work | Other
- **Tags** — Custom tags (comma-separated)
- **Notes** — Free text notes
- **Favorite** — Star/unstar a contact
- **Call Count** — Auto-incremented via Log a Call

## Requirements

- Python 3.8+
- No external dependencies (stdlib only)
- `pytest` for running tests
