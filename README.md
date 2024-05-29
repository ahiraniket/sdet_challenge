# Fetch SDET Challenge

## Introduction
This script is designed to automate the process of identifying a fake bar (among nine bars) using the website provided in the SDET coding challenge. The fake bar is determined using a balance scale. The script utilizes Selenium for browser automation to interact with the web page.

## Prerequisites
Before running the program, ensure the following prerequisites are met:
- **Python Installation**: Python 3.x should be installed on the system.
- **Pip Installation**: Ensure `pip` is installed to manage Python packages.
- **WebDriver**: The solution uses Chrome WebDriver. Ensure the Chrome browser is installed on the system. The script will automatically install `chromedriver` using the `chromedriver_autoinstaller` package and requires the Selenium package for browser automation.


## Setup Instructions
Follow these steps to set up and run the program successfully:
1. **Clone Repository**: Clone or download the repository to your local machine.
```
git clone https://github.com/ahiraniket/sdet_challenge.git
cd sdet_challenge
```
2. **Install Dependencies**: Install required Python dependencies by running the following:
```
pip install -r requirements.txt
```
3. **Execute Program**: Run the Python script `fetchsdet.py` using the following on your CLI:
``` 
python fetchsdet.py
```
4. **WebDriver Execution**: The WebDriver will automate the process of finding the fake bar on the challenge website.
5. **Interactive Quit Option**: After execution, choose to quit the WebDriver when prompted.


## Algorithm Explanation
The algorithm identifies the fake bar in three weighings by dividing the bars into groups and comparing their weights:

1. **Divide into 3 Groups**:
Divide the 9 bars into three groups of three bars each: group1, group2, and group3.

2. **First Weighing**:
- Weigh group1 against group2.
- If they balance, the fake bar is in group3.
- If group1 is lighter, the fake bar is in group1.
- If group2 is lighter, the fake bar is in group2.

3. **Second Weighing**:
- Take the suspect group identified from the first weighing (three bars).
- Weigh two bars from this group against each other.
- If they balance, the remaining bar is the fake one.
- If one is lighter, it is the fake bar.

This ensures that the fake bar is identified in at most three weightings.

## Code Documentation
1. **Weigh Function**:
The weigh function automates filling the balance scale and clicking the "Weigh" button. It waits for the result of the weighing and returns it.

2. **Find Fake Bar Function**:
The find_fake_bar function implements the algorithm to identify the fake bar. It uses the weigh function to compare groups of bars and determine which group contains the fake bar, then narrows it down to the specific fake bar.

3. **Main Function**:
The main function orchestrates the overall process, from finding the fake bar to clicking the correct bar and handling the resulting alert. It prints the number of weighings and the result of each weighing and prompts the user to confirm quitting the WebDriver.

### Note
If you encounter any issues or have any questions, please feel free to reach out at `aaahir@asu.edu`.
