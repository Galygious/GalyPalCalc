import subprocess
import sys

# Function to install packages using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing necessary packages, and install them if import fails
try:
    import tkinter as tk
    from tkinter import ttk  # Import ttk from tkinter
    from tkinter import Scale, Checkbutton, IntVar, HORIZONTAL, Frame, Label, Listbox, MULTIPLE
except ImportError:
    install('tkinter')  # Note: Tkinter is usually included with Python, might not need this line
    import tkinter as tk
    from tkinter import ttk  # Import ttk from tkinter after installation
    from tkinter import Scale, Checkbutton, IntVar, HORIZONTAL, Frame, Label, Listbox, MULTIPLE

try:
    import pandas as pd
except ImportError:
    install('pandas')
    import pandas as pd

try:
    from io import StringIO
except ImportError:
    install('io')  # Note: The 'io' module is included in standard Python, should not need to install
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
    
    # Extract constraints from the filters
    for pal_var, max_count_var in pal_constraint_vars:
        pal_name = pal_var.get()
        max_count = max_count_var.get()

        if pal_name and max_count.isdigit():  # Check if both fields are filled and max_count is a number
            max_count = int(max_count)
            # Apply this constraint to your optimization logic
            # For example, if using a linear programming model:
            # Find the index of the pal in your DataFrame
            pal_index = df[df['Name'] == pal_name].index.item()
            # Add a constraint for this pal
            prob += pal_vars[pal_index] <= max_count

    # Solve the problem
    status = prob.solve()

    # Check if an optimal solution was found
    if LpStatus[status] == 'Optimal':
        # Prepare team composition output
        team_output = ""
        for i in df.index:
            if pal_vars[i].varValue > 0:
                team_output += f"{int(pal_vars[i].varValue)} x {df.loc[i, 'Name']}\n"

        # Prepare skill total output
        skill_output = ""
        for skill in skill_columns:
            total_skill_exprating = sum(pal_vars[i].varValue * df.loc[i, f'{skill}_ExpVal'] for i in df.index)
            skill_output += f"{skill}: {total_skill_exprating}\n"
    else:
        # Prepare output for no solution
        team_output = "No optimal solution found. You may want to check the constraints.\n"
        skill_output = ""

    # Update the Team Composition Output Text widget
    team_output_text.config(state=tk.NORMAL)
    team_output_text.delete(1.0, tk.END)
    team_output_text.insert(tk.END, team_output)
    team_output_text.config(state=tk.DISABLED)

    # Update the Skill Totals Output Text widget
    skill_output_text.config(state=tk.NORMAL)
    skill_output_text.delete(1.0, tk.END)
    skill_output_text.insert(tk.END, skill_output)
    skill_output_text.config(state=tk.DISABLED)
    
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
        self.frame.grid()  # Use grid instead of pack

        self.label = Label(self.frame, text=label_text, width=10, anchor='w', fg='white', bg='black')
        self.label.grid(row=0, column=0, sticky='w', padx=(0, 10))  # Use grid instead of pack

        self.value = IntVar()
        self.slider = Scale(self.frame, from_=0, to=max_value, resolution=2, orient=HORIZONTAL, length=200, variable=self.value, bg='black', fg='white', troughcolor='grey')
        self.slider.grid(row=0, column=1, sticky='w')  # Use grid instead of pack

        self.slider.bind("<ButtonRelease-1>", slider_moved_callback)

        self.channel = None  # This will store the current channel of the slider

        self.channel_vars = []
        for i in range(num_channels):
            channel_var = IntVar()
            cb = Checkbutton(self.frame, text=f"Ch {i+1}", variable=channel_var, command=lambda i=i: self.update_channel(i), selectcolor='black', fg='white', bg='black', activebackground='black', activeforeground='white')
            cb.grid(row=0, column=2+i, sticky='w')  # Use grid instead of pack
            self.channel_vars.append(channel_var)

    def update_channel(self, channel_index):
        # Set the channel to the selected one or None if unselected
        if self.channel_vars[channel_index].get() == 1:
            self.channel = channel_index
        else:
            self.channel = None  # No channel assigned

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

    # Identify which slider was moved
    for slider in sliders:
        if slider.slider == event.widget:
            moved_slider = slider
            break

    if moved_slider and moved_slider.channel is not None:
        # Update all sliders in the same channel
        for slider in sliders:
            if slider.channel == moved_slider.channel and slider != moved_slider:
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
        
