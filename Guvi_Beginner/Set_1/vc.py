let=input()
v=['a','e','i','o','u','A','E','I','O','U']
if (ord(let)>64 and ord(let)<91) or (ord(let)>96 and ord(let)<123):
  if let in v:
    print('Vowel')
  else:
    print('Consonant')
else:
  print('Invalid')
