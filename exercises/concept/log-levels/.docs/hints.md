## General

- [Python Docs: Enum](https://docs.python.org/3/library/enum.html)

## 1. Parse log level

- You need to use string splits to split the log message to multiple parts.
- Once you have the required part of the string split you can use LogLevel(`string`) to return

## 2. Support unknown log level

- You need to first check if the value is in the LogLevel enum before calling LogLevel(`string`) and return.

## 3. Convert log line to short format

- You need to do an if else with all the members of the LogLevel and return the String along with the int value as per the given format. ( You need to use a `==` operator )

## 4. Create an Alias

- You just have to return the newly created alias value to the function output.

## 5. All Member Names and Values

- You need to iterate over all the members in the enum and return a tuple containing (member.name, member.value) in a list.
