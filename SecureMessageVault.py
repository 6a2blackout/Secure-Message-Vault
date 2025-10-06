from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256, md5
import json, base64


def pad(data):
    paddingLength = 16 - (len(data) % 16)
    return data + chr(paddingLength) * paddingLength

def unpad(data):
    paddingLength = ord(data[-1])
    return data[:-paddingLength]



print("Welcome!!")

command = 0

while command != 3:
    print("1.\tCreate a New User\n2.\tLogin to an Existing User\n3.\tExit\n")
    try:
        command = int(input("\nEnter Command:\t"))
        if command == 1:
            newUserName = input("Enter Name:\t")
            newPassword = input("Enter Password:\t")
            newMessage = input("Enter a Message to Encrypt:\t")


            

            choice = 0
            while choice == 0:
                choice = int(input("Choose:\n1.\tSHA-256\n2.\tMD5\nChoice:\t"))
                if choice == 1:
                    key = sha256(newPassword.encode()).digest()
                    IV = get_random_bytes(16)
                    encryption = AES.new(key, AES.MODE_CBC, IV)
                    encryptedMessage = encryption.encrypt(pad(newMessage).encode())
                    hashValue = sha256(encryptedMessage).hexdigest()
                    hashAlgo = "SHA-256"
                elif choice == 2:
                    key = md5(newPassword.encode()).digest()
                    IV = get_random_bytes(16)
                    encryption = AES.new(key, AES.MODE_CBC, IV)
                    encryptedMessage = encryption.encrypt(pad(newMessage).encode())
                    hashValue = md5(encryptedMessage).hexdigest()
                    hashAlgo = "MD5"
                else:
                    print("Try Again")


            User = {
                "Username": newUserName, "HashAlgo": hashAlgo, "IV": base64.b64encode(IV).decode(), "encryptedMessage": base64.b64encode(encryptedMessage).decode(), "hashValue": hashValue,
                #"hashAlgorithm": "SHA256"
            }

            with open("Users.json", "a") as file:
                file.write(json.dumps(User) + "\n\n\n")

            print("User Created and Message Encrypted Successfully\n\n")
        elif command == 2:
            userName = input("Enter Username:\t")
            password = input("Enter Password:\t")

            access = False
            with open("Users.json", "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    try:
                        User = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    if User["Username"] == userName:
                        access = True
                        if User["HashAlgo"] == "SHA-256":

                            key = sha256(password.encode()).digest()

                            IV = base64.b64decode(User["IV"])
                            encryptedMessage = base64.b64decode(User["encryptedMessage"])
                            hashValue = User["hashValue"]

                            testHash = sha256(encryptedMessage).hexdigest()
                            if testHash != hashValue:
                                print("Integrity Check failed\n\n")
                            else:
                                encryption = AES.new(key, AES.MODE_CBC, IV)
                                message = unpad(encryption.decrypt(encryptedMessage).decode())
                                print(f"Decryption Successfull!!\n\nMessage:\t{message}")
                                break
                        elif User["HashAlgo"] == "MD5":

                            key = md5(password.encode()).digest()

                            IV = base64.b64decode(User["IV"])
                            encryptedMessage = base64.b64decode(User["encryptedMessage"])
                            hashValue = User["hashValue"]

                            testHash = md5(encryptedMessage).hexdigest()
                            if testHash != hashValue:
                                print("Integrity Check failed\n\n")
                            else:
                                encryption = AES.new(key, AES.MODE_CBC, IV)
                                message = unpad(encryption.decrypt(encryptedMessage).decode())
                                print(f"Decryption Successfull!!\nMessage:\t{message}")
                                break
                        else:
                            print("EEERRROOORRR")
            if access == False:
                print("Username not found:(")

        elif command == 3:
            print("Exiting...")
            continue
        else:
            print("Choose either 1, 2, or 3\n")
            print("1.\tCreate a New User\n2.\tLogin to an Existing User\n3.\tExit\n")
    except:
        print("")