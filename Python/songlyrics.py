# import time  # python time module for import time

# def printlyrics():   # tuples(line, delay)
#     lines = [
#         ("I wanna da", 0.05),
#         ("I wanna dance in the lights", 0.05),
#         ("I wanna Ro" , 0.05),
#         ("I wanna Rock yo Body" , 0.05),
#         ("I wanna go", 0.05),
#         ("I wanna go for a ride", 0.05),
#         ("Pop in the music and", 0.05),
#         ("Rock your body", 0.05),
#         ("Rock your body", 0.05),
#         ("((Rock your body))", 0.05),
#         ("((Rock that body))", 0.05),
#         ("Come on, come on, come on", 0.05),
#         ("Rock that body", 0.05),
#     ]  
   
#     delays_after_line = [0.5] * len(lines) # 0.05 sec delay for each lines


#     # loop for everyline and charecter delay on line list 
#     for i, (line, char_delay) in enumerate(lines): #enumerate = print with index 
#         for char in line:
#             print(char, end='', flush=True)  # print the charecter in one line
#             time.sleep(char_delay)           # time delay between every character
#         print()                               # time delay between every character
#         time.sleep(delays_after_line[i])      # delay after the whole line

# printlyrics() # function call


import time # python time module for import time

def print_lyrics():   # tuples(line, delay)
   
    lines = [
    ("Touch my body tender", 0.15),
    ("'Cause the feeling makes me weak", 0.15),
    ("Kicking off the covers", 0.15),
    ("I see the ceiling while you're looking down at me", 0.1),
    ("How can we go back to being friends", 0.15), 
    ("When we just shared a bed?", 0.15),
    ("How can you look at me and pretend", 0.15),
    ("I'm someone you've never met?", 0.15),
]



    # Delay after each full line
    delays_after_line = [0.7] * len(lines)  # 0.7 sec delay for each lines


     # loop for everyline and charecter delay on line list 
    for i, (line, char_delay) in enumerate(lines):  #enumerate = print with index 
        for char in line:
            print(char, end='', flush=True) # print the charecter in one line
            time.sleep(char_delay)# time delay between every character
        print() # after finishing the current line go to the new line
        time.sleep(delays_after_line[i]) # delay after the whole line

print_lyrics() # function call

