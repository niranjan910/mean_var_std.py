import pandas as pd

def calculate_demographic_data():
    # Read the dataset
    df = pd.read_csv('adult.data.csv')

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Percentage of people without advanced education earning >50K
    lower_education_rich = round((df[~higher_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work minimum hours and earn >50K
    min_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round((df[min_workers]['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    highest_earning_country = (country_earning / country_count * 100).idxmax()
    highest_earning_country_percentage = round((country_earning / country_count * 100).max(), 1)

    # 9. Most popular occupation in India for people earning >50K
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    # Return the results
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
