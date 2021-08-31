taking = True
class_list = []
while taking:
    
    classes = input('What classes are you taking: ')
    class_list.append(classes)
    no_more = str(input('Are you taking more classes? press n if not ' ))
    if no_more == 'n':
        taking = False

for x in class_list:
    print(x)