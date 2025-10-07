def word_count(b):
    count = 0
    i = 0

    word_list = b.split()
    total_words = len(word_list)
    while i < total_words:
        count+=1
        i+=1
    return count

def char_count(b):
    i = 0
    j = 0

    alphabet = {}
    alpha_char_dict = {}
    alpha_num_dict = {}

    alpha_merge = {}
    new_alpha = []

    char_lower = b.lower()
    total_words = len(char_lower)

    while i < total_words:
        if char_lower[i] in alphabet:
            alphabet[char_lower[i]]+=1
            
        else:
            alphabet[char_lower[i]] = 1

            
        i+=1  
    

    return alphabet

def sort_alpha(b):
    j = 0


    alpha_char_dict = {}
    alpha_num_dict = {}
    alpha_merge = {}
    new_alpha = []


    alpha_char = list(b.keys())
    alpha_num = list(b.values())

    total_alpha = len(alpha_char)
    
    while j < total_alpha:

        alpha_char_dict["char"]= alpha_char[j]
        
        alpha_num_dict["num"] = alpha_num[j]

        for key in alpha_char_dict:
            alpha_merge[key] = alpha_char_dict[key]
            #print(alpha_merge,"1")
        for key in alpha_num_dict:
            alpha_merge[key] = alpha_num_dict[key]
            #print(alpha_merge,"2")
        
        new_alpha.append(alpha_merge.copy())
        #new_alpha.append(alpha_merge)
        
        j+=1

    

    new_alpha.sort(reverse=True, key=sort_on)

    final_alpha = filter_alpha(new_alpha)

    return final_alpha


def sort_on(alpha):
    return alpha["num"]


def filter_alpha(alpha):
    k=0

    alpha_len = len(alpha)

    temp_dict = {}
    f_alpha = []

    while k < alpha_len:
        dict1 = alpha[k]["char"]
        dict2 = alpha[k]["num"]


        if dict1.isalpha():
            #f_alpha.append(alpha[k].copy())
            temp_dict[dict1] = dict2
            k+=1
        else:
            k+=1
        

    return temp_dict

