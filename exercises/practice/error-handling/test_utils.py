class FileLike:
    def __init__(self, fail_something=True):
        self.is_open = False
        self.was_open = False
        self.did_something = False
        self.fail_something = fail_something

    def open(self):
        self.was_open = False
        self.is_open = True

    def close(self):
        self.is_open = False
        self.was_open = True

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def do_something(self):
        self.did_something = True
        if self.fail_something:
            raise Exception("Failed while doing something")