import re

def is_valid_email(email):
    # Define a simple email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    return re.match(email_pattern, email) is not None