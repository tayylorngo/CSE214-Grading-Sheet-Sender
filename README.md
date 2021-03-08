# Grading Sheet Sender - CSE 214

## Introduction

* #### A python script that automatically sends grading sheets to all students in your recitation. 
* #### Designed specifically for CSE 214 Recitation Teaching Assistants.

## Usage
1. Python Installation 🐍
    * Install here: https://www.python.org/downloads/
    * I recommend installing the latest version
    * You can check that python is installed by running ```python``` in your command prompt

![python command](https://i.gyazo.com/14dcd095a25672f1e9c4af2d10f45a59.png)

2. Setup Gmail Account ✉️
    * If you do not have **two-factor authentication**, enable less secure app access
        #### https://myaccount.google.com/lesssecureapps
        ![googlelogin1](https://i.gyazo.com/0c7832ca47c6e7d497628166761df0b3.png)
      <br/>
      <br/>
    * If you have **two-factor authentication** enabled
    create an app and generate a password for an application.
        #### https://myaccount.google.com/apppasswords
        * After logging in click "Select app" and "Other (Custom name)"
          <br />
          <br />
          ![google login2](https://i.gyazo.com/5d59f8e1791a793d615eafa66e508b25.png)
          <br />
          <br />
        * Enter a name and generate a password. Save the password for later.
          <br />
          <br />
          ![google login3](https://i.gyazo.com/c6d1ccd85b8a30f9e4e60ed28ea944bb.png)
          <br />
          <br />

3. Download & Setup ⬇️
    * Download project in .zip and extract the 
    files in a new directory.
    * Create a **.env** file in the same directory as your **sendgrades.py** and **studentdata.py**
    * In the **.env** file create two variables: **EMAIL_ADDRESS** and **PASSWORD**
    * Set your email and password as such:   
      * ```EMAIL_ADDRESS = "youremail@gmail.com"```
      * ```PASSWORD = "email password" or "app password generated"``` (refer to step 2)
    * Create a new folder/directory named **gradingsheets** in the same directory as
      **sendgrades.py** and **studentdata.py** (This is where your .xlsx files will be stored)
    * In the **studentdata.py** put in all student data as a Python dictionary (you will only need to do this once I swear)
    * Follow this format:
      <br/>
        ![setup1](https://i.gyazo.com/f3c27c8470f15220bbedf5b040c4b2de.png)
    * Install the following libraries (you can use pip):
        * ```pip install python-dotenv```
        * ```pip install pylightxl```
          <br/>
        <br/>  
4. Run time ✔️
    * Put all your .xlsx files (grading sheets) into the **gradingsheets** directory
    * In the **sendgrades.py** enter the homework number and body message (if you want)
    ![runtime1](https://i.gyazo.com/009c31f918e45ef8d2ea1d4e00bb81cd.png)
      
    * Go to your terminal/command prompt and go to the directory in which your **sendgrades.py** file is located
    * Run ```python sendgrades.py```
    <br/><br/>
5. Output 🖥️
    * The console output will tell you the emails successfully sent, and the emails that were not sent
    * Usually if the emails were not sent, that means that in the .xlsx sheet, the name of the student
    was spelled incorrectly and you would have to manually send it 😪.
   * Sample output: 
     <br/>
      ![output1](https://i.gyazo.com/51e2bbc1f5fb1dca43650f832091bd67.png)
       * As you can see the successful emails sent have the full email posted while the non-successful ones 
         usually have some error with the naming.
         
## How It Works

* The grading sheets for CSE 214 are the same with the name section
being in cell G1.
* The formatting of the name is usually "Name: firstname lastname"
* This program reads the name from that cell and sends an email that
corresponds to that name in the student data table.
* If no name corresponds, no email is sent. 

## Testing
- Tested with Homework 2 - works exactly as expected. 

## Possible Errors
1. If the grading sheet is formatted differently.
2. If the name does not match in **studentdata.py**
then it will not send an email.