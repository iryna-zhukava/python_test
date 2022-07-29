import unittest



class TestStringMethods(unittest.TestCase):

  def test_new_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')
  def test__new_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())
  def test__new_isupperNew(self):
      self.assertTrue(1 == 2)
      self.assertFalse('Foo'.isupper())
  def test_new_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()