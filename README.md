# PRODIGY_CS_03
Password-Strength-Tool
Description
This tool assesses the strength of a password based on length, presence of uppercase and lowercase letters, digits, and special characters.
Installation
How It Works
User Input: The user enters their password into a text field in the GUI.
Assessment: When the user clicks the "Check Strength" button, the check_password function is called. This function retrieves the password from the entry field and calls the assess_password_strength function.
Feedback: The assess_password_strength function checks the password against the defined criteria and returns a strength rating (Weak, Medium, Strong) along with feedback messages for any unmet criteria.
Display Results: The results are shown to the user in a message box, providing them with clear feedback on how to improve their password if necessary.

You can install this tool using pip:

```bash
pip install .

After installation you can run this tools in your linux termninal by simply typing passwd_stg_tool on the command line interface, this will open the Graphical User Interface.
Paste your Password to check the Strength. 

