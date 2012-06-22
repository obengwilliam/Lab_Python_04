import string
print 'exerxise*************************************************************************'
#1a
groceries=['bananas','strawberries','apples','bread']
groceries.append('champagne')
print 'LIST'
print groceries

#1b
print
print
groceries.remove('bread')
print 'THis is the new list'
print groceries



#1c
print
print

messi_item=raw_input('please input item to obtain aisle: ')
messi_itemc=messi_item[:1]
letters=map(chr,range(97,123))
if messi_itemc in letters:
    print messi_item ,'can be found in aisle' ,messi_itemc




print
print

print 'Exercise 2******************************************************************'


#Exercise 2a




#Exercise 2b

item_price={'apples':'sphic_apples','bananas':'spic_bananas',
            'bread':'sphic_bread',
            'carrots':'spic_carrots',
            'champagne':'spic_champagne',
            'strawberries':'sphic_strawberries'
            }
print item_price

#Exercise 2c

print 'Modifing price in data structure'
item_price['strawberries']='wpic_strawberries'
print '\n\n\n\n\n\n\n\n'
print 'After modification we have this',item_price




#Exercise 2d

print 'adding chicken '

item_price['chicken']='spic_chicken'
print '\n\n'
print item_price




#Exercise 3a
print 'The tuple data sturcture can be used'




#Exercise 3b
#always_in_stock=('shoe','plates')
always_in_stock=tuple(item_price.keys())



#Exercise 3c
second_stock=('dictionary','spoon')

combined_stock=always_in_stock[:] + second_stock[:]

print  combined_stock



#EXERCISE 4
#a

print 'dictionaries can be used'

list_of=[45,67,89,90]
def binary_insert(new_float,list_of):
    length=len(list_of):
        







    return

#Exercise 5


























             
