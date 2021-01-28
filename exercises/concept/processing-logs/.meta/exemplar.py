import re

LOGLINE_RE = r"\[(?P<level>INFO|ERROR|WARN)\] (?P<msg>.*)"


def _extract_pieces(message):
    pieces = re.search(LOGLINE_RE, message)
    return pieces.group("level"), pieces.group("msg")

def _extract_pieces_no_regex_groups(message):
    words = [word for word in re.split("[\s\[\]]", message) if word]
    return words[0], " ".join(words[1:])

def _extract_pieces_no_regex(message):
    words = [word for word in message.strip().replace("]", "[").split("[") if word]
    return words[0], words[1].strip()

def change_log_level(message, new_loglevel):
    """Change loglevel of message to new_loglevel."""
    return f"[{new_loglevel}] {extract_message(message)}"

def extract_message(message):
    return _extract_pieces_no_regex(message)[1]

def reformat(message):
    loglevel, msg = _extract_pieces_no_regex_groups(message)
    return f"{msg} ({loglevel.lower()})"
