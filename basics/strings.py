s1 = 'This is a string'
s2 = """This is a multi-line string.
It can span multiple lines.
Interesting."""
sub = "text"

# List of string methods
print(dir(str))


print(help(str))

# function to get length of string
len(s1)  # 16

# function to convert string to uppercase
s1.upper()  # 'THIS IS A STRING'

# function to replace a substring
s1.replace('string', 'text')  # 'This is a text'

# Case Conversion Methods
s1.capitalize()      # First letter uppercase
s1.casefold()        # Strong lowercase (for comparisons)
s1.lower()           # Convert to lowercase
s1.upper()           # Convert to uppercase
s1.swapcase()        # Swap case (uppercase to lowercase and vice versa)
s1.title()           # Title case

# String Search Methods
s1.find(sub)         # Returns index (or -1)
s1.rfind(sub)        # Find from right
s1.index(s1)       # Like find() but error if not found
s1.rindex(sub)      # Reverse index
s1.count(sub)       # Count occurrences

# Check / Validation Methods (Return True/False)
s1.isalnum()         # Alphanumeric
s1.isalpha()         # Alphabet only
s1.isascii()         # ASCII characters only
s1.isdecimal()       # Decimal numbers
s1.isdigit()         # Digits
s1.isnumeric()       # Numeric
s1.isidentifier()    # Valid variable name
s1.islower()         # Lowercase check
s1.isupper()         # Uppercase check
s1.isspace()         # Only whitespace
s1.istitle()         # Title case check
s1.isprintable()     # Printable characters

# Strip / Remove Methods
s1.strip()           # Remove whitespace from both ends
s1.lstrip()          # Remove whitespace from the left
s1.rstrip()          # Remove whitespace from the right
s1.removeprefix()    # Remove prefix (Python 3.9+)
s1.removesuffix()    # Remove suffix (Python 3.9+)

# Replace & Modify Methods
s1.replace(old, new)  # Replace occurrences of a substring
s1.split(sep)        # Split into a list (default is whitespace)
s1.join(iterable)    # Join elements of an iterable into a string
s1.format(*args, **kwargs)  # Format string (Python 3.6+)
s1.translate(table)  # Translate characters using a translation table
s1.maketrans()       # Create a translation table
s1.expandtabs()      # Expand tabs in a string

# Split & Join Methods
s1.split()           # Split into list
s1.rsplit()          # Split from right
s1.splitlines()      # Split by line
s1.partition()       # Split into 3 parts
s1.rpartition()      # Reverse partition
s1.join(iterable)    # Join list into string