# Substitution-Cipher
A command-line interface for encryption and decryption using a substitution cipher.

## Run
To start using **Substitution-Cipher** run:

on windows
``` windows
python.exe main.py
```
on linux/mac
``` linux/mac
python3 main.py
```
## Usage
From the command line, use:
```Substitution-Cipher
keygen [-m]
[-m] - user manually writes in a key one letter at a time.
usekey <KEY>
- If a user has a key in mind they may input the entire key here to use it. 
whatiskey
- Prints currently loaded key
encrypt <MESSAGE>
decrypt <MESSAGE>
```

## **DESCRIPTION**
**substitution-cli** is a command-line tool that allows users to encrypt and decrypt messages using a **substitution cipher**. A substitution cipher replaces each letter of the alphabet with another letter based on a generated key.

Users can generate a key automatically or manually, input a custom key, and encrypt/decrypt messages based on the key.

## **COMMANDS**

### **keygen [-m]**
Generate a substitution cipher key.

- **Without `-m`**: The key is generated randomly.
- **With `-m`**: The user manually assigns each letter in the key.

---

### **usekey <KEY>**
Set a custom key for encryption and decryption. The key must be exactly **26 unique lowercase letters**.

#### **Example:**
```sh
usekey qwertyuiopasdfghjklzxcvbnm
```
If the key is invalid (wrong length or contains duplicates), an error message will be displayed.

---

### **whatiskey**
Display the current encryption key.

#### **Example:**
```sh
whatiskey
```
*(Outputs the current key if initialized, otherwise prompts the user to generate one.)*

---

### **encrypt <MESSAGE>**
Encrypts a given message using the substitution key.

- **Only lowercase English letters are supported.**
- **Spaces and punctuation are not transformed.**
- **Requires an initialized key.**

#### **Example:**
```sh
encrypt hello
```
*If the key is:*
```
qwertyuiopasdfghjklzxcvbnm
```
*Then output would be:*
```
itssg
```

---

### **decrypt <MESSAGE>**
Decrypts a given message using the substitution key.

- **Only lowercase English letters are supported.**
- **Requires an initialized key.**

#### **Example:**
```sh
decrypt itssg
```
*If the key is:*
```
qwertyuiopasdfghjklzxcvbnm
```
*Then output would be:*
```
hello
```

---

## **EXIT**
Press `Ctrl+C` (`^C`) to exit the program.

---

### Authors Note
This command-line-interface was written for an assignment in CUS-1185. This was my first time successfully managing to write a proper python CLI

-- Kristin Malone

### https://github.com/KMalone42/Substitution-Cipher
---