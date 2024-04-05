import re

pattern = r'[^a-zA-Z0-9]'

def is_palindrome(str):
  plain = re.sub(pattern, '', str).lower()
 # print(plain)
  reversed = plain[::-1]
 # print(reversed)

  return plain == reversed


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
