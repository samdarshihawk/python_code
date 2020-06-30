
"""
Minimum Index Sum of Two Lists
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer. 
"""



def findRestaurant(list1, list2):
    output={}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i]==list2[j]):
                output[list1[i]]=i+j
    l1=output.keys()
    l2=output.values()
    small = min(l2)
    return(l1[l2.index(small)])
    
    
