Drink = ['cola','mike','coffee','water']
print(Drink)
print(len(Drink))
print(Drink[2])
Drink.append('juice')
print(Drink)
Drink.pop()
'juice'
print(Drink)
Drink.extend(['apple juice','orange juice'])
print(Drink)
Drink.remove('mike')
print(Drink)
Drink.insert(2,'mike')
print(Drink)
Drink.insert(1,'500ml')
print(Drink)

Drink = ['cola', 'mike', 'coffee', 'water',
         ['num_Drink = len(Drink)',
          ['apple juice', 'orange juice']]]

for each_item in Drink:
          if isinstance(each_item,list):
              for nested_item in each_item:
                  if isinstance(nested_item,list):
                     for deeper_item in nested_item:
                         print(deeper_item)
                  else:
                       print(nested_item)
          else:
                print(each_item)
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

