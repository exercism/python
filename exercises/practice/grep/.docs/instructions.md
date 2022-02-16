# Instructions

Search a file for lines matching a regular expression pattern. Return the line
number and contents of each matching line.

The Unix [`grep`](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/grep.html) command can be used to search for lines in one or more files
that match a user-provided search query (known as the *pattern*).

The `grep` command takes three arguments:

1. The pattern used to match lines in a file.
2. Zero or more flags to customize the matching behavior.
3. One or more files in which to search for matching lines.

Your task is to implement the `grep` function: given a list of files, find all
lines that match the specified pattern.
Return the lines in the order they appear in the files.
You'll also have to handle options (given as flags), which control how matching
is done and how the results are to be reported.

As an example, suppose there is a file named "input.txt" with the following contents:

```text
hello
world
hello again
```

If we were to call `grep "hello" input.txt`, the result should be:

```text
hello
hello again
```

If given multiple files, `grep` should prefix each found line with the file it was found in.
As an example:

```text
input.txt:hello
input.txt:hello again
greeting.txt:hello world
```

If given just one file, this prefix is not present.

## Flags

As said earlier, the `grep` command should also support the following flags:

- `-n` Prefix each matching line with its line number within its file.
  When multiple files are present, this prefix goes *after* the filename prefix.
- `-l` Print only the names of files that contain at least one matching line.
- `-i` Match line using a case-insensitive comparison.
- `-v` Invert the program -- collect all lines that fail to match the pattern.
- `-x` Only match entire lines, instead of lines that contain a match.

If we run `grep -n "hello" input.txt`, the `-n` flag will require the matching
lines to be prefixed with its line number:

```text
1:hello
3:hello again
```

And if we run `grep -i "HELLO" input.txt`, we'll do a case-insensitive match,
and the output will be:

```text
hello
hello again
```

The `grep` command should support multiple flags at once.

For example, running `grep -l -v "hello" file1.txt file2.txt` should
print the names of files that do not contain the string "hello".
