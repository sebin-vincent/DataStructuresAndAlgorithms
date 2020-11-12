class Palindrome:
    start_pos = 0
    max_length = 1

    def expandAtChar(self, text, start, end):
        length = len(text)
        while start >= 0 and end < length and (text[start] == text[end]):
            start -= 1
            end += 1

        new_length = end - start - 1
        if self.max_length < new_length:
            self.max_length = new_length
            self.start_pos = start+1

    def find_lps(self, text):
        j = len(text)
        for i in range(0, j):
            self.expandAtChar(text, i, i)
            self.expandAtChar(text, i, i + 1)

        print(text[self.start_pos:(self.start_pos + self.max_length)])


obj = Palindrome()
obj.find_lps("aaba")
