import random 

print("""\                                                                                                                                                                                              
      * ***                                                                   *                         ***** *     **                                     *                               
    *  ****  *                                                        *     **                       ******  **    **** *                                **                                
   *  *  ****                                                        **     **                      **   *  * **    ****                                 **                                
  *  **   **                                                         **     **                     *    *  *  **    * *                                  **                                
 *  ***          **   ****                  ****       ****        ******** **                         *  *    **   *     **   ****                      **                   ***  ****    
**   **           **    ***  *    ***      * **** *   * **** *    ********  **  ***      ***          ** **    **   *      **    ***  * *** **** ****    ** ****       ***     **** **** * 
**   **   ***     **     ****    * ***    **  ****   **  ****        **     ** * ***    * ***         ** **     **  *      **     ****   *** **** ***  * *** ***  *   * ***     **   ****  
**   **  ****  *  **      **    *   ***  ****       ****             **     ***   ***  *   ***        ** **     **  *      **      **     **  **** ****  **   ****   *   ***    **         
**   ** *  ****   **      **   **    ***   ***        ***            **     **     ** **    ***       ** **      ** *      **      **     **   **   **   **    **   **    ***   **         
**   ***    **    **      **   ********      ***        ***          **     **     ** ********        ** **      ** *      **      **     **   **   **   **    **   ********    **         
 **  **     *     **      **   *******         ***        ***        **     **     ** *******         *  **       ***      **      **     **   **   **   **    **   *******     **         
  ** *      *     **      **   **         ****  **   ****  **        **     **     ** **                 *        ***      **      **     **   **   **   **    **   **          **         
   ***     *       ******* **  ****    * * **** *   * **** *         **     **     ** ****    *      ****          **       ******* **    **   **   **   **    **   ****    *   ***        
    *******         *****   **  *******     ****       ****           **    **     **  *******      *  *****                 *****   **   ***  ***  ***   *****      *******     ***       
      ***                        *****                                       **    **   *****      *     **                                ***  ***  ***   ***        *****                
                                                                                   *               *                                                                                       
                                                                                  *                 **                                                                                     
                                                                                 *                                                                                                         
                                                                                *                                                                                                          
                                                                                                                                                                                            """)

gen_number = int(random.randint(1,100))

print("Welcome to the NUmber Guessing Game!")
print("Im thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or'hard':")

def diff():
  no_guesses = 0
  if difficulty == "easy":
    no_guesses = 10
    return no_guesses
  elif difficulty == "hard":
    no_guesses = 5
    return no_guesses
  
#no_guesses = int(no_guesses)
#print(f"You have {no_guesses} attempts remaining to guess the number.")

#guess_number = int(input("Make a guess:"))

def check_answer(guess_number, gen_number , no_guesses):
    #guess_number = int(input("Make a guess:"))
    #while gen_number != guess_number:
    if guess_number < gen_number:
      print("Too low.\n")
      #print(f"You have {no_guesses-1} attempts remaining to guess the number.")
      return no_guesses - 1
    elif guess_number > gen_number:
      print("Too High.\n")
      #print(f"You have {no_guesses-1} attempts remaining to guess the number.")
      return no_guesses - 1
    else:
      print(f"You got it! The answer was {guess_number}")
 

def lol():
  no_guesses = diff()
  guess_number = 0
  while guess_number != gen_number:
    print(f"You have {no_guesses} attempts remaining to guess the number.")     
    guess_number = int(input("Make a guess:"))
    no_guesses = check_answer(guess_number, gen_number, no_guesses)

    if no_guesses == 0:
      print("you loose")
      return
    elif guess_number != gen_number:
      print("Guess again.")

lol()