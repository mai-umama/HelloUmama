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

print_lyrics() #fuction call
