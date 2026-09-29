import array as arr
import random
 
# ---------------------------------------------------
# how life is going(game)
# ask 15 ques and find about your life
# All questions are positive so yes will give 1 point
# Questions come in a random order every time.
# It shows your life just for fun.
 
 
# function will ask one yes/no question and then return yes or no 
def ask_yes_no(question):
    print(question)
    answer = input("Answer (Yes/No): ").strip().lower()
 
    if answer == "yes" or answer == "y":
        return "Yes"
    elif answer == "no" or answer == "n":
        return "No"
    else:
        print("Invalid input, taking No.")
        return "No"
 
 
# use list there will be 15 question 
questions = [
    "do you ever feel excited when your day begins?",
    " you do not like going out more than staying at home?",
    "Do you enjoy watching movies alone with some snacks in free time?",
    "Do you feel calm and in control when you get angry?",
    "Do you have someone special who supports you?",
    "do you feel happy and peaceful when you are alone?",
    "you do not feeling nervous whenver u are in stage or performing in front of someone who you dont know",
    "Can you study for a long time with good energy, even when you are tired?",
    "are you in relationship?",
    "you never feel jealous  whenever u see a couple?",
    "Do you like travelling?",
    "Do you feel confident about your future?",
    "are you extrovert?",
    "Do you sleep well at night?",
    "Are you focused on your goal?",
]
 
# dictionary is used for stroing answer
answers = {}
 
# array store yes as 1 and 0 as no 
signal_array = arr.array('i', [])
 
# for randomized the questions
random.shuffle(questions)
 
# LOOP - to ask each questions
number = 1
for q in questions:
    print()
    result = ask_yes_no(str(number) + ". " + q)
    answers[q] = result
    number = number + 1
 
    # yes will show +1 
    if result == "Yes":
        signal_array.append(1)
    else:
        signal_array.append(0)
 
 
# FUNCTION - analyze ALL answers together and return ONE final life result
def analyze_life(signal_array):
    total_questions = len(signal_array)
    good_signals = 0
 
    # LOOP - go through every signal and count the good ones
    for value in signal_array:
        if value == 1:
            good_signals = good_signals + 1
 
    percent = (good_signals / total_questions) * 100
 
    # if-else  used for findind result to predict each type of answere

    if percent >= 90:
        life = "perfect life u are living, most people dream but u are living"
        message = "just dont be overconfident and always remember if u are the smartest in the room ,you are in wrong room "
 
    elif percent >= 80:
        life  = "u are just amazing, just maintain this life with u and have fun "
        message = "just dont care if u are alone at top as its much better to be alone at top rather than bottom"
    elif percent >= 75:
        life = " u are in great direction just maintain it "
        message = " just work without seeing time and develop your skills  learn just believe that you can " 
 
    elif  percent >= 70:
        life = "your life is going great, just a little improvement and it will be perfect"
        message ="just plan everything , eliminate all your distractions and last do the hardest task first"
    elif percent >= 60:
        life = "your life is good, but you are not using your full power yet"
        message ="just dont addicted to most dangerous drug which is called fear dont be shy just say and do whatever in your mind"
 
    elif percent >= 50:
        life = "u are little bit exhausted, i will recommend u to have a life partner so that u can give him or her tension too (lol)"
        message = "Overall, i will recommend u to have a life partner so that u can give him or her tension too (lol), jk but yeah, have someone in your life who supports u in your problems"
    elif percent >= 40:
        life = "your life is like a roller coaster, some days up and some days down"
        message ="Overall, many things together seem to be affecting your life. Just live today, as someone says tomorrow is a mystery, yesterday is history but today is a gift, that's why it's called present"
    elif percent >= 30:
        life = "your life is not much bad but u can improve"
        message ="always choose hardest right over easier wrong"
 
    elif percent >= 20:
        life = "your life is not much bad but u can improve"
        message = "Overall, a few things seem to be affecting you. I recommend u to travel and be extrovert, just talk to strangers and make friends, hangout and make your life beautiful or just watch (Zindagi Na Milegi Dobara)"
    else :
        life =  "aah u are in a much bad case "
        message = "Overall, many things together seem to be affecting your life. Just live today, as someone says tomorrow is a mystery, yesterday is history but today is a gift, that's why it's called present"
 
    return life, message
 
 
final_life, final_message = analyze_life(signal_array)
 
print()
print("===================================")
print("YOUR FINAL LIFE RESULT")
print("===================================")
print("Life:", final_life)
print(final_message)
print("===================================")
