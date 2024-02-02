import sys

# Function to install packages using pip
def install(package):
    if hasattr(sys, 'real_prefix'):
        # We are in a virtual environment, so use pip to install
        !{sys.executable} -m pip install {package}
    else:
        # We are not in a virtual environment, so try to install globally
        !pip install {package}

# Try importing necessary packages, and install them if import fails
try:
    import tkinter as tk
    from tkinter import Scale, Checkbutton, IntVar, HORIZONTAL, Frame, Label, Listbox, MULTIPLE
except ImportError:
    install('tkinter')
    import tkinter as tk
    from tkinter import Scale, Checkbutton, IntVar, HORIZONTAL, Frame, Label, Listbox, MULTIPLE

try:
    import pandas as pd
except ImportError:
    install('pandas')
    import pandas as pd

try:
    from io import StringIO
except ImportError:
    install('io')
    from io import StringIO

try:
    from pulp import *
except ImportError:
    install('pulp')
    from pulp import *



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

# Extract pal names from the csv_data
csv_io = StringIO(csv_data)
pal_df = pd.read_csv(csv_io)
pal_names = sorted(pal_df['Name'].tolist())
max_value = 100

def recalculate_results():
    # Retrieve the current values from the sliders
    slider_values = {slider.label['text']: slider.value.get() for slider in sliders}
    
    # Retrieve whether 'Infused' is checked
    Infused = bool(infused_var.get())
    
    # Retrieve the selected blacklist items
    selected_indices = blacklist_listbox.curselection()
    blacklist = [blacklist_listbox.get(i).split(". ", 1)[-1] for i in selected_indices]  # Remove the number prefix
    
    # Set the maximum number of Pals from the slider
    max_pals = int(max_pals_var.get())

    # Load your data into a DataFrame
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
    
    # Update minimum exprating requirements from sliders
    min_exprating_requirements = {}
    for slider in sliders:
        skill = slider.label['text']
        try:
            # Ensure slider_value is a valid integer
            slider_value = int(slider.value.get())
            if slider_value > 0:
                min_exprating_requirements[skill] = slider_value
            else:
                min_exprating_requirements[skill] = 0
        except ValueError:
            # Handle the case where slider_value is not a valid integer
            min_exprating_requirements[skill] = 0  # Set to 0 as a default value
            print(f"Warning: Invalid slider value for skill '{skill}'. Setting to 0.")
        except Exception as e:
            # Handle any other exceptions
            min_exprating_requirements[skill] = 0  # Set to 0 as a default value
            print(f"Error: An exception occurred for skill '{skill}': {e}")



    # Add constraints for minimum exprating requirements for each skill
    for skill in skill_columns:
        if min_exprating_requirements[skill] > 0:
            prob += lpSum([pal_vars[i] * df.loc[i, f'{skill}_ExpVal'] for i in df.index]) >= min_exprating_requirements[skill]

    # Add a constraint for the maximum number of Pals
    prob += lpSum([pal_vars[i] for i in df.index]) <= max_pals

    # Solve the problem
    status = prob.solve()

    # Output the results
    results_text = ""
    if LpStatus[status] == 'Optimal':
        for i in df.index:
            if pal_vars[i].varValue > 0:
                results_text += f"{int(pal_vars[i].varValue)} x {df.loc[i, 'Name']}\n"
    else:
        results_text += "No optimal solution found. You may want to check the constraints.\n"

    # Update the output Text widget with the results
    output_text.config(state=tk.NORMAL)  # Enable editing of the widget
    output_text.delete(1.0, tk.END)  # Clear existing text
    output_text.insert(tk.END, results_text)  # Insert new text
    output_text.config(state=tk.DISABLED)  # Set back to read-only mode
    
# Define a callback function to set the maximum constraint
def set_maximum_constraint():
    try:
        max_constraint = int(max_constraint_entry.get())
        if max_constraint >= 1 and max_constraint <= 1000:
            for slider in sliders:
                slider.slider.configure(to=max_constraint)
            recalculate_results()
        else:
            print("Invalid maximum constraint. Please enter a value between 1 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 1000.")

class LinkedSlider:    
    def __init__(self, master, label_text, num_channels, slider_moved_callback):
        self.frame = Frame(master, bg='black')
        self.frame.pack()

        self.label = Label(self.frame, text=label_text, width=10, anchor='w', fg='white', bg='black')
        self.label.pack(side=tk.LEFT, padx=(0, 10))

        self.value = IntVar()
        self.slider = Scale(self.frame, from_=0, to=max_value, resolution=2, orient=HORIZONTAL, length=200, variable=self.value, bg='black', fg='white', troughcolor='grey')
        self.slider.pack(side=tk.LEFT)

        self.slider.bind("<ButtonRelease-1>", slider_moved_callback)

        self.channel = None  # This will store the current channel of the slider

        self.channel_vars = []
        for i in range(num_channels):
            channel_var = IntVar()
            cb = Checkbutton(self.frame, text=f"Ch {i+1}", variable=channel_var, command=lambda i=i: self.update_channel(i), selectcolor='black', fg='white', bg='black', activebackground='black', activeforeground='white')
            cb.pack(side=tk.LEFT)
            self.channel_vars.append(channel_var)

    def update_channel(self, channel_index):
        # Update the channel of the slider
        self.channel = channel_index

        # Ensure only one channel is selected at a time
        for i, var in enumerate(self.channel_vars):
            if i != channel_index:
                var.set(0)


    def get_selected_channel(self):
        for i, var in enumerate(self.channel_vars):
            if var.get() == 1:
                return i
        return None

