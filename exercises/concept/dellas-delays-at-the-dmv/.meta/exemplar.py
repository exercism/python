# really just a stub right now

def line_length(oclock):
    if oclock == 9 or oclock == 4:
        return 10
    if oclock == 12:
        return 20
    return 5


def wait_minutes(oclock):
    return line_length(oclock) * 5
  
wait_time = wait_minutes

def respond(greeting):
    response = greeting
    secret_thought = ""

    def thinking():
        nonlocal secret_thought
        if greeting.startswith("Good"):
            secret_thought = "What's good about it?"
        else:
            secret_thought = "I wish you would go away!"
    thinking()
    return f"{response} {secret_thought}"
