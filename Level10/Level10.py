import pandas as pd

# Read the football data
football = pd.read_csv("Level10/cfb.csv")

season = int(input("Enter the season to analyze: "))

# Get only the teams from the season
season_data = football[football['Season'] == season]

if len(season_data) == 0:
    print("Season not found.")

else:
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

# Put each team into the right category
    for index, row in season_data.iterrows():
        team = row['Team']
        wins = row['Win']

        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8-9 wins"].append(team)
        elif wins >= 6:
            categories["6-7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)

    for category, teams in categories.items():
        print(f"\nCollege Football Teams with {season}")
        
# Print each category and its teams
for category in categories:
    print(f"\n{category}:")

    for team in categories[category]:
        print(team)