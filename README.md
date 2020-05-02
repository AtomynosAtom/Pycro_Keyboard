# Pycro_Keys
Configure an entire keyboard to be a macro board with Python! Inspired by the MacroKing.

Have you ever wondered if I could configure an entire 2nd Keyboard to run commands?
Well wonder no more because I had done the same goddam thing and finially decided to explore the internet to find methods to do such things.
And I came up with a solution that may not be pretty but it works....

# How to set this up...

1st => Make sure you are using Linux... If you are using Windows then the Macro King has already made tutorials for you.

2nd => Make sure you have ssh enabled on boot and also passwordless entry **AS ROOT TO USER**. That means you should be able to ssh into the user without a password.(I know this may be a shitty way but it works...) To do that run 'ssh-keygen' as root to generate keys **without a password** and then 'ssh-copy-id user@localhost'.

3rd => Copy InfoEXAMPLE.json to Info.json and fill in the username and host.

4th => Get the keyboard name and keyboard id name by these commands(make sure you have them installed):-

xinput list -> copy you 2nd_keyboard name **exactly how it is displayed** and paste it into the KeyboardName value of the Info.json file.

cat /proc/bus/input/devices -> copy the event number of your 2nd_keyboard and now remember that.

udevadm info --query=property --name=/dev/input/event**THE EVENT NUMBER** -> Copy the words after 'ID_SERIAL=' **exactly how it is displayed** and paste it into the ID_Name value of the Info.json file.


5th => Save the Info.json file

6th => Install the requirements for the program. (sudo pip3 install requirements.txt)

7th => Give your self a pat on the back as you just finished configuring your 2nd Keyboard.

8th => Run the main.py as root (sudo python3 main.py) and if succeeded then redo the 7th step else I wish you good luck debugging :)

# How to configure commands
Now for the fun and painfull part. You notice how there is a Keys.json file. Yes its my current configuration. If you want a blank one then replace it with the BACKUP one. Commands may vary due to my crappy coding.



## If you have any ideas please do tell or if you can make my code better please do. This is my 1st Github project btw so expect mistakes.
