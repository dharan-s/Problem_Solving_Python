#String Compression
#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

#from nose.tools import assertEqual
import unittest

def compress(s):
	#s = "AAABCCDDDDD"
	out=""
	l = len(s)
	if len == 0:
		return('')
	elif len == 1:
		return(s+"1")
	else:
		a=set(s)
		for i in s:
			if(i in a):
				a.remove(i)
				out+=i+str(s.count(i))
		return(out)
		


class TestCompress(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol(''), '')
        self.assertEqual(sol('AABBCC'), 'A2B2C2')
        self.assertEqual(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)
