import randStr


def test_randWord(self):
    # Failure message:
    # Tests if random word is returned
    s1 = "Hello, this is my test string and should only be one word in return"
    t1 = randStr.randWord(s1, "a")
    t3 = randStr.randWord(s1, "b")
    t4 = randStr.randWord(s1, 5)
    t5 = randStr.randWord(s1)
    t6 = randStr.randWord(s1)
    t2 = randStr.randWord(s1, "a")

    self.assertEquals(t1, t2)
    self.assertFalse(t3==t1)
    self.assertFalse(t4==t5)
    self.assertFalse(t2==t6)

def test_strMixer_word(self):
# Failure message:
# Verify words mixing
    s1 = "FRANK"
    t1 = randStr.strMixer(s1)
    t2 = randStr.strMixer(s1)
    t3 = randStr.strMixer(s1)
    t4 = randStr.strMixer(s1)
    self.assertFalse(t1 == t2 == t3 == t4)

    t1 = randStr.strMixer(s1,9)
    t2 = randStr.strMixer(s1,9)
    t3 = randStr.strMixer(s1,9)
    t4 = randStr.strMixer(s1,9)
    self.assertTrue(t1 == t2 == t3 == t4)

def test_strMixer_string(self):
    # Failure message:
    # testing strings
    s1 = "Hello, this is my test string and should only be one word in return"
    t1 = randStr.strMixer(s1)
    t2 = randStr.strMixer(s1)
    t3 = randStr.strMixer(s1)
    t4 = randStr.strMixer(s1)
    self.assertFalse(t1 == t2 == t3 == t4)
    
    t1 = randStr.strMixer(s1,9)
    t2 = randStr.strMixer(s1,9)
    t3 = randStr.strMixer(s1,9)
    t4 = randStr.strMixer(s1,9)
    self.assertTrue(t1 == t2 == t3 == t4)

def test_randIntForWord(self):
# Failure message:
# Tests the random numbers for word
    n1_0 = randStr.randIntForWord("hello")
    n2_0 = randStr.randIntForWord("")
    n3_0 = randStr.randIntForWord(55)
    n1_1 = randStr.randIntForWord("hello")

    if n1_0 > 100000 or n2_0 > 100000 or n3_0 > 100000 or n1_1 > 100000:
        self.assertEquals("values shouldn't be", "larger than 100000")

    self.assertTrue(n1_0 == n1_1)
    self.assertFalse(n1_0 == n2_0)
    self.assertFalse(n2_0 == n3_0)
    self.assertFalse(n1_1 == n3_0)

    n1 = randStr.randIntForWord("hello", "s")
    n2 = randStr.randIntForWord("hello", "s")
    self.assertTrue(n2 == n1)

    n1 = randStr.randIntForWord("hello", "s")
    n2 = randStr.randIntForWord("hello", "t")
    n3 = randStr.randIntForWord("hello", "x")
    self.assertFalse(n2 == n1 == n3)
