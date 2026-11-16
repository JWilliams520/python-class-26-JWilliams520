print("CS 31 Python Programming")
print("Jaylynn Williams")
print("**************")
print("Welcome to My Mad Libs Game.....we are in for a journey... yes we...")
play = input("would you like to play anyways ? Yes or No:")
if play == 'Yes' or play == 'yes':
    yourName = input('What is your name? :')
    print(f" Welcome {yourName}! Which story would you like to play? ")
else:
    print("Well okay then I didnt want you to play anyways ")
    quit()

mycounter = 0

again = "y"
while again.lower() == "y":
      print("Option 1: Road Trip")
      print("Option 2 : First Date ")
      storyChoice = input("What is your story choice Option 1 or Option 2:")
      print('Now, Generating your story')


      if storyChoice == 'Option 1' or storyChoice == 'Road Trip'or storyChoice == 'option 1':
          mycounter = mycounter + 1
          friendName = input("1. What is the name of a family member or close friend:")
          luggageChoice = input("2.) leave  or buy new:")
          direction = input("3.) Left or Right:")
          carChoice = input("4.) Jump or Stay :")
          verb = input("5.) float or Swim:")
          finChoice = input("6.) Dolphin or Shark:")
          print(f"\n {yourName}, Here is your Story:\n ")
          print(f"You and, {friendName}, are heading out on a road trip.A few minutes after leaving, you realize your luggage is still at home.You decide to, {luggageChoice}, your luggage and continue the trip.")
          print(f"while driving your gps go's out and you reach a fork in the road and decide to  turn {direction} .Unfortunately, the road ends at a cliff.You decide to, {carChoice}. ")
          print(f"You somehow end up in a ocean.To escape, you immediately start to , {verb} . While {verb}ing through the water, you see a fin rapidly moving towards you.")
          print(f", it’s a, {finChoice}!!,The {finChoice} introduces himself as Gerold. Gerold leads you to an underwater kingdom.The citizens ask if you want to become King of Atlantis. ")
          print(f"And then you wake up and realize it was all a dream.")
          print(f"You have created {mycounter} story")

          again = input("Do you want to play again? (y/n): ")

      elif storyChoice == 'Option 2'or storyChoice == 'First Date' or storyChoice == 'option 2':
           mycounter = mycounter + 1
           partnerName = input("Enter the name of your date: ")
           foodChoice = input(" Enter your favorite food: ")
           clothesChoice = input("Change  or hope for the best: ")
           extrafoodChoice = input("Chesse or butter: ")
           movie = input("Enter your favorite movie: ")
           print(f"\n {yourName}, Here is your Story:\n ")
           print(f"You are getting ready to go on your first date with {partnerName} .While texting they ask what are you in the mood for you say {foodChoice}.As your getting changed you realize that your colthes arent fitting the way you want. ")
           print(f"You decide to {clothesChoice}.You arrive at the {foodChoice} place and you guys begin eating your food when your stomache starts to feel weird.You wave down the waiter and ask what's in it they say {extrafoodChoice}.")
           print(f"You panic because you're lactose intolerant and soon you can't keep things under wraps so you try to rush to the bathroom when a waiter accidentally falls onto you causing you fall and so do your pants and at the same time you  also release gas very loudly.")
           print(f"Embarassed you excuse yourself and rush out of the {foodChoice} place and go home in shame. When you hear knocking on your door and its {partnerName} who boxed up the food without the {extrafoodChoice} and you guys sit on the couch and watch {movie}")

           print(f"You have created {mycounter} story")

           again = input("Do you want to play again? (y/n): ")
# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
