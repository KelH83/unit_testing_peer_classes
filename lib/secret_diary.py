class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked:
            raise Exception("Go away!")
        else:
            return self.diary

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
