class inMemoryDB:

    def __init__(self):
        self.dict = {}
        self.buffer = []
        self.transaction = False


    def get(self, key):

        if not isinstance(key, str):
            return "Keys must be strings, try again loser!"

        if key in self.dict:
            return self.dict[key]

        else:
            return None

    def put(self, key, value):

        if not isinstance(key, str):
            return "Keys must be strings, try again loser!"

        if not isinstance(value, int):
            return "Values must be integers, try again loser!"

        if self.transaction:
            self.buffer.append(key)
            self.buffer.append(value)

        else:
            return "Cannot place items into the buffer without starting a transaction, lock in bruh"


    def begin_transaction(self):

        if not self.transaction:
            self.buffer.clear()
            self.transaction = True

        else:
            return "Transaction has already been started dummy"

    def commit(self):

        if self.transaction:

            if not self.buffer:
                return "No changes have been stored in the buffer, lock in bruh"

            for i in range(0, len(self.buffer), 2):
                self.dict[self.buffer[i]] = self.buffer[i + 1]

            self.transaction = False
            self.buffer.clear()

        else:
            return "No transaction has been started bro"

    def rollback(self):

        if not self.transaction:
            return "No transaction has been started bro"

        self.buffer.clear()
        self.transaction = False

