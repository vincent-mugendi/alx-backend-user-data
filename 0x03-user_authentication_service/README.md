# 0x03. User authentication service

## Back-end

### Authentification

- Weight: 1
- Project will start Apr 22, 2024 6:00 AM, must end by Apr 26, 2024 6:00 AM
- Checker was released at Apr 23, 2024 6:00 AM
- An auto review will be launched at the deadline

In the industry, you should not implement your own authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-User). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

### Resources

Read or watch:

- Flask documentation
- Requests module
- HTTP status codes

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

### Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- You should use SQLAlchemy 1.3.x
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions should be type annotated
- The Flask app should only interact with Auth and never with DB directly.
- Only public methods of Auth and DB should be used outside these classes

### Setup

You will need to install bcrypt:

```bash
pip3 install bcrypt
```

## Tasks

### 0. User model

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: user.py

### 1. Create user

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: db.py

### 2. Find user

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: db.py

### 3. Update user

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: db.py

### 4. Hash password

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 5. Register user

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 6. Basic Flask app

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 7. Register user

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 8. Credentials validation

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 9. Generate UUIDs

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 10. Get session ID

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 11. Log in

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 12. Find user by session ID

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 13. Destroy session

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 14. Log out

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 15. User profile

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 16. Generate reset password token

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 17. Get reset password token

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

### 18. Update password

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: auth.py

### 19. Update password end-point

- [GitHub repository](https://github.com/alx-backend-user-data/0x03-user_authentication_service)
- Directory: 0x03-user_authentication_service
- File: app.py

```

Feel free to adjust the formatting or

 add more details if needed!
```
