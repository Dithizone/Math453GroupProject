# This script will change survey response values to
# be consistent. A markdown file will be created so
# groupmates using R Studio can read what changes were
# made and why.

import pandas as pd
import matplotlib.pyplot as plt

somerville2017 = pd.read_csv('data/Happiness_Survey_2017.csv')
demographics = somerville2017[['1. What is your gender', '2. Age?',
                               '3. What language(s) do you speak at home?',
                               '4. What is your race or ethnicity?',
                               '5. Do you have children age 18 or younger who live with you?',
                               '6. Describe your housing status in Somerville.',
                               '8 How long have you lived here?',
                               '9. What is your annual household income?', '10. Are you a student?']]

# These are all the redundant gender responses
both_selected = ['(both selected)',
                 'both male and female selected', 'both selected',
                 '(Female and Male selected)', 'Female + Male checked',
                 'Checked Female & Male', '(Checked both Male and Female)',
                 'both male and female checked',
                 'both make and female checked', 'Both female and male checked',
                 'Male and Female',
                 'Both checked', 'Both Checked', ]

multiple_people = ['Two people answered',
                   'couple', 'Two People filled this out',
                   'a cou', '2 of us']

genderqueer = ['Transwoman', 'non binary female', 'Genderqueer',
               "I don't believe in the social construct of gender"]

for i in both_selected:
    demographics["1. What is your gender"] = demographics["1. What is your gender"].replace(i, "Both selected")
print("\n----- Both selected -----")
print(demographics["1. What is your gender"].value_counts())

for j in multiple_people:
    demographics["1. What is your gender"] = demographics["1. What is your gender"].replace(j, "Multiple people")
print("\n----- Multiple people -----")
print(demographics["1. What is your gender"].value_counts())

for k in genderqueer:
    demographics["1. What is your gender"] = demographics["1. What is your gender"].replace(k, "Non-binary")
print("\n----- Non-binary -----")
print(demographics["1. What is your gender"].value_counts())
print("\n-----Value counts for all demographics-----")

# Age responses are fine

# These are the household languages declared. TODO: condense redundant responses
languages = ['English',
             'Spanish',
             'English;Russian',
             'nan',
             'English;Spanish',
             'German',
             'English;Portugese',
             'English;Italian',
             'English;Croatian',
             'English;Japanese',
             'Portugese',
             'English;Arabic',
             'English;Chinese',
             'English;Spanish;Haitian Creole',
             'Korean',
             'English;Farsi',
             '3 languages',
             'English;French',
             'cape verdean creole',
             'English;Spanish;Portugese',
             'English;Sometimes Deutsch',
             'Hindi',
             'English;Nepali',
             'Indian',
             'French',
             'English;Vietnamese and Chinese',
             'English;Danish',
             'Finnish',
             'English;German + ....',
             'English;Italian, Swedish',
             'Bengali',
             'English;Haitian Creole',
             'English;French Creole',
             'English;Jamaican Patois',
             'Chinese',
             'Italian',
             'English;Spanish;Mandarin',
             'English;Bengali',
             'English;Bosnian',
             'English;Portugese;German',
             'English;Portugese;French',
             'English;Tamil',
             'Haitian Creole',
             'English;Haitian Creole;French',
             'English;Spanish;Chinese',
             'English;Hindi',
             'Cantonese',
             'Swahili',
             'English;Tibetan',
             'English;ENGLISH ONLY']

# These are the declared races/ethnicities. TODO: condense race/ethnicity
race_or_ethnicity = ['White', 'Hispanic/Latino;Puertoriquena', 'Italian/Turkish Scottich/Irish', 'nan',
                     'Hispanic/Latino', 'Hispanic/Latino;White;Middle Eastern', 'Irish', 'Asian',
                     'Black/African American',
                     'Asian;White', 'Human', 'White;American - White', 'Arab', 'White;American',
                     'Black/African American;White', 'White;Semitic', 'Cape Verdean', 'Hispanic/Latino;White',
                     'Hispanic/Latino;Portuguese/American', 'Multi-cultural', 'Italy', 'White;Jewish',
                     'Black/African American;Human Race', 'Multi-Racial', 'White;Hawai\'ian',
                     'Black/African American;Hatian', 'Semitic', 'Arabic, French', 'Indian American', 'White;Italian',
                     'Asian;Hispanic/Latino;White', 'central american', 'Mixed', 'Jewish', 'Hispanic/Latino;Brazil',
                     'Italian/American']

# Children age 18 or younger is fine.

# Rent or own responses to consider. TODO: look at rent/own responses
neither_rent_nor_own = ['desability apt do governo',
                        'Sre Housing ',
                        'selected both',
                        'Senior']

# How long have you lived here? responses fine

# income responses fine.

# Are you student? responses fine.

