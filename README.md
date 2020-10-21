# Group Project for CIT-383

Goal for project 1 was to display the contents in two files passwd and group to archive the two files for access, and also implement ifconfig into the file so the network information is put into a file. this way the administrator can transfer the csv file into another area freely after that.

I (Jin Nagai) came up with the idea so that all the contents can easily be put into a spreadsheet to log a batch of usernames and names of the individuals into the spreadsheet. 

The spreadsheet:
1. Displays ifconfig aka the network information
2. Displays the current ant total users from /etc/passwd
3. Displays the current ant total groups from /etc/group

This is to automate 3 things to neatly categorize later into a spreadsheet with 1 python script. Administrators are suppose to maintain network security, user information, groups created on the server for book keeping so I came up with the three important things to bundle up.

Instructions on how to run the python file
1. Ensure the file has execute privileges (if not 'chmod u+x project1.py')
2. Run ./project1.py in the project directory

Displays the three listed above in a csv file named system_audit.csv

---

##### Description by Jin Nagai and Quinn Brittain