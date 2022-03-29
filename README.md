# username-generator
Generates various combinations of potential usernames from a list of first and last names
This is useful for guessing usernames from OSINT sources for CTF challenges and pentesting.

# Examples

Generate from a file

`python generate_usernames.py -i names.txt -o usernames.txt`

Generate from a single name

`python generate_usernames.py -N "Haicen Hacks"`

`-o` is optional, and will print to stdout if not provided.
