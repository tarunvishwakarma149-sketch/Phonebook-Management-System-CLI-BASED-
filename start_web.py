import uvicorn
import sys
import os
import threading
import webbrowser

def open_browser():
    # Give the server a second to start
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    print(r"""
  ____  _                      _                 _    ____           
 |  _ \| |__   ___  _ __   ___| |__   ___   ___ | | _|  _ \ _ __ ___  
 | |_) | '_ \ / _ \| '_ \ / _ \ '_ \ / _ \ / _ \| |/ / |_) | '__/ _ \ 
 |  __/| | | | (_) | | | |  __/ |_) | (_) | (_) |   <|  __/| | | (_) |
 |_|   |_| |_|\___/|_| |_|\___|_.__/ \___/ \___/|_|\_\_|   |_|  \___/ 
                                                                         
         Futuristic Web Interface Initializing...
    """)
    print("Starting Web Server at http://127.0.0.1:8000")
    
    # Schedule the browser to open after 1.5 seconds
    threading.Timer(1.5, open_browser).start()
    
    uvicorn.run("web_app:app", host="127.0.0.1", port=8000)

