# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
petSpecies = "dog"
age = 1

if petSpecies == "dog":
    if age <2:
        print("puppy food")
elif petSpecies == "cat":
    if age >5:
        print("senior cat food")



