import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    whites = len(df[df['race'] == 'White'])
    blacks = len(df[df['race'] == 'Black'])
    apis = len(df[df['race'] == 'Asian-Pac-Islander'])
    aies = len(df[df['race'] == 'Amer-Indian-Eskimo'])
    others = len(df[df['race'] == 'Other'])
    race_count = pd.Series(data=[whites, blacks, apis, aies, others])
    race_count.index = df['race'].unique()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((
        len(df[df['education'] == 'Bachelors']) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bachelors = len(df[(df['education'] == 'Bachelors')
                       & (df['salary'] == '>50K')])
    masters = len(df[(df['education'] == 'Masters')
                     & (df['salary'] == '>50K')])
    doctorates = len(df[(df['education'] == 'Doctorate')
                        & (df['salary'] == '>50K')])

    len_higher_degrees = len(df[df['education'] == 'Bachelors']) + len(
        df[df['education'] == 'Masters']) + len(df[df['education'] == 'Doctorate'])

    higher_education_rich = (
        (bachelors + masters + doctorates) / len_higher_degrees) * 100

    len_lower_degrees_50K = len(df[~(df['education'] == 'Bachelors') & ~(
        df['education'] == 'Masters') & ~(df['education'] == 'Doctorate') & (df['salary'] == '>50K')])

    len_lower_degrees = len(df[~(df['education'] == 'Bachelors') & ~(
        df['education'] == 'Masters') & ~(df['education'] == 'Doctorate')])
    lower_education_rich = (len_lower_degrees_50K / len_lower_degrees) * 100

    # percentage with salary >50K
    # higher_education_rich = None
    # lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(
        df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])

    rich_percentage = len(
        df[df['hours-per-week'] == min_work_hours]) / num_min_workers

    # What country has the highest percentage of people that earn >50K?

    salary_dict = {}
    maxed_country = ''
    maxed_value = 0

    for c in df['native-country'].unique():
        try:
            one_h = len(df[df['native-country'] == c]) / \
                len(df[(df['native-country'] == c) & (df['salary'] == '>50K')])
            salary_dict[c] = 100 / one_h
            maxed_value = max(maxed_value, salary_dict[c])
            if maxed_value == salary_dict[c]:
                maxed_country = c
        except:
            salary_dict[c] = 0

    highest_earning_country = maxed_country
    highest_earning_country_percentage = maxed_value

    # Identify the most popular occupation for those who earn >50K in India.
    india = list(df[(df['native-country'] == 'India') &
                    (df['salary'] == '>50K')].groupby('occupation').size().items())
    maxed = df[(df['native-country'] == 'India') &
               (df['salary'] == '>50K')].groupby('occupation').size().max()
    top_IN_occupation = [x for x in india if x[1] == maxed][0][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