def limit_entry_size(var, maxlen=3):
    """Limits the size of the entry to maxlen characters."""
    if len(var.get()) > maxlen:
        var.set(var.get()[:maxlen])
def on_filter_change(*args):
    # Function called whenever a filter value changes
    recalculate_results()

root = tk.Tk()
root.title('GalyPalCalc')
root.configure(bg='black')

# Define a main container frame using grid
main_container = Frame(root, bg='black')
main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Configure the grid layout within the main container
main_container.grid_columnconfigure(0, weight=1)
main_container.grid_columnconfigure(1, weight=2)  # Blacklist frame may need more space
main_container.grid_columnconfigure(2, weight=2)  # Output frame may need more space
main_container.grid_columnconfigure(3, weight=1)  # Filter frame
main_container.grid_rowconfigure(0, weight=1)
main_container.grid_rowconfigure(1, weight=1)
main_container.grid_rowconfigure(2, weight=4)  # Sliders and channels may need more space
main_container.grid_rowconfigure(3, weight=4)  # Sliders and channels may need more space

# Left configuration frame for Max Pals, Max Constraints, and Infused (1,1)
left_config_frame = Frame(main_container, bg='black')
left_config_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create and place the Max Pals slider, Max Constraints slider, and Infused checkbox in left_config_frame
# Create the left_config_frame with a grid layout
left_config_frame = Frame(main_container, bg='black')
left_config_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create the IntVar for max_pals and max_constraints
max_pals_var = IntVar(value=1)
max_constraint_var = IntVar(value=100)
infused_var = IntVar()

# Max Pals label and slider
max_pals_label = Label(left_config_frame, text="Max Pals", fg='white', bg='black')
max_pals_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)
max_pals_slider = Scale(left_config_frame, from_=1, to=20, orient=HORIZONTAL, bg='black', fg='white', troughcolor='grey', variable=max_pals_var)
max_pals_slider.grid(row=1, column=0, sticky="ew", padx=5, pady=2)
max_pals_slider.bind("<ButtonRelease-1>", update_max_pals)

# Infused checkbutton
infused_checkbutton = Checkbutton(left_config_frame, text="Infused", variable=infused_var, selectcolor='black', fg='white', bg='black', activebackground='black', activeforeground='white')
infused_checkbutton.grid(row=2, column=0, sticky="w", padx=5, pady=2)

# Max Constraints label and slider
max_constraints_label = Label(left_config_frame, text="Max Constraints", fg='white', bg='black')
max_constraints_label.grid(row=3, column=0, sticky="w", padx=5, pady=2)
max_constraint_slider = Scale(left_config_frame, from_=20, to=640, resolution=20, orient=HORIZONTAL, bg='black', fg='white', troughcolor='grey', variable=max_constraint_var)
max_constraint_slider.grid(row=4, column=0, sticky="ew", padx=5, pady=2)
max_constraint_slider.bind("<ButtonRelease-1>", update_max_constraint)

# Center configuration frame for Blacklist (1,2 and 2,2)
center_config_frame = Frame(main_container, bg='black')
center_config_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

# Create and place the Blacklist section in center_config_frame
# Blacklist label
blacklist_label = Label(center_config_frame, text="Blacklist Pals", fg='white', bg='black')
blacklist_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)

# Blacklist listbox
blacklist_listbox = Listbox(center_config_frame, selectmode=MULTIPLE, bg='grey', fg='white', selectbackground='darkgrey', selectforeground='white', exportselection=False)
blacklist_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)  # 'nsew' makes the listbox expand
center_config_frame.grid_rowconfigure(1, weight=1)  # This allows the listbox to expand vertically
center_config_frame.grid_columnconfigure(0, weight=1)  # This allows the listbox to expand horizontally

# Binding for the blacklist update
blacklist_listbox.bind('<<ListboxSelect>>', on_blacklist_update)

# Populate the blacklist listbox with pal_names
for idx, name in enumerate(pal_names, 1):
    blacklist_listbox.insert(tk.END, f"{idx}. {name}")

# Right configuration frame for Output (1,3 and 2,3)
right_config_frame = Frame(main_container, bg='black')
right_config_frame.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=10, pady=10)

# Create and place the Team Composition Output and Skill Totals Output in right_config_frame
# Right configuration frame for Output (1,3 and 2,3)
right_config_frame = Frame(main_container, bg='black')
right_config_frame.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=10, pady=10)
right_config_frame.grid_columnconfigure(0, weight=1)  # Allow the team output frame to expand horizontally
right_config_frame.grid_columnconfigure(1, weight=1)  # Allow the skill output frame to expand horizontally

