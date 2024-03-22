# Password Manager
A secure and easy to use password manager built with Python, using Tkinter for the UI and cryptography for encrypting the data.
## Instructions to Run the Application

2. **Dependencies**:
   Install the required Python ppackages:
   ```bash
   pip install tk cryptography
   ```

3. **Starting the Application**:
   Navigate to the project directory and run the command:
   ```bash
   python password_manager.py
   ```



## Screenshots
-1
-2

## Security Discussion

### What it Protect Against

The Password Manager is designed to protect against unauthorized access of the stored passwords. The threats being:
- Hackers trying to access your data by hacking your computer.
- Malware that tries to read your files and steal information.


###  Limitations

- **Local Storage**: While storing data locally reduces the risk of online breaches, but it means that your data could still be at risk if your computer is compromised or stolen. 
- **Master Password Recovery**: There is no way to recover your master password if it is forgotten.
- **No Two-Factor Authentication**: Currently, the application does not support two-factor authentication.

## Conclusion

While our Password Manager provides a secure way to store and manage your passwords with strong encryption, its stillimportant to have a good security practices, such as keeping your operating system uptodate and using antivirus software. Also the security of the program is dependend on the complexity of your masterpassword.
