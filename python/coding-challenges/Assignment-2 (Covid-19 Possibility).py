
age = input ('Are you a cigarette addict older than 75 years old? ')
print(end='\n')
print(bool(age))
chronic = input ('Do you have a severe chronic disease?')
print(end='\n')
print(bool(chronic))
immune = input ('Is your immune system too weak?')
print(end='\n')
print(bool(immune))
print(end='\n')
risk = bool(age) and bool(chronic) and bool(immune)
print(bool(risk))
print(end='\n')
if risk == True:
   print('There is a risk of death')
else: 
   print('There is not a risk of death')

