import random
cb_counter=0    #code breaker input cb_counter
cb_input=0   #code breaker input
cb_list=[]   #code breaker input list


cm_list=["apple","kiwi","grape","banana","cherry"]      #Five choices of items to include in 4 slots of code maker

trial_counter=0 #amount of trials taken by user

print()
print('            Welcome to Mastermind:CSC1024 edition     ')
print('Below is the possible list of 5 fruits you will have to guess in 4 slots:')
print()
print(f"         {cm_list}                           ")
print()
print('Repetition of fruits is possible!          ')
print()


code_maker= random.choices(cm_list, k=4)    #generate 4 random items from cm_list with repetition being possible.



def verify_correctplace():              #function to count amount of correct items in correct place
    counter_verify_correctplace=0
    for x in enumerate(code_maker):
        for y in enumerate(cb_list):
          if x==y:                      #for each (index,element) in code maker and cb_list, if the index and element are equal, counter increment.
            counter_verify_correctplace=counter_verify_correctplace+1
    return counter_verify_correctplace 

         
def taken_matched_items():                  #function to remove items in cb_list that has index & element match in code maker.
    list1=cb_list.copy()
    list2=code_maker.copy()

    list_zip = zip(list1, list2)
    zipped_list = list(list_zip)            #zip cb_list and code maker
    
    for i, j in (zipped_list):      
        if i==j:                           #for each paired items in the zipped list (i,j), if the paired items are equal, remove the item.
            list2.remove(j)
            list1.remove(i)
    i,j=zip(*zipped_list)
    return (list2,list1)                   #the result gives us the mismatched items between the two lists
      


def verify_wrongplace():                #function to count amount of incorrect position but that element exist code maker.
    cm,cb=taken_matched_items()         #take values from taken_matched_items()
    counter_verify_wrongplace=0
    for i in cb:
        if i in cm:                     #check if values of mismatched items, where if one mismatch items exist in code maker list, then counter increment.
            counter_verify_wrongplace=counter_verify_wrongplace+1
    return(counter_verify_wrongplace)
              

                
print('------- START! Input 4 guesses of fruits -------')      #Notify user to give four inputs of guesses 

while cb_counter<4:
    cb_input=str(input ("Enter your guess:" ))      #guess input
    cb_lower=cb_input.lower()  #convert code breaker input to lower case only
    
    
    if cb_lower in cm_list:      #verify if input is apart of code maker list of fruits. if not, tell user input is invalid.
            cb_list.append(cb_lower)
            cb_counter=cb_counter+1
          
       
    if cb_lower not in cm_list:   
        print(cb_lower, "is not apart of the listed fruits.") 
            
trial_counter=trial_counter+1

print()
print('Below is the possible list of 5 fruits you will have to guess in 4 slots:')
print()
print(cm_list)
print()
print('YOUR GUESS:')
print()
print(cb_list)

print()
print("RESULT:")        #print result
correct_place= verify_correctplace() 
print("Correct fruits in the CORRECT POSITION:",correct_place)
wrong_place= verify_wrongplace()
print("Correct fruits in the WRONG POSITION:",wrong_place)
guess=4-(correct_place+wrong_place)
print("BONUS HINT! Fruit guessed that is NOT in the code maker:", guess)  #Acts as a clue to help user guess better
print("Amount of trials:", trial_counter)       #print how many counts of trials they get




while correct_place<4:          #after their first trial, they will continue to retry under this loop. until correct_place==4.
    cb_list=[]              
    cb_counter=0                #reset list and cb_counter
    print()
    print('RETRY:')
    print('Have another try in entering your 4 guesses:')
    print()
    
    while cb_counter<4:
        cb_input=str(input("re-enter your guesses:"))
        cb_lower=cb_input.lower()  #convert code breaker input to lower case only
    
        if cb_lower in cm_list:      #verify if input is apart of code maker.
                cb_list.append(cb_lower)
                cb_counter=cb_counter+1
        
        if cb_lower not in cm_list:   
            print(cb_lower, "is not apart of the listed fruits.") 
    trial_counter=trial_counter+1        
  
    print()
    print('Below is the possible list of 5 fruits you will have to guess in 4 slots:')
    print()
    print(cm_list)
    print()
    print('YOUR GUESS:')
    print()
    print(cb_list)

    print()
    print("RESULT:")            #print result
    correct_place= verify_correctplace() 
    print("Correct fruits in the CORRECT POSITION:",correct_place)
    wrong_place= verify_wrongplace()
    print("Correct fruits in the WRONG POSITION:",wrong_place)
    guess=4-(correct_place+wrong_place)
    print("BONUS HINT! Fruit guessed that is NOT in the code maker:", guess)  #Acts as a clue to help user guess better
    print("Amount of trials:", trial_counter)       #print how many counts of trials they get
        
if correct_place==4:
        print()
        print('--- Congratulations! You made it ---')
        print()
        print('your code breaker list:', cb_list)
        print('your code maker list:', code_maker)
        print("Amount of trials:", trial_counter)
