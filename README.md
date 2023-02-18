![The painless way to store session data](https://raw.githubusercontent.com/KrishnaVyshak/storr/main/storr%20cover.png)
# storr
### *The painless way to store session data*

[Github](https://github.com/KrishnaVyshak/storr)


`storr` is a Python library for providing a simple and secure way to store session data in a file. With `storr`, you can easily store and retrieve data without worrying about sensitive information being exposed in plain text. `storr` encrypts your data using the `cryptography`  package, ensuring that only authorized parties can access it. Plus, the encrypted data is stored in a file that's protected by your operating system's permissions, providing an additional layer of security. So, whether you're working on a personal project or a professional application, `storr` can help you keep your data secure.


## Installation


You can install `storr` using `pip`, the Python package manager:

```bash
pip install storr
``` 

## Usage

### Initialization

To initialize a `SecureStorage` object, you need to provide a `session_id` parameter. This is a unique identifier for the session. Additionally, you can provide a `file_path` parameter to specify the location of the session file, and a `key` parameter to specify the encryption key.

If you don't provide a `key` parameter, a new encryption key will be generated automatically.

```python
from storr import SecureStorage

session_id = "my-session-id"
storage = SecureStorage(session_id)
``` 

### Storing Data

To store data in the session, use the `set` method of the `SecureStorage` object. This method takes two parameters: the name of the data (a string), and the value of the data (any type).

```python
my_var = "John Doe"
storage.set("name", my_var)
``` 

### Retrieving Data

To retrieve data from the session, use the `get` method of the `SecureStorage` object. This method takes one parameter: the name of the data to retrieve (a string).

```python
my_var = storage.get("name")
```

If the requested data does not exist in the session, the `get` method will return `None`.

### Advanced Usage

#### Custom File Path

If you want to store the session data in a file other than the default file location, you can provide a `file_path` parameter when initializing the `SecureStorage` object.

```python
session_id = "my-session-id"
file_path = "/path/to/custom/session.json"
storage = SecureStorage(session_id, file_path)
``` 

#### Custom Encryption Key

If you want to use a custom encryption key, you can provide a `key` parameter when initializing the `SecureStorage` object.

```python
from storr import SecureStorage
import base64
import secrets

# create a session ID for the current user (you could use any string here)
session_id = '123'

# Generate 32 bytes of random data
data = secrets.token_bytes(32)

# Encode the data using base64url encoding
key = base64.urlsafe_b64encode(data)

# create an instance of the SecureStorage class for the session
#create a 32 urlsafe base64-encoded bytes key
storage = SecureStorage(session_id, key=key)
``` 

## Example

Here's a basic example usage of `storr`:

```python
from storr import SecureStorage

# initialize the storage with a session ID
storage = SecureStorage(session_id='123')

# store a value
storage.set('name', 'John Doe')

# retrieve a value
name = storage.get('name')

# print the value
print(name)  # Output: John Doe` 
```

In the above example, we created a new `SecureStorage` object with a session ID of `'123'`. We then stored the name `'John Doe'` under the key `'name'` and retrieved it back using the same key.

### Using a custom file path

You can also specify a custom file path for the session data file by passing in the `file_path` parameter to the `SecureStorage` constructor. Here's an example:

```python
import storr

# Create a SecureStorage instance with a custom file path
storage = storr.SecureStorage('my_session', file_path='/path/to/my/session.json')

# Set a value
storage.set('name', 'John Doe')

# Get a value
name = storage.get('name')
print(name)  # Output: John Doe` 
```

### Using a custom encryption key

If you want to use a custom encryption key for the session data, you can pass it in as a parameter to the `SecureStorage` constructor. Here's an example:

```python
import storr
import base64
import secrets

# Generate 32 bytes of random data
data = secrets.token_bytes(32)

# Encode the data using base64url encoding
myKey = base64.urlsafe_b64encode(data)

# Create a SecureStorage instance with the custom key
storage = storr.SecureStorage('my_session', key=myKey)

# Set a value
storage.set('name', 'John Doe')

# Get a value
name = storage.get('name')
print(name)  # Output: John Doe
```

### Handling missing or invalid values

If you try to get a value that doesn't exist, the `get` method will return `None`. You can use this to handle missing or invalid values in your code. Here's an example:

```python
import storr

# Create a SecureStorage instance
storage = storr.SecureStorage('my_session')

# Try to get a value that doesn't exist
name = storage.get('name')

if name is None:
    print('Name not found')
else:
    print('Name:', name)
```
We hope these examples help you understand the different features of `storr` and how to use them in your own code.

## Security

`storr` uses the Fernet symmetric encryption algorithm to encrypt all session data. The encryption key is generated automatically, but you can also provide a custom encryption key for added security.

## Version
### **1.0.0** - *`Latest`*

This is the first version of `storr`. In future versions, new and advanced features will be added to make session storage even more secure and flexible.

## Conclusion

This marks the end of the first version of `storr`. We hope that you find it useful for your needs. Please note that this is an open-source project, and we welcome contributions and feedback from the community.

In future versions, we plan to add new and advanced features to make it even more secure and useful. If you have any suggestions, please feel free to open an issue on the project's GitHub repository or contribute directly to the codebase.

Thank you for using `storr`. We hope it serves you well.
