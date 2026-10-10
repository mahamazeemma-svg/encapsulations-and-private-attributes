class book:
    def __init__(self,name,writer,pages):

        self.name = name
        self.writer = writer
        self.pages = pages

    def __len__(self):
        return self.pages

b = book("Harry potter","J.K rowling",378)
print(len(b))