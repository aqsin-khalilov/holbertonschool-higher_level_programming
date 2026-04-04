#!/usr/bin/python3
import hidden_4

def discover_names():
    # Get all names defined in the hidden_4 module
    all_names = dir(hidden_4)
    
    # Sort them alphabetically
    all_names.sort()
    
    # Filter and print names that do not start with "__"
    for name in all_names:
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    discover_names()
