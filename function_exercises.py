def get_letter_grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'

def is_two(num):
    #Return True if int 2 or str '2'
    if num == 2 or num == '2':
        return True
    #Return if not
    else:
        return False
    
def is_vowel(let):
    #Check to see if let is a vowel, if so return True
    if let in ['a','e','i','o','u']:
        return True
    #If not a vowel, return False
    else:
        return False
    
def is_consonant(let):
    #If let not a vowel, return True
    if let not in ['a','e','i','o','u']:
        return True
    else:
        return False

def cap_word_if_cons(word):
    #Use is_consonant function to determine first letter
    if is_consonant(word[0]) :
        return word.capitalize()
    else:
        return word

def calculate_tip(tip_per,bill_total):
    return bill_total*tip_per

def apply_discount(org_price,discount_per):
    
    #discount to be subtracted from original price
    discount = org_price*discount_per
    return org_price-discount

def handle_commas(str_num):
    return int(str_num.replace(',',''))

def remove_vowels(string):
    for s in string:
        #Determine if letter is a vowel, if so remove it
        if is_vowel(s):
            string = string.replace(s,'')
        
    return string


def normalize_name(string):
    import re
    #Removing all these characters 
    string, n = re.subn('[!@#$%^&*\(\)+=-]', '', string)
    return string.strip().lower().replace(' ','_')

def cumulative_sum(numbers):
    #sum is total sum of list for each iteration
    sum=0
    #new_list stores each new sum and is later returned
    new_list = []
    for n in numbers:
        sum+=n
        new_list.append(sum)
    return new_list

