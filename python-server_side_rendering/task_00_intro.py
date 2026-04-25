#!/usr/bin/python3
"""
Module to generate personalized invitation files from a template.
"""
import os


def generate_invitations(template, attendees):
    """
    Generates invitation files for each attendee in the list.
    
    Args:
        template (str): The template string with placeholders.
        attendees (list): List of dictionaries containing attendee data.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Invalid input type. Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type. Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee
    for i, attendee in enumerate(attendees, start=1):
        try:
            # Create a copy of the template to work on
            invitation = template
            
            # Placeholders to replace
            placeholders = ["name", "event_title", "event_date", "event_location"]
            
            for key in placeholders:
                # If key is missing or value is None, replace with "N/A"
                val = attendee.get(key)
                if val is None:
                    val = "N/A"
                
                # Replace {key} with the actual value
                invitation = invitation.replace("{" + key + "}", str(val))
            
            # 4. Generate Output Files
            filename = f"output_{i}.txt"
            
            # Check if file already exists to be safe
            if os.path.exists(filename):
                print(f"Warning: {filename} already exists. Overwriting...")
                
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(invitation)
                
        except Exception as e:
            print(f"An error occurred while processing attendee {i}: {e}")
