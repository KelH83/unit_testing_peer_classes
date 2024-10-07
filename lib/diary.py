class Diary:
    def __init__(self, contents):
        if type(contents) != str:
            raise Exception("Only strings are allowed!")
        self.contents = contents

    def read(self):
        return self.contents
