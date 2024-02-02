#======================================================================================================
#DONT EDIT THIS FILE UNLESS YOU KNOW WHAT YOU ARE DOING.
#======================================================================================================
import subprocess
import sys
from io import StringIO

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pandas as pd
except ImportError:
    install('pandas')
    import pandas as pd

try:
    from pulp import *
except ImportError:
    install('pulp')
    from pulp import *

# Import configuration variables from PacCalc.cfg
from GalyPalCalcConfig import max_pals, Infused, blacklist, min_exprating_requirements

#Define the CSV data as a multi-line string
csv_data = """Name,Kindling,Watering,Planting,Electricity,Handiwork,Gathering,Lumbering,Mining,Medicine,Cooling,Transporting,ExpSum,,,,,,,,,,,
Lyleen,0,0,4,0,3,2,0,0,3,0,0,36,,,,,,,,,,,
Wumpo,0,0,0,0,2,0,3,0,0,2,4,32,,,,,,,,,,,
Wumpo Botan,0,0,1,0,2,0,3,0,0,0,4,30,,,,,,,,,,,
Verdash,0,0,2,0,3,3,2,0,0,0,2,28,,,,,,,,,,,
Anubis,0,0,0,0,4,0,0,3,0,0,2,28,,,,,,,,,,,
Orserk,0,0,0,4,2,0,0,0,0,0,3,28,,,,,,,,,,,
Blazamut,3,0,0,0,0,0,0,4,0,0,0,24,,,,,,,,,,,
Grizzbolt,0,0,0,3,2,0,2,0,0,0,3,24,,,,,,,,,,,
Vaelet,0,0,2,0,2,2,0,0,3,0,1,22,,,,,,,,,,,
Petallia,0,0,3,0,2,2,0,0,2,0,1,22,,,,,,,,,,,
Penking,0,2,0,0,2,0,0,2,0,2,2,20,,,,,,,,,,,
Mossanda,0,0,2,0,2,0,2,0,0,0,3,20,,,,,,,,,,,
Mossanda Lux,0,0,0,2,2,0,2,0,0,0,3,20,,,,,,,,,,,
Bushi,2,0,0,0,1,1,3,0,0,0,2,20,,,,,,,,,,,
Warsect,0,0,1,0,1,0,3,0,0,0,3,20,,,,,,,,,,,
Lyleen Noct,0,0,0,0,3,2,0,0,3,0,0,20,,,,,,,,,,,
Robinquill,0,0,1,0,2,2,1,0,1,0,2,18,,,,,,,,,,,
Elizabee,0,0,2,0,2,2,1,0,2,0,0,18,,,,,,,,,,,
Quivern,0,0,0,0,1,2,0,2,0,0,3,18,,,,,,,,,,,
Astegon,0,0,0,0,1,0,0,4,0,0,0,18,,,,,,,,,,,
Robinquill Terra,0,0,0,0,2,2,1,0,1,0,2,16,,,,,,,,,,,
Ragnahawk,3,0,0,0,0,0,0,0,0,0,3,16,,,,,,,,,,,
Wixen,2,0,0,0,3,0,0,0,0,0,2,16,,,,,,,,,,,
Reptyro,3,0,0,0,0,0,0,3,0,0,0,16,,,,,,,,,,,
Reptyro Cryst,0,0,0,0,0,0,0,3,0,3,0,16,,,,,,,,,,,
Jormuntide,0,4,0,0,0,0,0,0,0,0,0,16,,,,,,,,,,,
Jormuntide Ignis,4,0,0,0,0,0,0,0,0,0,0,16,,,,,,,,,,,
Faleris,3,0,0,0,0,0,0,0,0,0,3,16,,,,,,,,,,,
Frostallion,0,0,0,0,0,0,0,0,0,4,0,16,,,,,,,,,,,
Frostallion Noct,0,0,0,0,0,4,0,0,0,0,0,16,,,,,,,,,,,
Beegarde,0,0,1,0,1,1,1,0,1,0,2,14,,,,,,,,,,,
Gorirat,0,0,0,0,1,0,2,0,0,0,3,14,,,,,,,,,,,
Lovander,0,0,0,0,2,0,0,1,2,0,2,14,,,,,,,,,,,
Beakon,0,0,0,2,0,1,0,0,0,0,3,14,,,,,,,,,,,
Cryolinx,0,0,0,0,1,0,2,0,0,3,0,14,,,,,,,,,,,
Bristla,0,0,1,0,1,1,0,0,2,0,1,12,,,,,,,,,,,
Incineram,1,0,0,0,2,0,0,1,0,0,2,12,,,,,,,,,,,
Lunaris,0,0,0,0,3,1,0,0,0,0,1,12,,,,,,,,,,,
Tombat,0,0,0,0,0,2,0,2,0,0,2,12,,,,,,,,,,,
Vanwyrm Cryst,0,0,0,0,0,0,0,0,0,2,3,12,,,,,,,,,,,
Katress,0,0,0,0,2,0,0,0,2,0,2,12,,,,,,,,,,,
Elphidran Aqua,0,3,0,0,0,0,2,0,0,0,0,12,,,,,,,,,,,
Blazehowl,3,0,0,0,0,0,2,0,0,0,0,12,,,,,,,,,,,
Blazehowl Noct,3,0,0,0,0,0,2,0,0,0,0,12,,,,,,,,,,,
Mammorest,0,0,2,0,0,0,2,2,0,0,0,12,,,,,,,,,,,
Mammorest Cryst,0,0,0,0,0,0,2,2,0,2,0,12,,,,,,,,,,,
Menasting,0,0,0,0,0,0,2,3,0,0,0,12,,,,,,,,,,,
Lifmunk,0,0,1,0,1,1,1,0,1,0,0,10,,,,,,,,,,,
Tanzee,0,0,1,0,1,1,1,0,0,0,1,10,,,,,,,,,,,
Flopie,0,0,1,0,1,1,0,0,1,0,1,10,,,,,,,,,,,
Hangyu Cryst,0,0,0,0,1,1,0,0,0,1,2,10,,,,,,,,,,,
Incineram Noct,0,0,0,0,2,0,0,1,0,0,2,10,,,,,,,,,,,
Vanwyrm,1,0,0,0,0,0,0,0,0,0,3,10,,,,,,,,,,,
Kingpaca Cryst,0,0,0,0,0,1,0,0,0,3,0,10,,,,,,,,,,,
Sibelyx,0,0,0,0,0,0,0,0,2,2,0,8,,,,,,,,,,,
Cattiva,0,0,0,0,1,1,0,1,0,0,1,8,,,,,,,,,,,
Pengullet,0,1,0,0,1,0,0,0,0,1,1,8,,,,,,,,,,,
Gobfin,0,2,0,0,1,0,0,0,0,0,1,8,,,,,,,,,,,
Gobfin Ignis,2,0,0,0,1,0,0,0,0,0,1,8,,,,,,,,,,,
Hangyu,0,0,0,0,1,1,0,0,0,0,2,8,,,,,,,,,,,
Dumud,0,1,0,0,0,0,0,2,0,0,1,8,,,,,,,,,,,
Leezpunk Ignis,1,0,0,0,1,1,0,0,0,0,1,8,,,,,,,,,,,
Sweepa,0,0,0,0,0,2,0,0,0,2,0,8,,,,,,,,,,,
Reindrix,0,0,0,0,0,0,2,0,0,2,0,8,,,,,,,,,,,
Dinossom,0,0,2,0,0,0,2,0,0,0,0,8,,,,,,,,,,,
Dinossom Lux,0,0,0,2,0,0,2,0,0,0,0,8,,,,,,,,,,,
Digtoise,0,0,0,0,0,0,0,3,0,0,0,8,,,,,,,,,,,
Azurobe,0,3,0,0,0,0,0,0,0,0,0,8,,,,,,,,,,,
Broncherry,0,0,3,0,0,0,0,0,0,0,0,8,,,,,,,,,,,
Broncherry Aqua,0,3,0,0,0,0,0,0,0,0,0,8,,,,,,,,,,,
Felbat,0,0,0,0,0,0,0,0,3,0,0,8,,,,,,,,,,,
Helzephyr,0,0,0,0,0,0,0,0,0,0,3,8,,,,,,,,,,,
Suzaku,3,0,0,0,0,0,0,0,0,0,0,8,,,,,,,,,,,
Suzaku Aqua,0,3,0,0,0,0,0,0,0,0,0,8,,,,,,,,,,,
Paladius,0,0,0,0,0,0,2,2,0,0,0,8,,,,,,,,,,,
Necromus,0,0,0,0,0,0,2,2,0,0,0,8,,,,,,,,,,,
Jetragon,0,0,0,0,0,3,0,0,0,0,0,8,,,,,,,,,,,
Flambelle,1,0,0,0,1,0,0,0,0,0,1,6,,,,,,,,,,,
Fuack,0,1,0,0,1,0,0,0,0,0,1,6,,,,,,,,,,,
Sparkit,0,0,0,1,1,0,0,0,0,0,1,6,,,,,,,,,,,
Depresso,0,0,0,0,1,0,0,1,0,0,1,6,,,,,,,,,,,
Daedream,0,0,0,0,1,1,0,0,0,0,1,6,,,,,,,,,,,
Fuddler,0,0,0,0,1,0,0,1,0,0,1,6,,,,,,,,,,,
Killamari,0,0,0,0,0,1,0,0,0,0,2,6,,,,,,,,,,,
Ribbuny,0,0,0,0,1,1,0,0,0,0,1,6,,,,,,,,,,,
Cinnamoth,0,0,2,0,0,0,0,0,1,0,0,6,,,,,,,,,,,
Arsox,2,0,0,0,0,0,1,0,0,0,0,6,,,,,,,,,,,
Leezpunk,0,0,0,0,1,1,0,0,0,0,1,6,,,,,,,,,,,
Univolt,0,0,0,2,0,0,1,0,0,0,0,6,,,,,,,,,,,
Pyrin,2,0,0,0,0,0,1,0,0,0,0,6,,,,,,,,,,,
Dazzi,0,0,0,1,1,0,0,0,0,0,1,6,,,,,,,,,,,
Maraith,0,0,0,0,0,2,0,1,0,0,0,6,,,,,,,,,,,
Relaxaurus,0,2,0,0,0,0,0,0,0,0,1,6,,,,,,,,,,,
Relaxaurus Lux,0,2,0,1,0,0,0,0,0,0,0,6,,,,,,,,,,,
Lamball,0,0,0,0,1,0,0,0,0,0,1,4,,,,,,,,,,,
Caprity,0,0,2,0,0,0,0,0,0,0,0,4,,,,,,,,,,,
Celaray,0,1,0,0,0,0,0,0,0,0,1,4,,,,,,,,,,,
Eikthyrdeer,0,0,0,0,0,0,2,0,0,0,0,4,,,,,,,,,,,
Eikthyrdeer Terra,0,0,0,0,0,0,2,0,0,0,0,4,,,,,,,,,,,
Nitewing,0,0,0,0,0,2,0,0,0,0,0,4,,,,,,,,,,,
Loupmoon,0,0,0,0,2,0,0,0,0,0,0,4,,,,,,,,,,,
Galeclaw,0,0,0,0,0,2,0,0,0,0,0,4,,,,,,,,,,,
Grintale,0,0,0,0,0,2,0,0,0,0,0,4,,,,,,,,,,,
Swee,0,0,0,0,0,1,0,0,0,1,0,4,,,,,,,,,,,
Chillet,0,0,0,0,0,1,0,0,0,1,0,4,,,,,,,,,,,
Foxcicle,0,0,0,0,0,0,0,0,0,2,0,4,,,,,,,,,,,
Pyrin Noct,1,0,0,0,0,0,1,0,0,0,0,4,,,,,,,,,,,
Rayhound,0,0,0,2,0,0,0,0,0,0,0,4,,,,,,,,,,,
Kisun,2,0,0,0,0,0,0,0,0,0,0,4,,,,,,,,,,,
Surfent,0,2,0,0,0,0,0,0,0,0,0,4,,,,,,,,,,,
Elphidran,0,0,0,0,0,0,2,0,0,0,0,4,,,,,,,,,,,
Fenglope,0,0,0,0,0,0,2,0,0,0,0,4,,,,,,,,,,,
Humans,0,0,0,0,1,0,0,0,0,0,0,2,,,,,,,,,,,
Chikipi,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Vixy,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Cremis,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Mau Cryst,0,0,0,0,0,0,0,0,0,1,0,2,,,,,,,,,,,
Foxparks,1,0,0,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Rooby,1,0,0,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Jolthog,0,0,0,1,0,0,0,0,0,0,0,2,,,,,,,,,,,
Jolthog Cryst,0,0,0,0,0,0,0,0,0,1,0,2,,,,,,,,,,,
Gumoss,0,0,1,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Hoocrates,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Teafant,0,1,0,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Rushoar,0,0,0,0,0,0,0,1,0,0,0,2,,,,,,,,,,,
Nox,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Direhowl,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Tocotoco,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Cawgnito,0,0,0,0,0,0,1,0,0,0,0,2,,,,,,,,,,,
Surfent Terra,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Kelpsea,0,1,0,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Kelpsea Ignis,1,0,0,0,0,0,0,0,0,0,0,2,,,,,,,,,,,
Kingpaca,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Shadowbeak,0,0,0,0,0,1,0,0,0,0,0,2,,,,,,,,,,,
Mau,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,
Mozzarina,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,
Woolipop,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,
Melpaca,0,0,0,0,0,0,0,0,0,0,0,0,,,,,,,,,,,
"""



