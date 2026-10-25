import requests
import random

def Pokemon(): 
    num  = random.randint(1, 1351)
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"
    response = requests.get(url)
       
    result = response.json()
    print(f"\nThis Pokemon's ID is:{result["id"]}")
    print(f"This Pokemon's Weight is:{result["weight"]}")
    print(f"This Pokemon's Height is:{result["height"]}")
    abilities = result["abilities"]
    print(f"And Lastly This Pokemon Have This Ability/Abilities: ")        
    for ability in abilities:
            print (ability["ability"]["name"])
    return result

def game():
    result = Pokemon()
    for x in range(1, 5):
        guess = input("\nWHO'S THAT POKEMON?!: ").lower()
        if guess == result["name"]:
            print("\nYou got the correct answerr!!!")
            break
        else:
            if x == 4:
                print("\nYou LOSE! :p")
                print(f"The answer is {result["name"]}")
                break
            else:
                print(f"\ntry again :p, {x} / 3 Chance")
        
def main():
     while True:
        answer = input("\nDo you wanna play? [1 yes/2 no]:")
        if answer == "1":
            game()    
        elif answer == "2":
            print("See You Laterr!! ^_^")
            break

main()