import os
import json
from cryptography.fernet import Fernet

# Set the default file path for the session storage to be
# in the user's home directory, in a hidden folder called ".storr",
# in a file called "session.json"
DEFAULT_DB_PATH = os.path.join(os.path.expanduser('~'), '.storr', 'session.json')

# If the file does not exist, create it with an empty JSON object
if not os.path.exists(DEFAULT_DB_PATH):
    with open(DEFAULT_DB_PATH, 'w') as f:
        f.write('{}')

class SecureStorage:
    def __init__(self, session_id, file_path=DEFAULT_DB_PATH, key=None):
        # If no encryption key is provided, generate a new one
        if not key:
            key = Fernet.generate_key()

        # Store the file path, encryption key, and session ID
        self.file_path = file_path
        self.key = key
        self.session_id = session_id

        # Create the directory for the session file if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # Create the session file if it doesn't exist, with an empty JSON object
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    # Encrypt a value using the encryption key
    def encrypt(self, value):
        f = Fernet(self.key)
        return f.encrypt(value.encode()).decode()

    # Decrypt a value using the encryption key
    def decrypt(self, value):
        f = Fernet(self.key)
        return f.decrypt(value.encode()).decode()

    # Set a value in the session data
    def set(self, name, value):
        # Load the session data from the file
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # If the session ID is not already in the data, create a new entry for it
        if self.session_id not in data:
            data[self.session_id] = {}

        # Encrypt the value and store it under the specified name
        data[self.session_id][name] = self.encrypt(value)

        # Write the updated session data back to the file
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    # Get a value from the session data
    def get(self, name):
        # Load the session data from the file
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # If the session ID is in the data and the specified name is present,
        # decrypt and return the value
        if self.session_id in data:
            session_data = data[self.session_id]
            if name in session_data:
                encrypted_value = session_data[name]
                return self.decrypt(encrypted_value)

        # If the session ID or specified name is not present, return None
        return None
