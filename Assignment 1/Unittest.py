import unittest
import collections

def test_getSubstringsInList(self):
    # Failure message:
    # Sorry, something went wrong
    iterable = "subsubstrings"
    tmpList = getSubstringsInList(iterable)

    myList = []
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            myList.append(iterable[index:index+size])

    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    self.assertEquals(compare(tmpList,myList), 1)


def test_substringsNoDubs(self):
# Failure message:
# Sorry but our lists do not match. Keep in mind this is only the bonus; you can submit anyway
    iterable = "subsubstrings"
    tmpList = set(getSubstringsInList(iterable))
    orgList = getSubstringsWithNoDubs(iterable)
            
    if len(tmpList) < 5:
        self.assertEquals(0, 1)
    
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    self.assertEquals(compare(tmpList,orgList), 1)
