In this exercise you'll be processing log-lines.

Each log line is a string formatted as follows: `"[<LVL>]: <MESSAGE>"`.

These are the different log levels:

- `TRC` (trace)
- `DBG` (debug)
- `INF` (info)
- `WRN` (warning)
- `ERR` (error)
- `FTL` (fatal)

You have three tasks.

## 1. Parse log level

Define a `LogLevel` enum that has six elements corresponding to the above log levels.

- `Trace`
- `Debug`
- `Info`
- `Warning`
- `Error`
- `Fatal`

Defind the `parse_log_level` function which will take the 1 parameter, the log message. Return the Type of Log Level the log message belongs to.

Note: The `LogLevel` enum has to be defined on top of the file (outside the function).

```python
parse_log_level("[INF]: File deleted")
#=> LogLevel.Info
```

## 2. Support unknown log level

Unfortunately, occasionally some log lines have an unknown log level. To gracefully handle these log lines, add an `Unknown` element to the `LogLevel` enum which should be returned when parsing an unknown log level:

```python
parse_log_level("[XYZ]: Overly specific, out of context message")
#=> LogLevel.Unknown
```

## 3. Convert log line to short format

The log level of a log line is quite verbose. To reduce the disk space needed to store the log lines, a short format is developed: `"[<ENCODED_LEVEL>]:<MESSAGE>"`.

The encoded log level is simple mapping of a log level to a number:

- `Trace` - `0`
- `Debug` - `1`
- `Info` - `4`
- `Warning` - `5`
- `Error` - `6`
- `Fatal` - `7`
- `Unknown` - `42`

Define the `convert_to_short_log()` which takes 2 parameters.

1. Log level - The Log level of the log sent. ex: LogLevel.Error
2. Log Message

```python
convert_to_short_log(LogLevel.Error, "Stack overflow")
# => "6:Stack overflow"
```

## 4. Create an Alais

It looks like the user has created logs for `LogLevel.Warn` instead of `LogLevel.Warning`. Create an `alias` for `LogLevel.Warning` and return the alias name. This can be done on the same enum class you have defined at the top of the file.

Note: Both the LogLevels should point to same value. ie: LogLevel.Warning = "WRN" & LogLevel.Warn = "WRN"

```python
return_alias()
#=> LogLevel.Warn
return_alias() == LogLevel.Warning
#=> True
```

## 5. All Member Names and Values

Define the function `return_members()` that will take 1 parameter.

1. This parameter will take a randomly created enum.

You should return the (name, value) in tuple format of all the members in a list.

```python

class Color(enum.Enum):
    RED = 'red'
    GREEN = 'green'

return_members(Color)
#=> [('RED', 'red'), ('GREEN', 'green')]
```
