import array as arr
import random
import time
import cmd

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


    # encrypt a message using the key
    def do_encrypt(self, arg):
        # obligatory check for a key being loaded
        if not self.whatiskey():
            return
        print(''.join(self.alphabet))
        message = list(arg)
        encoded_message = []
        for char in message:
            index = self.alphabet.index(char)
            encoded_message.append(self.key[index])
        
        print(''.join(map(str, encoded_message)))


    
    # decrypt a message using the key
    def do_decrypt(self, arg):
        # obligatory check for a key being loaded
        if not self.whatiskey():
            return
        print(''.join(self.alphabet))
        message = list(arg)
        decoded_message = []
        for char in message:
            index = self.key.index(char)
            decoded_message.append(self.alphabet[index])
        
        print(''.join(map(str, decoded_message)))

# runtime starts here
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    try:
        CLI().cmdloop()
    except KeyboardInterrupt:
        print("\n^C")