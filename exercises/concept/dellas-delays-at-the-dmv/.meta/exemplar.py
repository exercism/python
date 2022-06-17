# really just a stub right now

def line_length(oclock):
    if oclock == 9 or oclock == 4:
        return 10
    if oclock == 12:
        return 20
    return 5


def wait_minutes(oclock):
    return line_length(oclock) * 5
  
