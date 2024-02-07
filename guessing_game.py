class GuessingGame():
    def __init__(self, user_guess, answer=12) -> None:
        self._user_guess = user_guess 
        self._answer = answer
    
    def guess(self, user_guess):
        if user_guess != answer:
            if user_guess > answer:
                print("lower!")
            elif user_guess < answer:
                print("higher!")
            else:
            
    #a method of determining if the user was able 
        
