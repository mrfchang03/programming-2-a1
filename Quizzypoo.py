score = 0

question_One = input( "What is the root of 36? ").lower()
if question_One == "6" or question_One == "six":
        print("Nice job!")
        score += 1
else:
    print("Try using a calculator")

question_Two = input( "How many planets are there in the solar system?").lower()
if question_Two== "8" or question_Two == "eight":
        print("You an astronaut?")
        score += 1
else:
    print("Stay away from space maybe?")

question_Three = input( "Who is the main character in Re:Zero?").lower()
if question_Three == "Subaru" or question_Three == "Natsuki Subaru":
        print("Correct")
        score += 1
else:
    print("Really? Watch it right now then!")

question_Four = input( "Which does more damage in minecraft? The Axe or the Sword?").lower()
if question_Four == "sword":
        print("Dream? U code?")
        score += 1
else:
    print("Smh, I don't think you're playing enough!")

question_Five = input( "What is the difference between a vector and scalar quantity?").lower()
if question_Five == "direction and magnitude" or question_Five == "magnitude and direction":
        print("WOAHH, EINSTEINS ALIVE!")
        score += 1
else:
    print("Aiya, pay attention in Clements!)

print(f"Your final score is {score / 5 * 100} %")