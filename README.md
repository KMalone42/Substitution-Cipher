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

Additionally to run **lfa.py** run:

on windows
```
python.exe lfa.py -f inputfile.txt -o outputfile.txt
```

on linux/mac
``` linux/mac
python3 lfa.py -f inputfile.txt -o outputfile.txt
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
encrypt -f <inputfile.txt> -o <outputfile.txt>
decrypt <MESSAGE>
decrypt -f <inputfile.txt> -o <outputfile.txt>
```

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

### **encrypt [-f] <FILENAME> [-o] <FILENAME>**
Encrypts contents of a given file using the substitution key.

- **Only lowercase English letters are supported.**
- **Spaces and punctuation are not transformed.**
- **Requires an initialized key.**
- **Only supports text formatted as UTF-8.**
- **-o argument is optional, default file output is called 'encrypted.txt'**

#### **Example:**
```sh
encrypt -f Corpus.txt -o EncryptedCorpus.txt
```

Running this may take a minute depending on the length of the input file text.

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

### **decrypt [-f] <FILENAME> [-o] <FILENAME>**
Decrypts contents of a given file using the substitution key.

- **Only lowercase English letters are supported.**
- **Spaces and punctuation are not transformed.**
- **Requires an initialized key.**
- **Only supports text formatted as UTF-8.**
- **-o argument is optional, default file output is called 'decrypted.txt'**

#### **Example:**
```sh
decrypt -f Corpus.txt -o EncryptedCorpus.txt
```

Running this may take a minute depending on the length of the input file text.

---
## **EXIT**
Press `Ctrl+C` (`^C`) to exit the program.

---

### Authors Note
This command-line-interface was written for an assignment in CUS-1185. This was my first time successfully managing to write a proper python CLI

-- Kristin Malone

### https://github.com/KMalone42/Substitution-Cipher
---