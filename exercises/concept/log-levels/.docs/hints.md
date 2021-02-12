# Hints

## General

- [Python Docs: Enum](https://docs.python.org/3/library/enum.html)

## 1. Parse log level

- Use [`str.split`](https://www.w3schools.com/python/ref_string_split.asp) to extract the log level from the message.
- With the extracted part of the string, access and return the enum member using `LogLevel(string)`.

## 2. Support unknown log level

- Create a new Unknown log level member in the existing enum.
- Check if the extracted part of the string is a value of the enum `LogLevel`.
- If the value does not match any of the enum member values, then return the Unknown member of `LogLevel`.

## 3. Convert log line to short format

- Find the code (an integer) of the log level based on the log level, multiple solutions are possible: if statements, another enum or any other solution.
- Use string formatting to return a properly formatted code level and message.

## 4. Create an Alias

- Create the new alias member named Warn in the existing enum.
- Return the newly created member.

## 5. All Member Names and Values

- Iterate on all the members of the enum and return a list of tuple.
- The tuple can be constructed with `(item1, item2)`.
- The name and value of the enum can be accessed with `member.name` and `member.value`.
- Return the list containing all the tuples.