# Frame for Team Composition Output
team_output_frame = Frame(right_config_frame, bg='black')
team_output_frame.grid(row=0, column=0, sticky="nsew")

# Frame for Skill Totals Output
skill_output_frame = Frame(right_config_frame, bg='black')
skill_output_frame.grid(row=0, column=1, sticky="nsew")

# Text widget for Team Composition Output
team_output_text = tk.Text(team_output_frame, height=11, width=25, bg='black', fg='white', wrap=tk.WORD)
team_output_text.grid(row=0, column=0, sticky="nsew")
team_output_frame.grid_rowconfigure(0, weight=1)  # Allow the text widget to expand vertically
team_output_frame.grid_columnconfigure(0, weight=1)  # Allow the text widget to expand horizontally
team_output_text.config(state=tk.DISABLED)  # Set the text widget to read-only mode

# Text widget for Skill Totals Output
skill_output_text = tk.Text(skill_output_frame, height=11, width=25, bg='black', fg='white', wrap=tk.WORD)
skill_output_text.grid(row=0, column=0, sticky="nsew")
skill_output_frame.grid_rowconfigure(0, weight=1)  # Allow the text widget to expand vertically
skill_output_frame.grid_columnconfigure(0, weight=1)  # Allow the text widget to expand horizontally
skill_output_text.config(state=tk.DISABLED)  # Set the text widget to read-only mode

# Sliders section below the configuration frames (3,1 3,2 3,3 and 4,1 4,2 4,3)
sliders_frame = Frame(main_container, bg='black')
sliders_frame.grid(row=2, column=0, columnspan=3, rowspan=2, sticky="nsew", padx=10, pady=10)
main_container.grid_rowconfigure(2, weight=1)  # Allow the sliders frame to expand vertically
main_container.grid_rowconfigure(3, weight=1)  # Allow the sliders frame to expand vertically
main_container.grid_columnconfigure(0, weight=1)  # Allow the sliders frame to expand horizontally
main_container.grid_columnconfigure(1, weight=1)  # Allow the sliders frame to expand horizontally
main_container.grid_columnconfigure(2, weight=1)  # Allow the sliders frame to expand horizontally

# Create and place the sliders
skill_labels = ['Kindling', 'Watering', 'Planting', 'Electricity', 'Handiwork', 'Gathering', 'Lumbering', 'Mining', 'Medicine', 'Cooling', 'Transporting']
num_channels = 6
sliders = []
for i, label in enumerate(skill_labels):
    slider = LinkedSlider(sliders_frame, label, num_channels, on_slider_change)
    slider.frame.grid(row=i, column=0, columnspan=3, sticky="ew")
    sliders.append(slider)

# Filters frame (1,4 2,4 3,4 and 4,4)
filters_frame = Frame(main_container, bg='black')
filters_frame.grid(row=0, column=3, rowspan=4, sticky="nsew", padx=10, pady=10)

# Configure the grid within the filters frame
for i in range(16):  # Assuming 16 filters
    filters_frame.grid_rowconfigure(i, weight=1)

# Create dropdowns and entry fields for each filter
pal_constraint_vars = []
dropdown_width = 16  # Adjust this as needed to match the width of your blacklist element
for i in range(16):
    # Combobox for selecting an item
    pal_var = tk.StringVar()
    pal_combobox = ttk.Combobox(filters_frame, textvariable=pal_var, values=[''] + pal_names, state="readonly")
    pal_combobox.config(width=dropdown_width)
    pal_combobox.grid(row=i, column=0, sticky="ew", padx=(0, 5))

    # Entry field for specifying the constraint
    max_count_var = tk.StringVar()
    max_count_entry = tk.Entry(filters_frame, textvariable=max_count_var, width=3)
    max_count_entry.grid(row=i, column=1, sticky="ew")

    # Limit the size of the entry and other configurations
    max_count_var.trace("w", lambda name, index, mode, sv=max_count_var: limit_entry_size(sv))
    pal_constraint_vars.append((pal_var, max_count_var))

    # Store the variable references (if needed later)
    pal_constraint_vars.append((pal_var, max_count_var))

    # Bind the change event to the entry field's StringVar
    max_count_var.trace_add("write", on_filter_change)
    pal_var.trace_add("write", on_filter_change)

root.mainloop()


#recalculate_results()

root.mainloop()
