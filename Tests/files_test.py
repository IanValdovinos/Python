print('Hello there')

with open('my_txt.txt', 'w') as txt_file:
  txt_file.write('Hello txt!')

txt_file = open('my_txt.txt')
content = txt_file.read()
print(content)
