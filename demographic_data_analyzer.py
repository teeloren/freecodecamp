import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/teeloren/freecodecamp/main/adult.data.csv')

####columns ['age', 'capital-gain', 'capital-loss', 'education', 'education-num', 'fnlwgt', 'hours-per-week', 'marital-status', 'native-country', 'occupation', 'race', 'relationship', 'salary', 'sex', 'workclass']

ed = df['education']
total = ed.count()
ed_val = ed.value_counts()
bach = ed_val['Bachelors']
percentage_bachelors = bach/total*100

higher = ed_val['Masters'] + ed_val['Doctorate'] + ed_val['Bachelors']
higher_education = (higher/total)*100
lower_education = ((total - higher)/total)*100

salary_50K = df[df['salary'] == '>50K']
salary_total = salary_50K['education'].count()
salary_val = salary_50K['education'].value_counts()
higher_sal = salary_val['Masters'] + \
    salary_val['Doctorate'] + salary_val['Bachelors']

higher_education_rich = (higher_sal/salary_total)*100
lower_education_rich = ((salary_total - higher_sal)/salary_total)*100


# What is the minimum number of hours a person works per week (hours-per-week feature)?
hrs = df['hours-per-week']
min_work_hours = min(hrs)
# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
min_people = df[hrs == min_work_hours]
min_total = min_people['hours-per-week'].count()

num_min_workers = min_people[min_people['salary'] == '>50K']['salary'].count()
rich_percentage = (num_min_workers/min_total)*100

# What country has the highest percentage of people that earn >50K?
country = df['native-country']
country_total = country.value_counts()
country_50K = salary_50K['native-country'].value_counts()
country_perc = (country_50K/country_total)*100
dt = country_perc.loc[country_perc == max(country_perc)]

dict_country = dt.to_dict()
for key, value in dict_country.items():
    highest_earning_country = key
    highest_earning_country_percentage = value


# Identify the most popular occupation for those who earn >50K in India.
India_50K = salary_50K['native-country']
pop_occ = salary_50K[salary_50K['native-country']
                     == 'India']['occupation'].value_counts()
most_pop_occ = pop_occ.loc[pop_occ == max(pop_occ)]

dict_pop_occ = most_pop_occ.to_dict()
for key, value in dict_pop_occ.items():
    top_IN_occupation = key
    print(top_IN_occupation)


# def calculate_demographic_data(print_data=True):
#     # Read data from file
#     df = pd.read_csv(
#         'https://raw.githubusercontent.com/teeloren/freecodecamp/main/adult.data.csv')

#     # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
#     df_race = df[['race']]
#     race_count = df_race.value_counts()

#     # What is the average age of men?
#     df_men = df[df['sex'] == 'Male']
#     average_age_men = df_men['age'].mean()

#     # What is the percentage of people who have a Bachelor's degree?
#     ed = df['education']
# total = ed.count()
# ed_val = ed.value_counts()
# bach = ed_val['Bachelors']
# percentage_bachelors = bach/total*100


#     # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
#     # What percentage of people without advanced education make more than 50K?

#     # with and without `Bachelors`, `Masters`, or `Doctorate`
#     higher = ed_val['Masters'] + ed_val['Doctorate'] + ed_val['Bachelors']
#   higher_education = (higher/total)*100
#    lower = total - higher
#   lower_education = (lower/total)*100

#     # percentage with salary >50K
#     higher_education_rich = None
#     lower_education_rich = None

#     # What is the minimum number of hours a person works per week (hours-per-week feature)?
#     min_work_hours = None

#     # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
#     num_min_workers = None

#     rich_percentage = None

#     # What country has the highest percentage of people that earn >50K?
#     highest_earning_country = None
#     highest_earning_country_percentage = None

#     # Identify the most popular occupation for those who earn >50K in India.
#     top_IN_occupation = None

#     # DO NOT MODIFY BELOW THIS LINE

#     if print_data:
#         print("Number of each race:\n", race_count)
#         print("Average age of men:", average_age_men)
#         print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
#         print(
#             f"Percentage with higher education that earn >50K: {higher_education_rich}%")
#         print(
#             f"Percentage without higher education that earn >50K: {lower_education_rich}%")
#         print(f"Min work time: {min_work_hours} hours/week")
#         print(
#             f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
#         print("Country with highest percentage of rich:", highest_earning_country)
#         print(
#             f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
#         print("Top occupations in India:", top_IN_occupation)

#     return {
#         'race_count': race_count,
#         'average_age_men': average_age_men,
#         'percentage_bachelors': percentage_bachelors,
#         'higher_education_rich': higher_education_rich,
#         'lower_education_rich': lower_education_rich,
#         'min_work_hours': min_work_hours,
#         'rich_percentage': rich_percentage,
#         'highest_earning_country': highest_earning_country,
#         'highest_earning_country_percentage':
#         highest_earning_country_percentage,
#         'top_IN_occupation': top_IN_occupation
#     }


# print(calculate_demographic_data(print_data=True))
