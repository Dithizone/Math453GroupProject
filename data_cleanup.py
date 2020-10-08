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
gender = demographics['1. What is your gender']  # 506 female, 283 male

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

gender.value_counts().plot(kind='bar')
plt.show()
print(gender.value_counts())
