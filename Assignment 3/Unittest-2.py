import re

def test_cleanupline(self):
# Failure message:
    x = "Really? This can't be true! 5.5% is too much (trust me)"
    s1 = cleanupLine(x)
    s2 = re.sub("[^a-zA-Z0-9']",' ', x)
    self.assertEquals(s1, s2)


def test_countWords(self):
# Failure message:
    x = "Hello my Friend  hello my other friend2 i really like my friends"
    dict = countWords(x)
    self.assertEquals(dict['hello'], 2)
    self.assertEquals(dict['my'], 3)
    self.assertEquals(dict['like'], 1)
    self.assertEquals(dict['friend2'], 1)


def test_countLetters(self):
# Failure message:
    x = "Hello my Friend  hello my other friend2 i really like my friends"
    letters = countLetters(x)
    self.assertEquals(letters['e'], 8)
    self.assertEquals(letters['l'], 7)
    self.assertEquals(letters['a'], 1)
    self.assertEquals(letters['y'], 4)


def test_results(self):
    # Failure message:
    mine = [6209,1566,1205,302,132,334]
    yours = results()
    if mine == yours:
        self.assertEquals(mine, yours)
    else:
        self.assertEquals("my number for e = 6209", "and for to=302")
