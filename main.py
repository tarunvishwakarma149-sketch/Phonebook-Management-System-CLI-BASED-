#!/usr/bin/env python3
"""
PhonebookPro - Advanced Contact Management System
Entry point for the application.
"""

import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.cli import CLI
from core.phonebook import Phonebook
from storage.database import DatabaseStorage
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    print(r"""
  ____  _                      _                 _    ____           
 |  _ \| |__   ___  _ __   ___| |__   ___   ___ | | _|  _ \ _ __ ___  
 | |_) | '_ \ / _ \| '_ \ / _ \ '_ \ / _ \ / _ \| |/ / |_) | '__/ _ \ 
 |  __/| | | | (_) | | | |  __/ |_) | (_) | (_) |   <|  __/| | | (_) |
 |_|   |_| |_|\___/|_| |_|\___|_.__/ \___/ \___/|_|\_\_|   |_|  \___/ 
                                                                         
         Advanced Contact Management System v2.0
    """)

    try:
        storage = DatabaseStorage()
        book = Phonebook(storage)
        cli = CLI(book)
        cli.run()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        print(f"\n[✗] Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
