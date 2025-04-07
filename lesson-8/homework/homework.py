def divideing(a,b):
 try:
    return a/b
 except ZeroDivisionError:
   return 'ZeroDivisionError'
 except TypeError:
   
   return'TypeError'
def integer():
 try:
    a=int(input(' int : '))
    return a/b
 except ValueError:
   return 'valuerror'
 except TypeError:
   return'TypeError'
def fileopening(a):
 try:
   with open(f'{a}','r') as f:
     r=f.readline()
     return r
 except FileNotFoundError:
   return 'Filerror'
 except PermissionError:
   return'permission error'
def listt(a):
  kk=[1,2,3,4,4]
  try:
    kk[a]
  except IndexError:
    return 'IndexError'

  try:
    number = input("Enter a number: ")
    print(f"You entered: {number}")
  except KeyboardInterrupt:
    print("\nInput cancelled by user. Exiting...")
  

try:
    number = input("Enter a number: ")
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("\nInput cancelled by user. Exiting...")
def divideing(a,b):
 try:
    return a/b
 except ArithmeticError:
   return 'ArithmeticError'
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()  
    print(content)
except UnicodeDecodeError as e:
    print(f"Unicode decoding error: {e}")
except FileNotFoundError:
   print("ffff")
class Car:
    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")
try:
  
    print(car.model)  
except AttributeError as e:
    print(f"Attribute error: {e}")

with open('actors.json','r') as t:
    e=t.read()
with open('text.txt','w') as f:
    d=f.write(e)
with open('text.txt','w') as f:
    d=f.write('cvbcvbcvbcvbn\nsdfsdgsdgsg\nsrthshshsgh')
print(d)
with open('text.txt','r') as f:
    d=f.read()
with open('text.txt','r') as f:
    d=f.readline()
print(d)
#Write a Python program to read last n lines of a file.
def file(a,b):
    try :
        with open(a,'r') as d:
            t=d.readlines(-1)
            return t[b]
    except Exception as f:
        return 'Exception'
#Write a Python program to read a file line by line and store it into a list.
def file(a,b=0):
    y=[]
    try :
        with open(a,'r') as d:
            t=d.readlines()
            for i in  t:
                print( i)
                y.append(i)
            return y
    except Exception as f:
        return 'Exception'
#Write a Python program to read a file line by line and store it into a variable.
def file(a,b=0):
    y=' '
    try :
        with open(a,'r') as d:
            t=d.readlines()
            for i in  t:
                print( i)
                y+=' '+i
            return y
    except Exception as f:
        return 'Exception'
#Write a Python program to read a file line by line and store it into an array
def file(a,b=0):
    y=[]
    try :
        with open(a,'r') as d:
            t=d.readlines()
            for i in  t:
                print( i)
                y.append(i)
            return y
    except Exception as f:
        return 'Exception'
#Write a Python program to find the longest words.
def file(a,b=0):
    y=0
    try :
        with open(a,'r') as d:
            t=d.readlines()
            for i in t:
                print((i))
                if len(i)>y:
                    y=len(i)
                else:
                    break
            return y,i
    except Exception as f:
        return 'Exception'
#Write a Python program to count the number of lines in a text file.
def file(a,b=0):
    y=0
    try :
        with open(a,'r') as d:
            t=d.readlines()
            for i in t:
                y+=1
            return y
    except Exception as f:
        return 'Exception'
#Write a Python program to count the frequency of words in a file.
from collections import Counter
def file(a,b=0):
    try :
       with open(a,'r') as d:
            text=d.read().lower()
            words=text.split("\n")
            word_count = Counter(words)
            print(word_count)
    except Exception as f:
        return 'Exception'
    for word, count in word_count.items():
            print(f'{word}: {count}')
#Write a Python program to get the file size of a plain file.
import os
def file1(a,b=0):
    try :
       file_size = os.path.getsize(a)
       return file_size
    except Exception as f:
        return 'Exception'
