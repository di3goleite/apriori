newlist = [[['1'], ['2']], [['3'], ['4']], [['5'], ['6']]]
final = []

def generate(newlist, number):
  count = 0
  final = []
  while count < len(newlist)-1:
    sublist1 = newlist[count]
    sublist2 = newlist[count+1]

    for word1 in sublist1:              # Iterate all sublist1
      for word2 in sublist2:            # Iterate all sublist2
        if number == 0:
          templist = [word1] + [word2]
        else:
          templist = word1 + word2

        #print list(set(templist2))
        final.append(templist)   # Appends the templist1
    count = count + 1           # Update the value of the count variable
  return final

final = generate(newlist, 0)
final = generate(final, 1)
#print '################################# Final'
#print final
# Search if all elements of the list1 are conteined in the list2
list1 = [1,2,3,4]
list2 = [1,2,3,4,5]
if all( ( x in list1 for x in list2 ) ):
  print 'List2 in List1'
# Solve the sum
# In: [['normal'], ['FALSE'], ['FALSE'], ['no']]
# Out:['normal', 'FALSE', 'FALSE', 'no']
# templist2 = [item for sublist in templist2 for item in sublist]

