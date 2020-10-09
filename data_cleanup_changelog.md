# Data Cleanup
This is a record of the rationale behind data cleanup
choices. Empty responses were replaced with either ```0``` or ```blank```.

## Demographics
### Gender
So, a notable quantity of the survey responses are
inconsistent and need to be standardized. For example,

- (Female and Male selected)
- Female + Male checked
- Checked Female & Male

There are several explanations for these responses. 
First, that they are, in fact, gender fluid, non-binary, 
intersex, etc., and second, that they are a household
with more than one person and this reflects that. 
Other responses show this ambiguity more:

- Two People filled this out
- non binary female
- both make \[sic\] and female checked
- I don't believe in the social construct of gender

These have been condensed to:

- Both selected
- Multiple people
- Non-binary

### Languages in the home

The number of distinct languages is quite numerous
and condensing them can't be justified until we have
a clear language-related research question (e.g., 
"Are bilingual/trilingual people more likely to...").

Changes were standardization or typo fixing only.

- 'English Only' -> 'English'
- 'English;sometimes Deutsch' -> 'English;German'
- 'Portugese' -> 'Portuguese'

### Race/Ethnicity

As with languages, condensing was hard to justify.
Some of these I'm not 100% sure whether I want to
keep the changes or not.

Changes were:

- 'Hispanic/Latino;Puertoriquena': 'Hispanic/Latino'
- 'Italian/Turkish Scottich/Irish': 'Italian/Turkish;Scottish/Irish',
- 'Human': 'White',
- 'White;American - White': 'White',
- 'White;American': 'White',
- 'White;Semitic': 'White;Jewish',
- 'Multi-cultural': 'Multiple (unspecified)',
- 'Italy': 'Italian',
- 'Black/African American;Human Race': 'Black/African American',
- 'Multi-Racial': 'Multiple (unspecified)',
- 'Black/African American;Hatian': 'Black/African American;Haitian',
- 'Semitic': 'Jewish',
- 'Arabic, French': 'Arab;French',
- 'central american': 'Hispanic/Latino',
- 'Mixed': 'Multiple (unspecified)',
- 'Hispanic/Latino;Brazil': 'Hispanic/Latino',
- 'Italian/American': 'Italian'

