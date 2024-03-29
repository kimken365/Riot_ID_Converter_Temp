import pyperclip

def user_input():
    user_input = input("Type N to exclude alts. Otherwise press enter: ")
    return user_input

def riot_id_converter(riot_id_table, include_alts):
    #copies from clipboard
    input_text = pyperclip.paste()
    output_lines = []

    for line in input_text.split('\n'):
        modified_line = line.strip()

        #users with ALTS
        for riot_id, suffix_list in riot_id_table.items():
            
            if riot_id in line:
                #includes only the main account of the users
                if include_alts == 'N':
                    modified_line = suffix_list[0]
                
                #include all the accounts of the users
                else:
                    modified_line = '\n'.join(suffix_list)
                
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
riot_id_table = {
    'Suyeonchan': ['Suyeonchan#00000',
                   ],    
}

include_alts = user_input()

riot_id_converter(riot_id_table, include_alts)
