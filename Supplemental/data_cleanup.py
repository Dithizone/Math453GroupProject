# This script will change survey response values to
# be consistent. A markdown file will be created so
# groupmates using R Studio can read what changes were
# made and why.

import pandas as pd
import matplotlib.pyplot as plt

somerville2017 = pd.read_csv('data/Happiness_Survey_2017.csv')

demographics = ['1. What is your gender', '2. Age?',
                '3. What language(s) do you speak at home?',
                '4. What is your race or ethnicity?',
                '5. Do you have children age 18 or younger who live with you?',
                '6. Describe your housing status in Somerville.',
                '8 How long have you lived here?',
                '9. What is your annual household income?', '10. Are you a student?']

# First we need to replace blanks with either "Blank" or "0"
replace_with_zero = ['1. How happy do you feel right now?',
                     '2. How satisfied are you with your life in general?',
                     '3. How anxious did you feel yesterday?',
                     '4. How satisfied are you with Somerville as a place to live?',
                     '5. How satisfied are you with your neighborhood?',
                     '6. How proud are you to be a Somerville resident?',
                     '7a. How would you rate the availability of information about city services?',
                     '7b. How would you rate the cost of housing?',
                     '7c. How would you rate the overall quality of public schools?',
                     '7d. How would you rate your trust in the local police?',
                     '7e. How would you rate the maintenance of streets and sidewalks?',
                     '7f. How would you rate the availability of social community events?',
                     '8. How satisfied are you with the quality and number of transportation options available to you?',
                     '9. How safe do you feel walking in your neighborhood at night?',
                     '10. How satisfied are you with the appearance of parks and squares in your neighborhood?',
                     '11. How satisfied are you with the beauty or physical setting of your neighborhood?']
for blankspot in replace_with_zero:
    somerville2017[blankspot] = somerville2017[blankspot].fillna(0)

replace_with_blank = ['Language submitted in:', '1. What is your gender', '2. Age?',
                      '3. What language(s) do you speak at home?',
                      '4. What is your race or ethnicity?',
                      '5. Do you have children age 18 or younger who live with you?',
                      '6. Describe your housing status in Somerville.',
                      '7. Do you plan to move away from Somerville in the next two years?',
                      '8 How long have you lived here?',
                      '9. What is your annual household income?', '10. Are you a student?']
for blankspot in replace_with_blank:
    somerville2017[blankspot] = somerville2017[blankspot].fillna('Blank')

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


def fixthething(things_to_replace, column, replace_to, the_data=somerville2017, being_fixed="After fixing",
                give_printout=True):
    print(f"----- {being_fixed} -----")
    for i in things_to_replace:
        the_data[f"{column}"] = the_data[f"{column}"].replace(i, f"{replace_to}")
    if give_printout is True:
        print(the_data[f"{column}"].value_counts())
        print("")


for both in both_selected:
    somerville2017["1. What is your gender"] = somerville2017["1. What is your gender"].replace(both, "Both selected")
print("\n----- Both selected -----")
print(somerville2017["1. What is your gender"].value_counts())

for multi in multiple_people:
    somerville2017["1. What is your gender"] = somerville2017["1. What is your gender"].replace(multi,
                                                                                                "Multiple people")
print("\n----- Multiple people -----")
print(somerville2017["1. What is your gender"].value_counts())

for gender in genderqueer:
    somerville2017["1. What is your gender"] = somerville2017["1. What is your gender"].replace(gender, "Non-binary")
print("\n----- Non-binary -----")
print(somerville2017["1. What is your gender"].value_counts())
print("")

# Age responses are fine

# These are the household languages declared. TODO: Ask Chris how these should be condensed
# Maybe... English, Non-English, English and 1 Other, English and 2 Others?
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
bilingual = ['English;Russian',
             'English;Spanish',
             'English;Portugese',
             'English;Italian',
             'English;Croatian',
             'English;Japanese',
             'English;Arabic',
             'English;Chinese',
             'English;Farsi',
             'English;French',
             'English;Sometimes Deutsch',
             'English;Nepali',
             'English;Danish',
             'English;Haitian Creole',
             'English;French Creole',
             'English;Jamaican Patois',
             'English;Bengali',
             'English;Bosnian',
             'English;Tamil',
             'English;Hindi',
             'English;Tibetan']
