from LWW import LWW

def test1():
  LWW1 = LWW()
  LWW1.add('element1')
  LWW1.add('element2')
  LWW1.remove('element1')
  LWW1.update()
  expected = ['element2']
  assert LWW1.set == expected

def test2():
  LWW1 = LWW()
  LWW1.add('element1')
  LWW1.add('element2')
  LWW1.remove('element1')
  LWW1.update()
  LWW2 = LWW()
  LWW2.add('element3')
  LWW1.merge_with(LWW2)
  LWW1.update()
  expected = ['element2', 'element3']
  assert LWW1.set == expected
  
def test3():
  LWW1 = LWW()
  LWW1.add('element1')
  LWW1.add('element2')
  LWW1.remove('element1')
  LWW1.update()
  LWW2 = LWW()
  LWW2.add('element3')
  LWW2.remove('element2')
  LWW1.merge_with(LWW2)
  LWW1.update()
  expected = ['element3']
  assert LWW1.set == expected

def test4():
  LWW1 = LWW(bias='add', time_precision=1)
  LWW1.add('element1')
  LWW1.add('element2')
  LWW1.remove('element1')
  LWW1.update()
  expected = ['element1', 'element2']
  assert LWW1.set == expected

def test5():
  LWW1 = LWW(bias='remove', time_precision=1)
  LWW1.add('element1')
  LWW1.add('element2')
  LWW1.remove('element1')
  LWW1.update()
  expected = ['element2']
  assert LWW1.set == expected

def main():
  test1()
  test2()
  test3()
  test4()
  test5()
  print('All tests passed')

main()