# Load your data into a DataFrame
#df = pd.read_excel('Pals.xlsx')
df = pd.read_csv(StringIO(csv_data))

# Filter out the blacklisted pals
df = df[~df['Name'].isin(blacklist)]

# Define the skill columns, excluding 'Food' and 'Farming'
skill_columns = ['Kindling', 'Watering', 'Planting', 'Electricity', 
                 'Handiwork', 'Gathering', 'Lumbering', 'Mining', 'Medicine', 
                 'Cooling', 'Transporting']

# Ensure all skill level columns are numeric
for col in skill_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Update DataFrame with correct exponential values
for skill in skill_columns:
    exp_values = []
    for skill_level in df[skill]:
        adjusted_skill_level = skill_level + 1 if Infused and skill_level > 0 else skill_level
        exp_values.append(2 ** adjusted_skill_level if skill_level > 0 else 0)
    df[f'{skill}_ExpVal'] = exp_values

# Initialize the optimization problem
prob = LpProblem("BestPalCombination", LpMaximize)

# Define integer variables for each possible Pal, allowing multiple selections of the same Pal
pal_vars = LpVariable.dicts("Pal", df.index, lowBound=0, upBound=max_pals, cat='Integer')

# The objective function is to maximize the total exprating
prob += lpSum([pal_vars[i] * df.loc[i, 'ExpSum'] for i in df.index])

