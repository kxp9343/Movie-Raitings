
action = ["Avengers Endgame", "Wonder Woman", "Spiderman Far from Home", "Aquaman", "Shazam"]
comedy = ["Coco", "Zootopia", "Finding Dory", "Minions", "The Lego Movie"]
scifi = ["Arrival", "Children of Men", "The Martian", "Inception", "Interstellar"]
horror = ["The Nun", "The Conjuring", "It", "Insidious", "Annabelle Comes Home"]

while True:
	print("******************************************")
	print("Welcome to the Movie Recommendation System")
	print("******************************************")
	ask = input("Would you like to see our listings?    ")
	if ask == "Y":
		print("We have action, comedy, scifi, and horror listings")
		ask2 = input("Type 'action', 'comedy', 'scifi', or 'horror': ")
		if ask2 == "action":
			count = 0 
			while True:
				if count == len(action):
					break
				print(action[count] +" is our first recommentation")
				ask3 = input("Would you like to see it? Y/N")
				if ask3 == "Y":
					print("You have chosen " + action[count] + ".")
					break
				elif ask3 == "N":
					count = count + 1
		elif ask2 == "comedy":
			count = 0 
			while True:
				if count == len(comedy):
					break
				print(action[count] +" is our first recommentation")
				ask3 = input("Would you like to see it? Y/N")
				if ask3 == "Y":
					print("You have chosen " + comedy[count] + ".")
					break
				elif ask3 == "N":
					count = count + 1
		elif ask2 == "scifi":
			count = 0 
			while True:
				if count == len(scifi):
					break
				print(action[count] +" is our first recommentation")
				ask3 = input("Would you like to see it? Y/N")
				if ask3 == "Y":
					print("You have chosen " + scifi[count] + ".")
					break
				elif ask3 == "N":
					count = count + 1	
		elif ask2 == "horror":
			count = 0 
			while True:
				if count == len(horror):
					break
				print(action[count] +" is our first recommentation")
				ask3 = input("Would you like to see it? Y/N")
				if ask3 == "Y":
					print("You have chosen " + horror[count] + ".")
					break
				elif ask3 == "N":
					count = count + 1





