# Secure Message Vault

A Python-based cryptographic application that implements AES-CBC encryption for secure message storage with hash-based integrity verification. This project demonstrates practical application of symmetric encryption, user authentication, and cryptographic best practices.

**BONUS FEATURE**: Includes a web-based frontend interface connected via Flask for enhanced user experience.

## Overview

Secure Message Vault is an encryption application that allows users to create accounts, encrypt personal messages, and securely retrieve them using password-based authentication. Each message is protected with AES encryption and verified using cryptographic hash functions to ensure data integrity.

The application is available in two modes:
- **Command-line interface** (original assignment)
- **Web interface** (bonus implementation)

## Features

- **User Account Creation**: Register new users with encrypted message storage
- **AES-CBC Encryption**: Industry-standard symmetric encryption for message protection
- **Multiple Hash Algorithms**: Support for SHA-256 and MD5 hash functions
- **Integrity Verification**: Hash-based validation to detect message tampering
- **Password-Based Key Derivation**: Secure key generation from user passwords
- **Persistent Storage**: JSON-based user data storage
- **Web Interface**: User-friendly HTML/CSS/JavaScript frontend (bonus feature)
- **REST API**: Flask-based backend for frontend communication

## Technical Implementation

### Cryptographic Components

- **Encryption Algorithm**: AES (Advanced Encryption Standard) in CBC mode
- **Key Derivation**: SHA-256 or MD5 hashing of user passwords
- **Padding Scheme**: PKCS#7 padding for block cipher compatibility
- **Initialization Vector**: Randomly generated 16-byte IV for each encryption
- **Integrity Check**: Hash verification of encrypted messages

### Security Features

- AES-256 encryption when using SHA-256 (32-byte key)
- AES-128 encryption when using MD5 (16-byte key)
- Unique IV for each encrypted message
- Hash-based message authentication
- Secure random number generation for IVs

### Web Architecture (Bonus Feature)

- **Backend**: Flask REST API with CORS support
- **Frontend**: HTML5, CSS3, and vanilla JavaScript
- **Communication**: JSON-based API endpoints
- **Styling**: Modern gradient design with responsive layout

## Requirements

```
pycryptodome
flask
flask-cors
```

Install dependencies:
```bash
pip install pycryptodome flask flask-cors
```

## Usage

### Option 1: Command-Line Interface (Original)

Run the application:
```bash
python secure_message_vault.py
```

#### Creating a New User

1. Select option 1 from the main menu
2. Enter a username
3. Enter a password (used for key derivation)
4. Enter a message to encrypt
5. Choose a hash algorithm (SHA-256 or MD5)
6. User data is saved to `Users.json`

#### Logging In

1. Select option 2 from the main menu
2. Enter your username
3. Enter your password
4. If credentials are correct and integrity check passes, your decrypted message is displayed

### Option 2: Web Interface (Bonus Feature)

1. Start the Flask backend server:
```bash
python app.py
```

2. Open `index.html` in your web browser

3. Use the web interface to:
   - Create new users with encrypted messages
   - Login to decrypt and view stored messages
   - Choose between SHA-256 or MD5 hashing

The web interface provides a more intuitive user experience with visual feedback and modern styling.

## File Structure

```
secure-message-vault/
├── secure_message_vault.py    # Main CLI application (original)
├── app.py                      # Flask backend server (bonus)
├── index.html                  # Web frontend interface (bonus)
├── Users.json                  # Encrypted user data storage
└── README.md                   # Project documentation
```

## API Endpoints (Bonus Feature)

### POST /api/create-user
Creates a new user with encrypted message storage.

**Request Body:**
```json
{
  "username": "string",
  "password": "string",
  "message": "string",
  "hashChoice": "sha256|md5"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User created successfully!"
}
```

### POST /api/login
Authenticates user and returns decrypted message.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "success": true,
  "message": "decrypted_message_content"
}
```

## Data Storage Format

User data is stored in JSON format with the following structure:

```json
{
  "Username": "user_name",
  "HashAlgo": "SHA-256",
  "IV": "base64_encoded_iv",
  "encryptedMessage": "base64_encoded_ciphertext",
  "hashValue": "hex_hash_digest"
}
```

## Educational Purpose

This project demonstrates understanding of:

- Symmetric encryption algorithms
- Block cipher modes of operation
- Cryptographic hash functions
- Key derivation techniques
- Padding schemes
- Integrity verification methods
- Secure coding practices
- **Web application development** (bonus)
- **REST API design** (bonus)
- **Frontend-backend integration** (bonus)

## Development Process Disclosure

**Core Python Backend (Original Assignment)**: Implemented independently to demonstrate understanding of cryptographic concepts and secure programming practices.

**Web Interface (Bonus Feature)**: Developed with AI assistance (Claude AI) to extend the project beyond course requirements. This component demonstrates:
- Ability to integrate new technologies with existing code
- Understanding of web application architecture
- Initiative to create a more user-friendly interface
- Practical application of Flask for API development

The integration of Flask and frontend components required understanding of HTTP methods, JSON serialization, CORS policies, and API design principles.

## Security Considerations

**Note**: This project is intended for educational purposes and demonstrates cryptographic concepts. For production use, consider the following improvements:

- Use proper key derivation functions (e.g., PBKDF2, Argon2, scrypt)
- Implement salting to prevent rainbow table attacks
- Use authenticated encryption modes (e.g., AES-GCM)
- Avoid MD5 for security-critical applications (known vulnerabilities)
- Add proper error handling and input validation
- Implement secure password policies
- Use secure storage solutions for sensitive data
- Add rate limiting and input sanitization for web API
- Implement HTTPS for encrypted communication
- Add authentication tokens for API security

## Learning Outcomes

Through this project, I gained practical experience with:

**Core Cryptography:**
- Python cryptography libraries (PyCryptodome)
- AES encryption implementation
- CBC mode and IV management
- PKCS#7 padding and unpadding
- Hash function applications
- Base64 encoding for binary data
- JSON data persistence
- Secure application architecture

**Web Development (Bonus):**
- Flask framework and routing
- REST API design and implementation
- CORS configuration
- Frontend-backend communication
- Asynchronous JavaScript (fetch API)
- Responsive web design
- Error handling in web applications

## Technologies Used

**Backend:**
- Python 3.x
- PyCryptodome (cryptographic operations)
- Flask (web framework)
- Flask-CORS (cross-origin support)

**Frontend:**
- HTML5
- CSS3 (with gradients and animations)
- JavaScript (ES6+)
- Fetch API for HTTP requests

## License

This project is available for educational and portfolio purposes.

## Author

Developed to explore practical cryptographic implementations and secure application design, with bonus web interface to demonstrate full-stack integration capabilities.

## Acknowledgments

- PyCryptodome library for cryptographic primitives
- NIST standards for cryptographic best practices
- Flask framework for web application development
- AI assistance (Claude) for frontend development guidance