trilingual = ['English;Spanish;Haitian Creole',
              '3 languages',
              'English;Spanish;Portugese',
              'English;Vietnamese and Chinese',
              'English;German + ....',
              'English;Italian, Swedish',
              'English;Spanish;Mandarin',
              'English;Portugese;German',
              'English;Portugese;French',
              'English;Haitian Creole;French',
              'English;Spanish;Chinese']
portuguese = {'English;Portugese': 'English;Portuguese',
              'Portugese': 'Portuguese',
              'English;Spanish;Portugese': 'English;Spanish;Portuguese',
              'English;Portugese;German': 'English;Portuguese;German',
              'English;Portugese;French': 'English;Portuguese;French'}

fixthething(things_to_replace=['English;ENGLISH ONLY'],
            column='3. What language(s) do you speak at home?',
            replace_to='English', being_fixed='The one "English Only"')

fixthething(things_to_replace=['English;Sometimes Deutsch'],
            column='3. What language(s) do you speak at home?',
            replace_to='English;German', being_fixed='The one "sometimes Deutsch"')

for portuguesetypo in portuguese.keys():
    fixthething(things_to_replace=[portuguesetypo],
                column='3. What language(s) do you speak at home?',
                replace_to=portuguese[portuguesetypo], being_fixed=portuguesetypo,
                give_printout=False)
print(somerville2017['3. What language(s) do you speak at home?'].value_counts())
print("")

# These are the declared races/ethnicities.
race_or_ethnicity = ['White',
                     'Hispanic/Latino;Puertoriquena',
                     'Italian/Turkish Scottich/Irish',
                     'nan',
                     'Hispanic/Latino',
                     'Hispanic/Latino;White;Middle Eastern',
                     'Irish',
                     'Asian',
                     'Black/African American',
                     'Asian;White',
                     'Human',
                     'White;American - White',
                     'Arab', 'White;American',
                     'Black/African American;White',
                     'White;Semitic',
                     'Cape Verdean',
                     'Hispanic/Latino;White',
                     'Hispanic/Latino;Portuguese/American',
                     'Multi-cultural',
                     'Italy',
                     'White;Jewish',
                     'Black/African American;Human Race',
                     'Multi-Racial',
                     'White;Hawai\'ian',
                     'Black/African American;Hatian',
                     'Semitic',
                     'Arabic, French',
                     'Indian American',
                     'White;Italian',
                     'Asian;Hispanic/Latino;White',
                     'central american',
                     'Mixed',
                     'Jewish',
                     'Hispanic/Latino;Brazil',
                     'Italian/American']

quick_fixes_in_ethnicity = {'Hispanic/Latino;Puertoriquena': 'Hispanic/Latino',
                            'Italian/Turkish Scottich/Irish': 'Italian/Turkish;Scottish/Irish',
                            'Human': 'White',
                            'White;American - White': 'White',
                            'White;American': 'White',
                            'White;Semitic': 'White;Jewish',
                            'Multi-cultural': 'Multiple (unspecified)',
                            'Italy': 'Italian',
                            'Black/African American;Human Race': 'Black/African American',
                            'Multi-Racial': 'Multiple (unspecified)',
                            'Black/African American;Hatian': 'Black/African American;Haitian',
                            'Semitic': 'Jewish',
                            'Arabic, French': 'Arab;French',
                            'central american': 'Hispanic/Latino',
                            'Mixed': 'Multiple (unspecified)',
                            'Hispanic/Latino;Brazil': 'Hispanic/Latino',
                            'Italian/American': 'Italian'}  # Some are typos... others should be debated
for quick_fix in quick_fixes_in_ethnicity.keys():
    fixthething(things_to_replace=[quick_fix],
                column='4. What is your race or ethnicity?',
                replace_to=quick_fixes_in_ethnicity[quick_fix], being_fixed=quick_fix,
                give_printout=False)

fixthething(things_to_replace=['Black/African American;Human Race'],
            column='4. What is your race or ethnicity?',
            replace_to='Black/African American',
            being_fixed='The one "Human Race"')

# Children age 18 or younger is fine.

# Rent or own responses to consider.
neither_rent_nor_own = ['desability apt do governo',
                        'Sre Housing',
                        'selected both',
                        'Senior']
fixthething(things_to_replace=neither_rent_nor_own,
            column='6. Describe your housing status in Somerville.',
            replace_to='Neither',
            being_fixed='Neither Rent Nor Own')

# How long have you lived here? responses fine

# income responses fine.

# Are you student? responses fine.

somerville2017.to_csv(path_or_buf='cleanedData/2017HappinessSurvey.csv', index=False)
