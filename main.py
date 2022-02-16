'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  '''
      Determina daca un numar este Prim
      :param n: int
      :return: true daca e prim false in caz contrar
      '''
  if n < 2:
    return False
  else:
    x = 2
    while x != n:
      if n % x == 0:
        return False
      x += 1
  return True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  '''

  :param lst:
  :return: Returneaza produsul numerelor din lista lst.
  '''
  if len(lst) == 0:
    p=0
  else:
    p=1
  i=0
  while i < len(lst):
    p *= lst[i]
    i +=1
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  '''

  :param x:
  :param y:
  :return: Returneaza CMMDC a doua numere x si y
  '''
  if x != y:
    if x > y:
      x=x-y
    else:
      y=y-x
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  '''

  :param x:
  :param y:
  :return: Returneaza CMMDC a doua numere x si y
  '''
  while y > 0:
    r = x % y
    x=y
    y=r
  return x
  
def main():
  while True:
    print('1. Numar prim')
    print('2. Produsul unei liste.')
    print('3. Cmmdc.1.')
    print('4. Cmmdc.2.')
    print('x. Ieșire.')
    optiune = input('Alege optiunea: ')
    if optiune == '1':
      x = int(input("Introduceti un numar"))
      print(is_prime(x))
    elif optiune == '2':
      lst = []
      n = int(input("introduceti numarul de elemente : "))
      for i in range(0, n):
        ele = int(input())
        lst.append(ele)
      print(get_product(lst))
    elif optiune == '3':
      x = int(input("Introduceti un numar x:"))
      y = int(input("Introduceti un numar y:"))
      print(get_cmmdc_v1(x,y))
    elif optiune == '4':
      x = int(input("Introduceti un numar x:"))
      y = int(input("Introduceti un numar y:"))
      print(get_cmmdc_v2(x, y))
    elif optiune == 'x':
      break
    else:
      print('Optiune invalida!')

if __name__ == '__main__':
  main()
