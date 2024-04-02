import pyperclip

def user_input():
    user_input = input(" ")
    return user_input
    #disabling input function for now
    #user_input = input("Type Y to include alts. Otherwise press enter: ")
    #return user_input

def riot_id_converter(riot_id_table, include_alts):
    #copies from clipboard
    input_text = pyperclip.paste()
    output_lines = []

    for line in input_text.split('\n'):
        modified_line = line.strip()

        #users with ALTS
        for riot_id, suffix_list in riot_accounts_table.items():
            
            if riot_id in line:
                # include all the accounts of the users
                if include_alts != 'Y':
                    modified_line = '\n'.join(suffix_list)
                # includes only the main account of the users
                else:
                    modified_line = suffix_list[0]
    
                output_lines.append(modified_line)
                break

                    
        #users without ALTS  
        else:
            
            modified_line = modified_line[3:] 
            if modified_line and modified_line[0].isspace():
                modified_line = modified_line[2:]
            output_lines.append(modified_line)
            
        
    #saves to clipboard
    output_text = '\n'.join(output_lines)
    pyperclip.copy(output_text)

#add new usernames here
riot_accounts_table = {
    'Suyeonchan': ['Suyeonchan#00000',
                   ],    
}

include_alts = user_input()

riot_id_converter(riot_accounts_table, include_alts)
