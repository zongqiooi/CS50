# Food Wheel
Not sure what to eat for dinner tonight? Always worried about what to eat after studying or working? No worries, Food Wheel is here to help you to solve the problem! Food Wheel is a web application that helps people to decide what to eat! The users can add all their favorite foods onto the food wheel and let the food wheel decides the dinner for them. Other than that, the users can also remove their favorite foods from the food wheel. In other words, users are allowed to customize their own food wheels by adding and removing their favorite foods on the food wheel. The food wheel will expand and shrink depending on the number of foods on the food wheel.


# Video Demo
https://www.youtube.com/watch?v=r1k6uTqmVLE


# Tech Stack Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python, SQLite
- Frameworks: Flask, Bootstrap


# Steps to Use Food Wheel
1) Download and open all the files in VS Code.
2) Change the directory to "project" by using the command `cd project`.
3) Run the web application with Flask by using the command `flask run`.
4) Add your favorite foods to the food wheel in the add section.
5) May remove the foods from the food wheel in the remove section.
6) Finally, spin the food wheel for it to decide the meal for you in the wheel section!
7) Optionally, you can view back all the history of adding and removing foods from the food wheel in the history section.


# Functionalities
In this web application, it consists of 4 sections with different functionalities:
1) ``Wheel``: The food wheel that consists of all the user's favorite foods to pick from.
2) ``Add``: The food will be added to the food wheel.
3) ``Remove``: The food will be removed from the food wheel.
4) ``History``: The history that keeps track of all the foods added and removed from the wheel.


# Files
- static
  - ``food.png``: Icon for the website.
  - ``styles.css``: The CSS file for the aesthetic of the food wheel and website.
- templates
  - ``layout.html``: The HTML file for the general layout of the website
  - ``wheel.html``: The HTML file for the wheel functionality.
  - ``add.html``: The HTML file for the add functionality.
  - ``remove.html``: The HTML file for the remove functionality.
  - ``history.html``: The HTML file for the history functionality.
- others
  - ``app.py``: The Python file that contains the main functions for the project, such as wheel(), add(), remove(), and history().
  - ``food.db``: The database file that stores the table for foods and history.
  - ``helpers.py``: The Python file that contains the apology() function.
  - ``READEME.md``: The text file that describes the whole project.
  - ``requirements.txt``: The text file that contains the name of all the required libraries.


# Reason for Developing Food Wheel
My family and I always hesitate about what to eat for our dinner so I decided to make use of the knowledge I learned from CS50 to make a web application that helps us to decide on our dinner!