class SecretDiary:
    def __init__(self, diary):
        if type(diary) == str or type(diary) == int or type(diary) == dict or type(diary) == list:
            raise Exception("Only class instances are allowed!")
        else:          
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
