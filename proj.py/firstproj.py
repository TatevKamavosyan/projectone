import random

template=random.randint(1,3)


def template_one(number, measure_of_time,mode_of_transportation,adjective,
adjective2,noun,color,part_of_body,verb,number2,noun2,noun3,part_of_body2,
verb1,noun4,adjective3,silly_word,noun5):

    print(f'It was about {number} {measure_of_time} ago when I arrived at the hospital, in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.There are nurses here who have {color} {part_of_body}.If someone wants to come into my room I told them that they have to {verb1} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_body2}. I heard that all doctors {verb} {noun4} every day for breakfast.The most {adjective3} thing about being in the hospital is the {silly_word} {noun5} !')


def template_two(person_name,noun,adjective_feeling,verb,adjective_feeling2,
animal,verb2,color,verb_ending_in_ing,adverb_ending_in_ly,number,measure_of_time,
color2,animal2,number2,silly_word,noun2):

    print(f'This weekend I am going camping with {person_name}.I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent. I am {adjective_feeling2} we might see a(n) {animal},I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and{verb2}. I have heard that the {color} lake is great for {verb_ending_in_ing}Then we will {adverb_ending_in_ly} hike through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet!At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!')


def template_three(person_name,adjective,color,animal,place,
adjective2,magical_creature_plural,adjective3,magical_creature_plural2,
room_in_a_house,noun,noun2,noun_plural3,adjective4,noun_plural4,number,
measure_of_time,verb_ending_in_ing,adjective5,noun5):

    print(f'Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a{color} {animal} in {place}. There are {adjective2} {magical_creature_plural} and {adjective3} {magical_creature_plural2} here!In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}.It feels as though I have lived here for {number} {measure_of_time}.I hope one day you can visit, although the only way to get here now is {verb_ending_in_ing} on a{adjective5} {noun5}!')


if template==1:
    template_one( number=int(input("Enter a number: ")),
        measure_of_time=input("Enter measure of time: "),
        mode_of_transportation=input("Enter mode of transportation: "),
        adjective=input("Enter adjective: "),
        adjective2=input("Enter adjective 2: "),
        noun=input("Enter noun: "),
        color=input("Enter color: "),
        part_of_body=input("Enter part of the body: "),
        verb=input("Enter verb: "),
        number2=int(input("Enter number 2: ")),
        noun2=input("Enter noun 2: "),
        noun3=input("Enter noun 3: "),
        part_of_body2=input("Enter part of the body2: "),
        verb1=input('Enter a verb: '),
        noun4=input("Enter noun4: "),
        adjective3=input("Enter adjective3: "),
        silly_word=input("Enter silly word: "),
        noun5=input("Enter noun: "))
elif template==2:
    template_two(person_name=input("Input name: "),
    noun=input("Input noun: "),
    adjective_feeling=input("input adjective(feeling): "),
    verb=input("input verb: "),
    adjective_feeling2=input("input adjective2(feeling): "),
    animal=input("input animal: "),
    verb2=input("input verb2: "),
    color=input("input color: "),
    verb_ending_in_ing=input("Enter verb, ending in ing: "),
    adverb_ending_in_ly=input("Enter  adverb ending in ly: "),
    number=int(input("input number: ")),
    measure_of_time=input("input measure_of_time: "),
    color2=input("Enter a color: "),
    animal2=input('Enter an animal: '),
    number2=int(input("Enter a number: ")),
    silly_word=input("input silly word: "),
    noun2=input("input noun 2: "))
else:
    template_three(
    person_name=input("Enter a name: "),
    adjective=input("adjective(feeling): "),
    color=input("color: "),
    animal=input("animal: "),
    place=input("place: "),
    adjective2=input("adjective2: "),
    magical_creature_plural=input("Magical Creature (Plural): "),
    adjective3=input("adjective3: "),
    magical_creature_plural2=input("Magical Creature (Plural): "),
    room_in_a_house=input("Room in a House: "),
    noun=input("noun: "),
    noun2=input("noun 2: ") , 
    noun_plural3=input("noun 3(plural): "),
    adjective4=input("adjective: "),
    noun_plural4=input("noun 4(plural): "),
    number=int(input("number: ")),
    measure_of_time=input("measure_of_time: "),
    verb_ending_in_ing=input("verb: "),
    adjective5=input("adjective5: "),
    noun5=input("noun 5: "))
    
    






    

  





        
