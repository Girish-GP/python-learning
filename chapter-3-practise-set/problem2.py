letter = '''
  Dear <|Name|>
  You are selected!
  <|Date|>
'''

name = input("enter name:")
dateTest = input("enter date:")
test =letter.replace('<|Name|>',name)
test = test.replace('<|Date|>',dateTest)
print(test)