def on_slider_change(event):
    moved_slider = None
    moved_slider_channel = None

    # Identify which slider was moved and its channel
    for slider in sliders:
        if slider.slider == event.widget:
            moved_slider = slider
            moved_slider_channel = slider.channel
            break

    if moved_slider_channel is not None:
        # Update all sliders in the same channel
        for slider in sliders:
            if slider.channel == moved_slider_channel and slider != moved_slider:
                slider.slider.set(moved_slider.value.get())
    
    recalculate_results()

def on_blacklist_update(event):
    recalculate_results()

# Define a callback function to update max_pals
def update_max_pals(_):
    max_pals_var.set(max_pals_slider.get())
    recalculate_results()

# Define a callback function to update max_pals
def update_max_constraint(_):
    max_value = max_constraint_slider.get()
    for slider in sliders:
        slider.slider.config(to=max_value)

root = tk.Tk()
root.title('Linked Sliders Configuration')
root.configure(bg='black')

# Main configuration frame
config_frame = Frame(root, bg='black')
config_frame.pack(side=tk.TOP, fill=tk.X)

# Left configuration frame for Max Pals and Infused
left_config_frame = Frame(config_frame, bg='black')
left_config_frame.pack(side=tk.LEFT, padx=10)

# Max Pals Slider
Label(left_config_frame, text="Max Pals", fg='white', bg='black').pack()
max_pals_slider = Scale(left_config_frame, from_=1, to=20, orient=HORIZONTAL, bg='black', fg='white', troughcolor='grey', command=update_max_pals)
max_pals_slider.pack()

# Create a IntVar to store max_pals value
max_pals_var = IntVar()

# Link the StringVar to the slider and set the initial value
max_pals_slider.config(variable=max_pals_var)
max_pals_slider.set(1)  # Set an initial value

# Max constraint Slider
Label(left_config_frame, text="Max Constraints", fg='white', bg='black').pack()
max_constraint_slider = Scale(left_config_frame, from_=20, to=640, resolution = 20, orient=HORIZONTAL, bg='black', fg='white', troughcolor='grey', command=update_max_constraint)
max_constraint_slider.pack()

# Create a IntVar to store max_pals value
max_constraint_var = IntVar()

# Link the StringVar to the slider and set the initial value
max_constraint_slider.config(variable=max_constraint_var)
max_constraint_slider.set(100)  # Set an initial value

# Infused Checkbutton
infused_var = IntVar()
Checkbutton(left_config_frame, text="Infused", variable=infused_var, command=recalculate_results, selectcolor='black', fg='white', bg='black', activebackground='black', activeforeground='white').pack()

# Center configuration frame for Blacklist
center_config_frame = Frame(config_frame, bg='black')
center_config_frame.pack(side=tk.LEFT, padx=10)

# Blacklist section
Label(center_config_frame, text="Blacklist Pals", fg='white', bg='black').pack()
blacklist_listbox = Listbox(center_config_frame, selectmode=MULTIPLE, bg='grey', fg='white', selectbackground='darkgrey', selectforeground='white')
blacklist_listbox.pack()
blacklist_listbox.bind('<<ListboxSelect>>', on_blacklist_update)
for idx, name in enumerate(pal_names, 1):
    blacklist_listbox.insert(tk.END, f"{idx}. {name}")

# Right configuration frame for Output
right_config_frame = Frame(config_frame, bg='black')
right_config_frame.pack(side=tk.LEFT, padx=10)

# Output Text widget
output_text = tk.Text(right_config_frame, height=10, width=50, bg='black', fg='white', wrap=tk.WORD)
output_text.pack()
output_text.config(state=tk.DISABLED)  # Start with the text widget in read-only mode

# Sliders section below the configuration frames
sliders_frame = Frame(root, bg='black')
sliders_frame.pack(fill=tk.X, pady=10)
skill_labels = ['Kindling', 'Watering', 'Planting', 'Electricity', 'Handiwork', 'Gathering', 'Lumbering', 'Mining', 'Medicine', 'Cooling', 'Transporting']
num_channels = 6
sliders = [LinkedSlider(sliders_frame, label, num_channels, on_slider_change) for label in skill_labels]

recalculate_results()

root.mainloop()
