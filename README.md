# GalyPalCalc - Palworld Pal Optimizer
GalyPalCalc is a Python script designed to calculate the best possible Pal setup in the game Palworld, given certain constraints. It uses linear programming to optimize the selection of Pals based on their skills and user-defined constraints.

## Requirements<br>
Python (3.x recommended)<br>
Pandas<br>
PuLP<be>

# Introducing GalyPalCalc UI :computer:

I'm excited to bring a significant enhancement to GalyPalCalc with the launch of a separate UI version: `GalyPalCalcUi.pyw`. This new version introduces a graphical user interface, offering a more interactive and user-friendly way to optimize your Pal setups in Palworld.

## Key Features of GalyPalCalc UI:
- **Dedicated UI Script**: `GalyPalCalcUi.pyw` is a standalone script, specifically designed for a graphical interface experience.
- **Interactive Elements**: Utilize sliders, checkboxes, and buttons for an easy and intuitive setup process.
- **Real-Time Visualization**: See your Pal configuration updates in real time as you adjust your preferences in the UI.
- **User-Friendly Interface**: Whether you're a seasoned gamer or new to Palworld, the UI is designed to be straightforward and easy to navigate.

## Installation<br>
Python Installation<br>
Ensure you have Python installed on your machine. You can download Python from here.<br>
<br>
### Script Setup<br>
Clone the repository or download the script files (GalyPalCalc.py and GalyPalCalcConfig.py) from the GitHub repository.<br>
```
git clone https://github.com/Galygious/GalyPalCalc
```
Navigate to the script's directory.<br>
```
cd GalyPalCalc
```
## Running the UI Version:
To experience the new UI, run the dedicated script:
```
python GalyPalCalcUi.pyw
```
This will launch the graphical interface where you can interactively configure and optimize your Pal setups.

## Upcoming Documentation:
I will provide detailed documentation on how to fully utilize GalyPalCalc UI tomorrow. This comprehensive guide will include step-by-step instructions and tips to enhance your user experience.

Your feedback on this new UI version is invaluable. I look forward to hearing about your experiences and suggestions for further improvements. Try out GalyPalCalc UI and take your Palworld gaming to the next level!

### Dependencies
The script will automatically install required Python packages (pandas and pulp) if they are not already installed.<br>

## Non-UI Usage (deprecated)<br>
Basic Execution: Run the script using Python.<br>
```
python GalyPalCalc.py
```
### Output
The script will output the optimal Pal configuration to the console and write the results to an output.txt file.<be>
#### Example Output
```
Total 'ExpSum' of selected Pals: 344.0
Total exprating for Kindling: 16.0
Total exprating for Watering: 32.0
Total exprating for Planting: 44.0
Total exprating for Electricity: 16.0
Total exprating for Handiwork: 52.0
Total exprating for Gathering: 32.0
Total exprating for Lumbering: 28.0
Total exprating for Mining: 40.0
Total exprating for Medicine: 16.0
Total exprating for Cooling: 16.0
Total exprating for Transporting: 52.0
2.0 instances of Pal Lyleen are selected
2.0 instances of Pal Wumpo are selected
3.0 instances of Pal Verdash are selected
1.0 instances of Pal Orserk are selected
2.0 instances of Pal Blazamut are selected
1.0 instances of Pal Reptyro Cryst are selected
2.0 instances of Pal Jormuntide are selected
```

## Configuration
You can customize the script's behavior by editing the GalyPalCalcConfig.py file. Available configuration options include:<br>
<br>
max_pals: Maximum number of Pals.<br>
Infused: Include Pals with infusion (True/False).<br>
blacklist: List of Pal names to exclude.<br>
min_exprating_requirements: Minimum exprating requirements for each skill.<br>

#### Example Config
```
# Define the maximum number of Pals
max_pals = 13

# Include pals with infusion?
Infused = False

# Define a blacklist of pal names
blacklist = ['Frostallion Noct', 'Frostallion', 'Jetragon', 'Necromus', 'Paladius', 'Jormuntide Ignis']

# Define minimum exprating requirements for each skill
min_exprating_requirements = {
    'Kindling': 16,
    'Watering': 32,
    'Planting': 32,
    'Electricity': 16,
    'Handiwork': 32,
    'Gathering': 32,
    'Lumbering': 16,
    'Mining': 32,
    'Medicine': 16,
    'Cooling': 16,
    'Transporting': 32
}
```
### Understanding Exprating (Exponential Rating)
In Palworld, the effectiveness of a Pal's skills is assumed to increase in a manner that seems more exponential than linear. This assumption is the basis for the exprating (Exponential Rating) used in our script.<br>

#### The Exponential Model
I use the formula 2^skill_level to calculate exprating. This model is based on the observation that each additional skill level contributes significantly more to a Pal's effectiveness than the previous one.<br>

#### Practical Example
To put this into perspective, let's consider a scenario:<br>

Scenario: You want an exprating of 32 in the Kindling skill.<br>
Interpretation: An exprating of 32 in Kindling would be equivalent to having two Pals, each with a Kindling skill level of 4.<br>
Calculation: Since the exprating for a level 4 skill is 2^4 (which equals 16), having two such Pals would give you 2 × 16 = 32 in exprating.<br>
This example shows how exprating provides a more nuanced understanding of a Pal's skill effectiveness, especially when comparing Pals with different skill levels.<br>

### Infusion Consideration
The script also factors in the possibility of skill level enhancement through infusion, extending the maximum skill level to 5. The exprating adjusts accordingly, reflecting these higher potential skill levels.<br>

#### Assumption Disclaimer
It's important to remember that this exponential model is an educated guess based on gameplay observations, not a confirmed game mechanic. This model is used to approximate the perceived impact of skill levels in the game and might not precisely reflect the game's actual mechanics.



## Credits and Disclaimer
Assistance from ChatGPT-4<br>
This script was developed with the assistance of ChatGPT-4, an AI language model created by OpenAI. ChatGPT-4 provided guidance and suggestions in various aspects of the script's development, including logic implementation, troubleshooting, and documentation.

### AI Collaboration
Collaborating with an AI model like ChatGPT-4 offered unique insights and accelerated the development process. However, it's important to note that while ChatGPT-4 is a powerful tool, it's not infallible. The suggestions and guidance provided by the AI were carefully considered and integrated with the developer's expertise and understanding of the game mechanics.

### User Discretion
As with any tool or resource, users are encouraged to use their discretion and judgment when utilizing the script. Feedback and contributions are welcome to continually improve and refine its functionality.
