def main():
  n: int = int(input())
  print(f'{n if n % 2 == 0 else n * 2} casas brancas e {n} casas pretas')

if __name__ == '__main__':
  main()
