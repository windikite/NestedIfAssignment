#Task 1 ----------------------------------------------------------------------
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

#Task 2 ----------------------------------------------------------------------
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# upgraded_audio = "microphone and forward speakers" if attendees > 50 else "none"
# enhanced_audio = "microphone, forward and rear speakers" if attendees > 100 else "none"
# supreme_audio = "microphone, forward, central and rear speakers" if attendees > 150 else "none"
# upgraded_visuals = "projector and middle projector screen" 
# enhanced_visuals = "linked dual projectors and left and right projector screens" if attendees > 75 else "none"
# supreme_visuals = "3 linked projectors and left, right and central projector screens" if attendees > 150 else "none"

# audio = "none"
# visuals = "none"

# if supreme_audio != "none":
#     print("Are you interested in purchasing our Supreme Audio package? It comes with:")
#     print(supreme_audio)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         audio = supreme_audio
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# elif enhanced_audio != "none":
#     print("Are you interested in purchasing our Enhanced Audio package? It comes with:")
#     print(enhanced_audio)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         audio = enhanced_audio
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# elif upgraded_audio != "none":
#     print("Are you interested in purchasing our Upgraded Audio package? It comes with:")
#     print(upgraded_audio)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         audio = upgraded_audio
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# else:
#     pass

# if supreme_visuals != "none":
#     print("Are you interested in purchasing our Supreme Visuals package? It comes with:")
#     print(supreme_visuals)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         visuals = supreme_visuals
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# elif enhanced_visuals != "none":
#     print("Are you interested in purchasing our Enhanced Visuals package? It comes with:")
#     print(enhanced_visuals)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         visuals = enhanced_visuals
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# elif upgraded_visuals != "none":
#     print("Are you interested in purchasing our Upgraded Visuals package? It comes with:")
#     print(upgraded_visuals)
#     choice = input("Choice (yes or no): ")
#     if choice == "yes":
#         visuals = upgraded_visuals
#         print("Excellent! Added to cart.")
#     elif choice == "no":
#         print("Not a problem!")
# else:
#     pass

# if venue != "none": print("Venue: ", venue)
# if audio != "none": print("Audio Equipment: ", audio)
# if visuals != "none": print("Visual Equipment: ", visuals)

#Task 3 ------------------------------------------------------------------------
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
upgraded_audio = "microphone and forward speakers" if attendees > 50 else "none"
enhanced_audio = "microphone, forward and rear speakers" if attendees > 100 else "none"
supreme_audio = "microphone, forward, central and rear speakers" if attendees > 150 else "none"
upgraded_visuals = "projector and middle projector screen" 
enhanced_visuals = "linked dual projectors and left and right projector screens" if attendees > 75 else "none"
supreme_visuals = "3 linked projectors and left, right and central projector screens" if attendees > 150 else "none"
vegetarian = '"Veggie Delight Caterers"'
non_vegetarian = '"Gourmet Meals Caterers"'

audio = "none"
visuals = "none"
catering = "none"

if supreme_audio != "none":
    print("Are you interested in purchasing our Supreme Audio package? It comes with:")
    print(supreme_audio)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        audio = supreme_audio
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
elif enhanced_audio != "none":
    print("Are you interested in purchasing our Enhanced Audio package? It comes with:")
    print(enhanced_audio)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        audio = enhanced_audio
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
elif upgraded_audio != "none":
    print("Are you interested in purchasing our Upgraded Audio package? It comes with:")
    print(upgraded_audio)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        audio = upgraded_audio
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
else:
    pass

if supreme_visuals != "none":
    print("Are you interested in purchasing our Supreme Visuals package? It comes with:")
    print(supreme_visuals)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        visuals = supreme_visuals
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
elif enhanced_visuals != "none":
    print("Are you interested in purchasing our Enhanced Visuals package? It comes with:")
    print(enhanced_visuals)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        visuals = enhanced_visuals
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
elif upgraded_visuals != "none":
    print("Are you interested in purchasing our Upgraded Visuals package? It comes with:")
    print(upgraded_visuals)
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        visuals = upgraded_visuals
        print("Excellent! Added to cart.")
    elif choice == "no":
        print("Not a problem!")
else:
    pass

print("Do you want to setup vegetarian catering?")
choice = input("Choice (yes or no): ")
if choice == "yes":
    print("Our partner", vegetarian, "is top rated in vegetarian catering and options, would you like to order catering through them?")
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        catering = vegetarian
    if choice == "no":
        print("Our partner", non_vegetarian, "is a top rated caterer with classic and fun options, would you like to order catering through them?")
        choice = input("Choice (yes or no): ")
        if choice == "yes":
            catering = non_vegetarian
        if choice == "no":
            "Not a problem!"
if choice == "no":
    print("Our partner", non_vegetarian, "is a top rated caterer with classic and fun options, would you like to order catering through them?")
    choice = input("Choice (yes or no): ")
    if choice == "yes":
        catering = non_vegetarian
    if choice == "no":
        "Not a problem!"



if venue != "none": print("Venue: ", venue)
if audio != "none": print("Audio Equipment: ", audio)
if visuals != "none": print("Visual Equipment: ", visuals)
if catering != "none": print("Catering: ", catering)