import pyperclip

def user_input():
    user_input = ""
    return user_input
    #disabling input function for now
    #user_input = input("Type Y to include alts. Otherwise press enter: ")
    #return user_input

def riot_id_converter():
    # Copies from clipboard
    input_text = pyperclip.paste()
    output_lines = []

    for line in input_text.split('\n'):
        modified_line = line.strip()

        
        
        colon_positions = [pos for pos, char in enumerate(modified_line) if char == ':']
        fourth_colon_position = colon_positions[3]
        modified_line = modified_line[fourth_colon_position + 1:].strip()
        output_lines.append(modified_line)
           
        
 

    # Join the output lines into a single string and copy to clipboard
    output_text = '\n'.join(output_lines)
    pyperclip.copy(output_text)
            
        
    #saves to clipboard
    output_text = '\n'.join(output_lines)
    pyperclip.copy(output_text)



riot_id_converter()
