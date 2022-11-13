def countdown(i):
  # Базовый случай
  if i <= 0:
    return 0
  # Рекурсивный случай
  else:
    print(i)
    return countdown(i-1)

countdown(5)