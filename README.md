# Secure Message Vault

A Python-based cryptographic application that implements AES-CBC encryption for secure message storage with hash-based integrity verification. This project demonstrates practical application of symmetric encryption, user authentication, and cryptographic best practices.

## Overview

Secure Message Vault is a command-line application that allows users to create accounts, encrypt personal messages, and securely retrieve them using password-based authentication. Each message is protected with AES encryption and verified using cryptographic hash functions to ensure data integrity.

## Features

- **User Account Creation**: Register new users with encrypted message storage
- **AES-CBC Encryption**: Industry-standard symmetric encryption for message protection
- **Multiple Hash Algorithms**: Support for SHA-256 and MD5 hash functions
- **Integrity Verification**: Hash-based validation to detect message tampering
- **Password-Based Key Derivation**: Secure key generation from user passwords
- **Persistent Storage**: JSON-based user data storage

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

## Requirements

```
pycryptodome
```

Install dependencies:
```bash
pip install pycryptodome
```

## Usage

Run the application:
```bash
python SecureMessageVault.py
```

### Creating a New User

1. Select option 1 from the main menu
2. Enter a username
3. Enter a password (used for key derivation)
4. Enter a message to encrypt
5. Choose a hash algorithm (SHA-256 or MD5)
6. User data is saved to `Users.json`

### Logging In

1. Select option 2 from the main menu
2. Enter your username
3. Enter your password
4. If credentials are correct and integrity check passes, your decrypted message is displayed

## File Structure

```
secure-message-vault/
├── secure_message_vault.py    # Main application file
├── Users.json                  # Encrypted user data storage
└── README.md                   # Project documentation
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

## Security Considerations

**Note**: This project is intended for educational purposes and demonstrates cryptographic concepts. For production use, consider the following improvements:

- Use proper key derivation functions (e.g., PBKDF2, Argon2, scrypt)
- Implement salting to prevent rainbow table attacks
- Use authenticated encryption modes (e.g., AES-GCM)
- Avoid MD5 for security-critical applications (known vulnerabilities)
- Add proper error handling and input validation
- Implement secure password policies
- Use secure storage solutions for sensitive data

## Learning Outcomes

Through this project, I gained practical experience with:

- Python cryptography libraries (PyCryptodome)
- AES encryption implementation
- CBC mode and IV management
- PKCS#7 padding and unpadding
- Hash function applications
- Base64 encoding for binary data
- JSON data persistence
- Secure application architecture

## License

This project is available for educational and portfolio purposes.

## Author

Developed to explore practical cryptographic implementations and secure application design.

## Acknowledgments

- PyCryptodome library for cryptographic primitives
- NIST standards for cryptographic best practices
