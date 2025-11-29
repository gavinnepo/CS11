print("""    ****************************************
        |                               |
        |       Welcome to madlibs!     |
        |                               |
    ****************************************""")

play=input("DO you want to play madlibs?").strip().lower()  
if play == "yes":
    person_name=input("Choose a name for your person: ")
    place=input("Choose a place: ")
    noun_1=input("Choose a singular item: ")
    animal_1=input("Choose an animal: ")
    adjective_1=input("Choose an adjective for a feeling: ")
    adjective_2=input("Choose an adjective: ")
    adjective_3=input("Choose an adjective: ")
    animal_2=input("Choose an animal: ")
    food=input("Choose an input: ")
    print(f"""
    Over break I am going camping with {person_name}. It is important to be prepared when camping at {place}, so I made sure to pack a sleeping bag, a flashlight, and a {noun_1}. 
    The possibility of seeing a {animal_1} makes me feel {adjective_1}
    I am excited to go hiking on the {adjective_2} trail. 
    If i see a {adjective_3} {animal_2} on the hike, I will take it home as my new pet!
    The best part of camping is eating {food} by my campfire!
     """)


