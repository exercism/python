In this exercise you'll be processing log-lines.

Each log line is a string formatted as follows: `"[<LEVEL>]: <MESSAGE>"`.

There are three different log levels:

- `INFO`
- `WARNING`
- `ERROR`

You have three tasks, each of which will take a log line and ask you to do something with it.

## 1. Extract a message from a log line

Implement a function to return a log line's message:

```python
>>> extract_message("[ERROR]: Invalid operation")
'Invalid operation'
```

The message should be trimmed of any whitespace.

```python
>>> extract_message("[ERROR]: Invalid operation.\t\n")
'Invalid operation.'
```

## 2. Change a message's loglevel.

Implement a function that replaces a log line's current log level with a new one:

```python
>>> change_log_level("[INFO]: Fatal Error.", "ERROR")
'[ERROR]: Fatal Error.'
```

## 3. Reformat a log line

Implement a function that reformats the log line, putting the message first and the log level after it in parentheses:

```python
>>> reformat("[INFO]: Operation completed")
'Operation completed (info)'
```
