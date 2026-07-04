def no_of_dices(n,k,target):#if the target is 0 and the number of dices is also 0 then we are returning 1 because we have found a valid combination
    if target == 0 and n == 0:
        return 1
    #if the target is less than 0 or the number of dices is less than 0 then we are returning 0 because we have not found a valid combination
    if target < 0 or n < 0:
        return 0
    count = 0 #we are initializing the count variable to store the number of combinations
    for i in range(1,k+1):#we are iterating through each face of the dice and we are including that face in the current combination and we are finding the combinations of the remaining faces and the remaining target
        count += no_of_dices(n-1,k,target-i) #we are including the current face in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
    return count #we are returning the total number of combinations found by including each face of the dice in the current combination
n = 2 #number of dices
k = 6 #number of faces on each dice
target = 7 #target sum
print(no_of_dices(n,k,target)) #we are calling the no_of_dices function for the given number of dices, number of faces, and target sum
'''tc: O(k^n) because we are iterating through each face of the dice and we are including that face in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i for each face of the dice
   sc: O(n) because of the recursive call stack and the current combination string which can be at most n characters long'''
'''trace the example in the code
   n = 2, k = 6, target = 7
   no_of_dices(2,6,7)
   #first dice
   # face 1
   # we are including the face 1 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #    no_of_dices(1,6,6)
   #   # face 2
   # we are including the face 2 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #       no_of_dices(0,6,4) => 0 because the
   # target is less than 0 or the number of dices is less than 0
   #  # face 3
   # we are including the face 3 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #      no_of_dices(0,6,3) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 4
   # we are including the face 4 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #     no_of_dices(0,6,2) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 5
   # we are including the face 5 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #    no_of_dices(0,6,1) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 6
   # we are including the face 6 in the current combination and we are finding the combinations
   # of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #   no_of_dices(0,6,0) => 1 because the target is 0 and the number of dices is also 0
   # face 2
   # we are including the face 2 in the current combination and we are finding the combinations
   # of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #    no_of_dices(1,6,5)
   #  # face 1
   # we are including the face 1 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #      no_of_dices(0,6,4) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 2
   # we are including the face 2 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #     no_of_dices(0,6,3) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 3
   # we are including the face 3 in the current combination and we are finding the combinations
   # of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #    no_of_dices(0,6,2) => 0 because the target is less than 0 or the number of dices is less than 0 
   # face 4
   # we are including the face 4 in the current combination and we are finding the combinations of the remaining faces and the remaining target by calling the no_of_dices function recursively with n-1, k, and target-i
   #   no_of_dices(0,6,1) => 0 because the target is less than 0 or the number of dices is less than 0
   # face 5
   # we are including the face 5 in the current combination and we are finding the combinations'''