from functools import lru_cache
from time import sleep

try:
  user = int(input("Enter how many functions you want in your cache: "))

  @lru_cache(maxsize=user)
  def remaining_time(n):
    sleep(n)
    return f"After time {n}"

  print(remaining_time(3))
  print(remaining_time(2))
  print(remaining_time(5))
  print(remaining_time(3))
  print(remaining_time(2))

except Exception as e:
  print(e)