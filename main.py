import array as arr
import random
import time
import cmd
import os

class CLI(cmd.Cmd):
    alphabet = arr.array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    key = [''] * 26

    def reinit_key(self):
        self.key = [''] * 26

    def do_usekey(self, arg):
        # argument is the key that the user wants to use written as string
        potential_key = list(arg)
        if len(potential_key) != 26:
            print(f"{arg}\nis not a valid key, key length should be = to 26")
        for char in potential_key:
            index = potential_key.index(char)
            # Just gonna do a switch statement i guess
            if char not in self.alphabet:
                print(f"{char} is not a valid input")
                print("input characters must be lowercase and apart of the standard english alphabet")
                return
            elif potential_key.count(char) > 1:
                print(f"{char} is not valid")
                print("duplicate keypairs not accepted.")
                return
        self.key = potential_key

    def do_keygen(self, arg):
        if '-m' in arg:
            self.keygen_manual()
        else:
            self.keygen()

    def keygen(self):
        self.reinit_key()
        # Randomly generates your key
        start_time = time.perf_counter()
        for index, letters in enumerate(self.alphabet):
            random_integer = random.randint(0,25)
            if self.alphabet[random_integer] in self.key:
                duplicate = True

                # This is a really stupid duplicate check that can
                # Run infinetely, however computers are fast
                while duplicate:
                        random_integer = random.randint(0,25)
                        if self.alphabet[random_integer] not in self.key:
                            duplicate = False

            self.key[index] = self.alphabet[random_integer]
        print("generated key in %s seconds" % (time.perf_counter() - start_time))

    def keygen_manual(self):
        # Manually write your key out
        # Need to refactor these functions for this
        self.reinit_key()
        for index, letters in enumerate(self.alphabet):
            # Do a thing, take an input and create a second array. 
            # I think that self.alphabet[letters] should output a string
            inp = self.validateinput(self.alphabet[index], index)
            self.key[index] = inp

    def validateinput(self, letter, index):
        valid = False
        while valid is False:
            inp = input(f"substitute '{letter}' with an unused letter")
            if inp not in self.alphabet: # passed test
                print(f"{inp} is not a valid input")
                print("input must be lowercase and apart of the standard english alphabet")
                continue
            elif inp in self.key: # passed test
                print(f"{inp} is not valid")
                print("duplicate keypairs not accepted.")
                print(f"Used keypairs: {self.key[:index]}")
                continue
            valid = True
            return inp

    def do_whatiskey(self, arg):
        try:
            if '' in self.key:
                print("Key not initialized try 'keygen' or 'keygen -m' for manual key generation")
            else:
                print(''.join(map(str, self.key)))
        except:
            print("Key not initialized try 'keygen' or 'keygen -m' for manual key generation")
    
    def whatiskey(self):
        try:
            if '' in self.key:
                print("Key not initialized try 'keygen' or 'keygen -m' for manual key generation")
                return False
            else:
                print(''.join(map(str, self.key)))
                return True
        except:
            print("Key not initialized try 'keygen' or 'keygen -m' for manual key generation")
            return False

    def do_encrypt(self, arg):
        if not self.whatiskey():
            return
        print(''.join(self.alphabet))

        args = arg.split(' ')  # Handle multiple arguments properly
        output_file = "encrypted.txt"  # Default output filename

        if '-f' in args:
            try:
                file_index = args.index('-f') + 1
                filename = args[file_index]

                if not os.path.exists(filename):
                    print(f"[!] File '{filename}' not found.")
                    return
                with open(filename, 'r', encoding='utf-8') as file:
                    plaintext = file.read().lower()  # Convert to lowercase

                # Encrypt the text
                encrypted_text = ''.join(self.key[self.alphabet.index(c)] if c in self.alphabet else c for c in plaintext)

                if '-o' in args:
                    output_index = args.index('-o') + 1
                    if output_index < len(args):
                        output_file = args[output_index]  # Set the custom output filename

                # Save to file
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(encrypted_text)
                print(f"[✓] Encrypted content saved to '{output_file}'")
            except (IndexError, ValueError):
                print("[!] Error: Missing filename after '-f' or '-o'")
        else:
            message = arg.lower() # Convert to lowercase
            encoded_message = [self.key[self.alphabet.index(c)] if c in self.alphabet else c for c in message]
            print("".join(encoded_message))

    def do_decrypt(self, arg):
        if not self.whatiskey():
            return
        print(''.join(self.alphabet))

        args = arg.split(' ')  # Handle multiple arguments properly
        output_file = "encrypted.txt"  # Default output filename

        if '-f' in args:
                    try:
                        file_index = args.index('-f') + 1
                        filename = args[file_index]

                        if not os.path.exists(filename):
                            print(f"[!] File '{filename}' not found.")
                            return
                        with open(filename, 'r', encoding='utf-8') as file:
                            ciphertext = file.read().lower()

                        # Decrypt the text
                        decrypted_text = ''.join(self.alphabet[self.key.index(c)] if c in self.key else c for c in ciphertext)

                        if '-o' in args:
                            output_index = args.index('-o') + 1
                            if output_index < len(args):
                                output_file = args[output_index]  # Set the custom output filename

                        # Save to file
                        with open(output_file, 'w', encoding='utf-8') as file:
                            file.write(decrypted_text)
                        print(f"[✓] decrypted content saved to '{output_file}'")
                    except (IndexError, ValueError):
                        print("[!] Error: Missing filename after '-f' or '-o'")
        else:
            message = arg.lower()
            decoded_message = [self.alphabet[self.key.index(c)] if c in self.key else c for c in message]
            print("".join(decoded_message))
# runtime starts here
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    try:
        CLI().cmdloop()
    except KeyboardInterrupt:
        print("\n^C")