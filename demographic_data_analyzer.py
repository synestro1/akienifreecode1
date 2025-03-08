import pandas as pd


def calculate_demographic_data(print_data=True):
    # Lire les données d'un fichier
    df = pd.read_csv("adult.data.csv")

    # Combien de personnes de chaque race sont représentées dans cet ensemble de données ? Il devrait s'agir d'une série Pandas avec les noms des courses comme étiquettes d'index.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # Quel est le pourcentage de personnes titulaires d'une licence ?
    num_bachelors = len(df[df["education"] == "Bachelors"])
    total_num = len(df)
    percentage_bachelors = round(num_bachelors / total_num * 100, 1)

    # Quel est le pourcentage de personnes ayant suivi une formation supérieure(`Bachelors`, `Masters`, or `Doctorate`) gagner plus de 50 000 $ ?
    # Quel est le pourcentage de personnes sans formation supérieure qui gagnent plus de 50 000 $ ?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    
    # pourcentage du salaire >50K
    non_percentage_higher = len(higher_education[higher_education.salary == ">50K"])

    higher_education_rich = round(non_percentage_higher / len(higher_education) * 100, 1)
    non_percentage_lower = len(lower_education[lower_education.salary == ">50K"])

    lower_education_rich = round(non_percentage_lower / len(lower_education) * 100, 1)
    

    

    # Quel est le nombre minimum d'heures de travail hebdomadaire d'une personne ? (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # Quel est le pourcentage des personnes qui travaillent le nombre minimum d'heures par semaine et qui ont un salaire >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round(len(num_min_workers[num_min_workers.salary == ">50K"])/ len(num_min_workers) * 100, 1)

    # Quel est le pays où le pourcentage de personnes qui gagnent de l'argent est le plus élevé ?>50K?
    country_count = df['native-country'].value_counts()  
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_rich_count / country_count * 100).idxmax()
    highest_earning_country_percentage = round((country_rich_count / country_count * 100).max(), 1)

    # Identifiez la profession la plus populaire pour ceux qui gagnent plus de 50 000 $ en Inde.
    people_of_india = df[(df['native-country'] == "India") & (df['salary'] == ">50K")]
    occupation_counts = people_of_india['occupation'].value_counts()
    top_IN_occupation = occupation_counts.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