# Add constraints for minimum exprating requirements for each skill, taking into account the exponential nature of skill effectiveness
for skill in skill_columns:
    if skill in min_exprating_requirements and min_exprating_requirements[skill] > 0:
        prob += lpSum([pal_vars[i] * df.loc[i, f'{skill}_ExpVal'] for i in df.index]) >= min_exprating_requirements[skill]

# Add a constraint for the maximum number of Pals
prob += lpSum([pal_vars[i] for i in df.index]) <= max_pals

# Solve the problem
status = prob.solve()

# Output the results
if LpStatus[status] == 'Optimal':
    print(f"Total 'ExpSum' of selected Pals: {value(prob.objective)}")
    for skill in skill_columns:
        total_skill_exprating = sum(pal_vars[i].varValue * df.loc[i, f'{skill}_ExpVal'] for i in df.index)
        print(f"Total exprating for {skill}: {total_skill_exprating}")
    for i in df.index:
        if pal_vars[i].varValue > 0:
            print(f"{pal_vars[i].varValue} instances of Pal {df.loc[i, 'Name']} are selected")
else:
    print("No optimal solution found. You may want to check the constraints.")

    
# Now, open the file to write the updated output
with open('output.txt', 'w') as output_file:
    # Write the optimization results to the file
    if LpStatus[status] == 'Optimal':
        output_file.write(f"Total 'ExpSum' of selected Pals: {value(prob.objective)}\n")
        for skill in skill_columns:
            total_skill_exprating = sum(pal_vars[i].varValue * df.loc[i, f'{skill}_ExpVal'] for i in df.index)
            output_file.write(f"Total exprating for {skill}: {total_skill_exprating}\n")
        for i in df.index:
            if pal_vars[i].varValue > 0:
                output_file.write(f"{pal_vars[i].varValue} instances of Pal {df.loc[i, 'Name']} are selected\n")
    else:
        output_file.write("No optimal solution found. You may want to check the constraints.\n")