#Write a Python program to write a list to a file.
def file2(a,b):
    try :
      with open(a,'w') as d:
        for i in b:
         print(i)
         g=d.write('\n'+i) 
         
      return g,i
    except Exception as f:
        return 'Exception'
my_list = ['apple', 'banana', 'cherry', 'date']
#Write a Python program to copy the contents of a file to another file.
def file2(a,b):
    try :
      with open(a,'r') as d:
          r=d.read()
      with open(b,'w') as h:
          t=h.write(r)
          return t
    except Exception as f:
           return 'Exception'
#Write a Python program to combine each line from the first file with the corresponding line in the second file.
def combine_files(file1, file2, output_file):
    try:
        # Open both files and the output file
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as output:
            # Read both files line by line
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            # Find the maximum number of lines in either file
            max_lines = max(len(lines1), len(lines2))

            # Combine corresponding lines
            for i in range(max_lines):
                line1 = lines1[i].strip() if i < len(lines1) else ""
                line2 = lines2[i].strip() if i < len(lines2) else ""
                output.write(f"{line1} {line2}\n")

        print(f"Combined lines written to {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
import random
#Write a Python program to read a random line from a file.
def file(a):
   
    try :
         with open(a, 'r', encoding='utf-8') as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Check if the file is not empty
            if lines:
                # Select a random line
                random_line = random.choice(lines).strip()
                print(f"Random line from the file: {random_line}")
    except Exception as f:
        return 'Exception'
#Write a Python program to assess if a file is closed or not.
def check_if_file_closed(filename):
    try:
        # Open the file
        file = open(filename, 'r', encoding='utf-8')
        
        # Check if the file is closed
        if file.closed:
            print(f"The file '{filename}' is closed.")
        else:
            print(f"The file '{filename}' is open.")
        
        # Close the file after checking
        file.close()
        
        # Re-check if the file is closed after closing it
        if file.closed:
            print(f"After closing, the file '{filename}' is closed.")
        
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    #kk 
def combine_files(file1, file2, output_file):
    try:
        # Open both files and the output file
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as output:
            # Read both files line by line
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            # Find the maximum number of lines in either file
            max_lines = max(len(lines1), len(lines2))

            # Combine corresponding lines
            for i in range(max_lines):
                line1 = lines1[i].strip() if i < len(lines1) else ""
                line2 = lines2[i].strip() if i < len(lines2) else ""
                output.write(f"{line1} {line2}\n")

        print(f"Combined lines written to {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
#Write a Python program to remove newline characters from a file.
def newline(a):
    with open(a,'r')as f:
        d=f.read()
        r=d.replace("\n",'')
    with open(a,'w') as f:
        d=f.write(r)
        return d
#Write a Python program that takes a text file as input and returns the number of words in a given text file.
def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    word_count = count_words_in_file(filename)
    if word_count is not None:
        print(f"The number of words in '{filename}' is {word_count}.")
import os

def extract_characters_from_files(file_list):
    characters = []
    for filename in file_list:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                characters.extend(list(content))  # Add each character to the list
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred while reading {filename}: {e}")
    return characters

if __name__ == "__main__":
    # Example usage: enter file names separated by commas
    input_files = input("Enter file names separated by commas: ").split(',')
    input_files = [f.strip() for f in input_files]  # Remove extra spaces
    character_list = extract_characters_from_files(input_files)
    
    print("Characters extracted:")
    print(character_list)
import string

def generate_alphabet_files():
    for letter in string.ascii_uppercase:  
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
    print("26 files A.txt to Z.txt have been created.")

if __name__ == "__main__":
    generate_alphabet_files()
import string

def create_alphabet_file(letters_per_line, output_filename="alphabet.txt"):
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    
    with open(output_filename, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i+letters_per_line]
            file.write(line + '\n')
    
    print(f"File '{output_filename}' created with {letters_per_line} letters per line.")

if __name__ == "__main__":
    try:
        n = int(input("Enter number of letters per line: "))
        create_alphabet_file(n)
    except ValueError:
        print("Please enter a valid integer.")
