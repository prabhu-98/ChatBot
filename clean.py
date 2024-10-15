import cleantext

# Dictionary of gender-biased words and their replacements
gender_bias_replacements = {
    'chairman': 'chairperson',
    'businessman': 'businessperson',
    'fireman': 'firefighter',
    'policeman': 'police officer',
    'stewardess': 'flight attendant',
    'mankind': 'humankind',
    'manpower': 'workforce',
    'congressman': 'congressperson',
    'mailman': 'mail carrier',
    'salesman': 'salesperson',
    'spokesman': 'spokesperson',
    'fisherman': 'fisher',
    'craftsman': 'craftsperson',
    'freshman': 'first-year student',
    'middleman': 'intermediary',
    'repairman': 'repairer',
    'barman': 'bartender',
    'cameraman': 'camera operator',
    'foreman': 'supervisor',
    'layman': 'layperson',
    'newsman': 'reporter',
    'sportsmanship': 'fair play',
    'weatherman': 'meteorologist',
    'man-made': 'human-made',
    'housewife': 'homemaker',
    'workman': 'worker',
    'yardman': 'yard worker',
    'anchorman': 'anchor',
    'gentleman': 'polite person',
    'handyman': 'handy person',
    'showman': 'showperson',
    'milkman': 'milk deliverer',
    'firewoman': 'firefighter',
    'policewoman': 'police officer',
    'councilman': 'council member',
    'statesman': 'statesperson',
    'forewoman': 'supervisor',
    'newswoman': 'reporter',
    'postman': 'mail carrier',
    'assemblyman': 'assembly member',
    'congresswoman': 'congressperson',
    'deliveryman': 'delivery person',
    'mailwoman': 'mail carrier',
    'repairwoman': 'repairer',
    'saleswoman': 'salesperson',
    'spokeswoman': 'spokesperson',
    'fisherwoman': 'fisher',
    'craftswoman': 'craftsperson',
    'foreperson': 'supervisor',
    'news anchor': 'anchor',
    'police official': 'police officer',
    'workwoman': 'worker',
    'yardwoman': 'yard worker',
    'assemblywoman': 'assembly member',
    'firefighter': 'firefighter',
    'police officer': 'police officer',
    'chairwoman': 'chairperson',
    'businesswoman': 'businessperson',
    'repair person': 'repairer',
    'bartender': 'bartender',
    'camera operator': 'camera operator',
    'supervisor': 'supervisor',
    'reporter': 'reporter',
    'fair play': 'fair play',
    'human-made': 'human-made',
    'homemaker': 'homemaker',
    'worker': 'worker',
    'yard worker': 'yard worker',
    'anchor': 'anchor',
    'polite person': 'polite person',
    'handy person': 'handy person',
    'showperson': 'showperson',
    'milk deliverer': 'milk deliverer',
    'council member': 'council member',
    'statesperson': 'statesperson',
    'assembly member': 'assembly member',
    'delivery person': 'delivery person',
    'chairperson': 'chairperson',
    'businessperson': 'businessperson',
    'repairer': 'repairer',
    'camera operator': 'camera operator',
    'intermediary': 'intermediary',
    'craftsperson': 'craftsperson',
    'layperson': 'layperson',
    'meteorologist': 'meteorologist',
    'first-year student': 'first-year student',
    'workforce': 'workforce',
    'Mankind': 'Humankind'
}


def replace_gender_biased_words(text, replacements=gender_bias_replacements):
    for biased_word, replacement in replacements.items():
        text = text.replace(biased_word, replacement)
    return text

# Example text with gender-biased words
# text = """
# The chairman of the committee is a businessman. The fireman and the policeman helped the stewardess. 
# Mankind has always relied on manpower. The congressman gave a speech.
# """

# Clean the text using cleantext
# cleaned_text = cleantext.clean(text,
#                                replace_with_punct="",
#                                no_urls=True,
#                                no_emails=True,
#                                no_phone_numbers=True,
#                                no_numbers=True,
#                                no_digits=True,
#                                no_currency_symbols=True,
#                                replace_with_url="<URL>",
#                                replace_with_email="<EMAIL>",
#                                replace_with_phone_number="<PHONE>",
#                                replace_with_number="<NUMBER>",
#                                replace_with_digit="0",
#                                replace_with_currency_symbol="<CUR>",
#                                lang="en"
#                               )

# Replace gender-biased words
# final_text = replace_gender_biased_words(text, gender_bias_replacements)


