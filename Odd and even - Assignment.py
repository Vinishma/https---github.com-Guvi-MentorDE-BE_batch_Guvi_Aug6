def oddoreven():
  num = int(input ("Enter One Variable: "))
  if (num % 2) == 0:
      print ("The number is even")
  else:
      print ("The provided number is odd")
  def check_int(num):
    try:
      value_int = int(num)
      return 'Value is integer'
    except ValueError:
      return 'Not an integer'
  return check_int(num)
oddoreven()