import pandas as pd

df = pd.read_csv('survey_results_public.csv')

# Series -> 1D array
# Dataframe -> 2D array

# rows x cols
# print(df.shape)

# rows x cols + datatypes
# print(df.info())

# top rows
# print(df.head(10))
# bottom rows
# print(df.tail(10))

# column names
# print(df.columns)
# Index(['Respondent', 'MainBranch', 'Hobbyist', 'OpenSourcer', 'OpenSource',
#        'Employment', 'Country', 'Student', 'EdLevel', 'UndergradMajor',
#        'EduOther', 'OrgSize', 'DevType', 'YearsCode', 'Age1stCode',
#        'YearsCodePro', 'CareerSat', 'JobSat', 'MgrIdiot', 'MgrMoney',
#        'MgrWant', 'JobSeek', 'LastHireDate', 'LastInt', 'FizzBuzz',
#        'JobFactors', 'ResumeUpdate', 'CurrencySymbol', 'CurrencyDesc',
#        'CompTotal', 'CompFreq', 'ConvertedComp', 'WorkWeekHrs', 'WorkPlan',
#        'WorkChallenge', 'WorkRemote', 'WorkLoc', 'ImpSyn', 'CodeRev',
#        'CodeRevHrs', 'UnitTests', 'PurchaseHow', 'PurchaseWhat',
#        'LanguageWorkedWith', 'LanguageDesireNextYear', 'DatabaseWorkedWith',
#        'DatabaseDesireNextYear', 'PlatformWorkedWith',
#        'PlatformDesireNextYear', 'WebFrameWorkedWith',
#        'WebFrameDesireNextYear', 'MiscTechWorkedWith',
#        'MiscTechDesireNextYear', 'DevEnviron', 'OpSys', 'Containers',
#        'BlockchainOrg', 'BlockchainIs', 'BetterLife', 'ITperson', 'OffOn',
#        'SocialMedia', 'Extraversion', 'ScreenName', 'SOVisit1st',
#        'SOVisitFreq', 'SOVisitTo', 'SOFindAnswer', 'SOTimeSaved',
#        'SOHowMuchTime', 'SOAccount', 'SOPartFreq', 'SOJobs', 'EntTeams',
#        'SOComm', 'WelcomeChange', 'SONewContent', 'Age', 'Gender', 'Trans',
#        'Sexuality', 'Ethnicity', 'Dependents', 'SurveyLength', 'SurveyEase'],
#       dtype='object')

# column (series)
# df['Country']
# print(df.Country)

# columns (dataframe)
# print(df[['Country', 'YearsCodePro']])

# get stuff by integer_location
# col
# print(df.iloc[0])
# cols
# print(df.iloc[[0,1]])
# col and row (cell)
# print(df.iloc[[1], [1]])

# get stuff by name and integer location
# row
# print(df.loc[0])
# row and col
# print(df.loc[[0,1], ['Country']])
# filtered row and col (cols are inclusive)
# print(df.loc[0:2, 'Hobbyist': 'Employment'])

# set index (from integer to unique value)
# df.set_index('Respondent')

### FILTERS

# filt = df['Country'] == 'United Kingdom'
# print(df[filt])

# multiple and not
# filt = (df['Country'] == 'United Kingdom')|( df['Country'] == 'Spain')
# print(df[-filt])

# count different values
# print(df['Country'].value_counts())
# normalise
# print(df['Country'].value_counts(normalize=True))

