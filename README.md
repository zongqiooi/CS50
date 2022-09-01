# CS50's Introduction to Computer Science
CS50 is an introductory course to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web programming. Languages include C, Python, and SQL plus HTML, CSS, and JavaScript. Problem sets inspired by the arts, humanities, social sciences, and sciences. Course culminates in a final project. Designed for concentrators and non-concentrators alike, with or without prior programming experience. Two thirds of CS50 students have never taken CS before. Among the overarching goals of this course are to inspire students to explore unfamiliar waters, without fear of failure, create an intensive, shared experience, accessible to all students, and build community among students.

This CS50 repository contains all the labs and problem sets that I have submitted for all the coursework. Below summarizes some of the projects for the labs and problem sets. 

# Week 0: Scratch (Wizard Pong) 
Wizard Pong is a game that is created for CS50 Problem Set 0. The game is created by using Scratch. The users can press up and down keys to control the broomstick in the game. Score 8 points to win. 

## Some Screenshots from Wizard Pong 
<img src="https://user-images.githubusercontent.com/95561298/178139018-6e0da0f1-185c-4887-8dde-b528f854dd0e.png" height="400" width="550">
<img src="https://user-images.githubusercontent.com/95561298/178139025-4b98da6e-e2bc-4b92-9660-f7cc49a3e08e.png" height="400" width="550">

## Link
Visit this Scratch link to play the game!: https://scratch.mit.edu/projects/711721445/

# Week 1: C (Credit)
Credit is a program that is created for CS50 Problem Set 1. The program is used to check the types of credit cards and it is created by using C. The users will be prompted to enter a credit card number in integers. After that, the program will be classified whether the credit card number is AMEX (American Express), MASTERCARD, VISA, or INVALID. The validity of the Visa card is checked by using Luhn's Algorithm. 

## Information about Credit Cards
A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a quadrillion.)

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.

## Some Screenshots from Credit
![cs50 pset 1 ss1](https://user-images.githubusercontent.com/95561298/178524440-8af3579e-5b1d-4d44-a48a-7468b3a8eb79.png)

# Week 2: Arrays (Substitution)
Substitution is a program that is created for CS50 Problem Set 2. The program is used to encrypt plaintext into ciphertext and it is created by using C. The users have to run the C file with an extra command line argument known as "key", in the format of "./substitution key". Then, the users will be prompted to enter plaintext in strings. After that, the plaintext will be encrypted into ciphertext based on the "key" entered in the command line argument.

## Information about Substitution (Encryption)
In a substitution cipher, we “encrypt” (i.e., conceal in a reversible way) a message by replacing every letter with another letter. To do so, we use a key: in this case, a mapping of each of the letters of the alphabet to the letter it should correspond to when we encrypt it. To “decrypt” the message, the receiver of the message would need to know the key, so that they can reverse the process: translating the encrypt text (generally called ciphertext) back into the original message (generally called plaintext).

A key, for example, might be the string NQXPOMAFTRHLZGECYJIUWSKDVB. This 26-character key means that A (the first letter of the alphabet) should be converted into N (the first character of the key), B (the second letter of the alphabet) should be converted into Q (the second character of the key), and so forth.

A message like HELLO, then, would be encrypted as FOLLE, replacing each of the letters according to the mapping determined by the key.

## Some Screenshots from Substitution 
![cs50 pset 2 ss1](https://user-images.githubusercontent.com/95561298/178780713-7ed243c2-bde3-45c6-ba51-61721e1e5970.png)

# Week 3: Algorithms (Tideman)
Tideman is a program that is created for CS50 Problem Set 3. The program is used to determine the winner in an election and it is created by using C. The users have to run the C file with extra command line arguments known as "[candidates ...]", in the format of "./tideman [candidates ...]". The users will then be prompted to enter the number of voters. Every voter gets to cast three votes for three different candidates. Then, the program will determine the winner in the tideman election.

## Information about Tideman 
Tideman voting method consists of three parts:
1) **Tally**: Once all of the voters have indicated all of their preferences, determine, for each pair of candidates, who the preferred candidate is and by what margin they are preferred.
2) **Sort**: Sort the pairs of candidates in decreasing order of strength of victory, where strength of victory is defined to be the number of voters who prefer the preferred candidate.
3) **Lock**: Starting with the strongest pair, go through the pairs of candidates in order and “lock in” each pair to the candidate graph, so long as locking in that pair does not create a cycle in the graph.

Once the graph is complete, the source of the graph (the one with no edges pointing towards it) is the winner!

## Some Screenshots from Tideman
![cs50 pset 3 ss1](https://user-images.githubusercontent.com/95561298/179237447-00202646-fb69-4b54-a4b0-8bf8753de26d.png)

# Week 4: Memory (Filter)
Filter is a program that is created for CS50 Problem Set 4. The program is used to filter the input image and it is created by using C. The users have to run the C file with 3 extra command line arguments, in the format of "./filter -x images/yard.bmp out.bmp", where "-x" can be "-g", "-r", "-b" or "-e" that stands for grayscale, reflect, blur, or edges. The original image to be filtered is as shown below. 

![image](https://user-images.githubusercontent.com/95561298/179399686-3f151d31-855b-410d-9f7b-d76d28a70d66.png)

## Information about Filter 
Filter can be used to filter image by 4 different ways:
1) **Grayscale**: The function grayscale should take an image and turn it into a black-and-white version of the same image. Grayscale is represented by "-g". The grayscaled image is as shown below. 
2) **Reflect**: The reflect function should take an image and reflect it horizontally. Reflect is represented by "-r". The reflected image is as shown below. 
3) **Blur**: The blur function should take an image and turn it into a box-blurred version of the same image. Blur is represented by "-b". The blurred image is as shown below.
4) **Edges**: The edges function should take an image and highlight the edges between objects, according to the Sobel operator. Edges is represented by "-e". The edges of the image are detected by using Sobel Edge Detection algorithm and the filtered image is as shown below. 

## Some Filtered Images from Filter
**Grayscale**

![image](https://user-images.githubusercontent.com/95561298/179400065-0775ea0b-6506-4191-bdc3-d39047aca9df.png)

**Reflect**

![image](https://user-images.githubusercontent.com/95561298/179400077-00b39fe1-275a-40e1-8dfb-517de5adf266.png)

**Blur**

![image](https://user-images.githubusercontent.com/95561298/179400083-f7f1d4ec-ed9f-45ac-a5cb-cb58b8536a79.png)

**Edges**

![image](https://user-images.githubusercontent.com/95561298/179400094-affb9d61-49cd-4220-b746-a2b66fe14608.png)

# Week 5: Data Structures (Speller) 
Speller is a program that is created for CS50 Problem Set 5. The program is used to check the spelling of the words in a text file based on the vocabulary that can be found in a dictionary and it is created by using C. The users have to run the C file with an extra command line argument, in the format of "./speller texts/xxx.txt", where "xxx.txt" can be any file name of text files in the texts directory such as "lalaland.txt", "cat.txt", "aca.txt", and etc. 

## Information about Speller Checking 
The speller consists of five functions: 
1) **Load**: Load all the vocabulary in a dictionary into the hashtable, by dynamically allocating the memory.
2) **Hash**: Hash word to a number.
3) **Size**: Calculate the number of words in a dictionary. 
4) **Check**: Check whether the spelling of the word is correct based on the vocabulary in a dictionary. 
5) **Unload**: Unload all the vocabulary in a dictionary from the hashtable, by freeing the memory allocated. 

## Some Screenshots from Speller
![image](https://user-images.githubusercontent.com/95561298/179654665-bec2b5e0-3472-4dc5-8b4f-109a3fe96aae.png)

.
.
.

![image](https://user-images.githubusercontent.com/95561298/179654776-dfcd72f9-10b1-443c-a249-d17acae8085c.png)

# Week 6: Python (DNA)
DNA is a program that is created for CS50 Problem Set 6. The program is used to identify a person based on their DNA and it is created by using Python. The users have to run the Python file with two extra command line arguments, in the format of "python dna.py databases/*.csv sequences/*.txt", where "databases/*.csv" can be any csv files that can be found in the databases directory and "sequences/*.txt" can be any text files that can be found in the sequences directory. 

## Information about DNA 
DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?

Well, DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.


![image](https://user-images.githubusercontent.com/95561298/180004659-a308ae99-898b-4277-92c3-63ac6b476f54.png)


Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, the FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.
```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```
The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.

Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

## Some Screenshots from DNA
![image](https://user-images.githubusercontent.com/95561298/180004109-d59d689d-87c6-41fd-883a-aad7fb79c66f.png)

# Week 7: SQL (Fiftyville)
Fiftyville is a program that is created for CS50 Problem Set 7. The program is used to solve the mystery in Fiftyville by querying the data in a database using SQL. The users have to run the SQL file by using `cat log.sql | sqlite3 fiftyville.db` to read the SQL commands written in "log.sql" and pipe it to query the database known as "fiftyvilel.db". The thief, the city of the thief escaped to, and the accomplice of the thief are shown in the last three tables on the output terminal. 

## Information about Fiftyville  
The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:

* Who the thief is,
* What city the thief escaped to, and
* Who the thief’s accomplice is who helped them escape

All you know is that the theft **took place on July 28, 2021** and that it **took place on Humphrey Street**.

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town’s records from around the time of the theft and prepared a SQLite database for you, `fiftyville.db`, which contains tables of data from around the town. You can query that table using SQL SELECT queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery.

## Some Screenshots from Fiftyville 
![image](https://user-images.githubusercontent.com/95561298/180398194-165792ff-05e9-4c98-a7b5-1abdd14f2ad9.png)

![image](https://user-images.githubusercontent.com/95561298/180398278-42b6dd70-260a-45e1-87ca-ae4d0dcb0a63.png)

![image](https://user-images.githubusercontent.com/95561298/180398324-20a7a6d7-3094-4af8-9d65-3d65ae68b48e.png)

![image](https://user-images.githubusercontent.com/95561298/180398380-8f3028bc-1f2a-4fd9-9bfa-58a7ab7fd3b9.png)

# Week 8: HTML, CSS, Javascript (Trivia)
Trivia is a webpage that is created for CS50 Lab 8. The webpage enables the users to answer trivia questions by using HTML, CSS, and Javascript. The users get to answer 2 questions, which are multiple choice questions and free response questions. After that, feedback will be generated immediately based on the users' answers given. 

## Information about Trivia 
Design a webpage using HTML, CSS, and JavaScript to let users answer trivia questions.

- In index.html, add beneath “Part 1” a multiple-choice trivia question of your choosing with HTML.
  - You should use an h3 heading for the text of your question.
  - You should have one button for each of the possible answer choices. There should be at least three answer choices, of which exactly one should be correct.
- Using JavaScript, add logic so that the buttons change colors when a user clicks on them.
  - If a user clicks on a button with an incorrect answer, the button should turn red and text should appear beneath the question that says “Incorrect”.
  - If a user clicks on a button with the correct answer, the button should turn green and text should appear beneath the question that says “Correct!”.
- In index.html, add beneath “Part 2” a text-based free response question of your choosing with HTML.
  - You should use an h3 heading for the text of your question.
  - You should use an input field to let the user type a response.
  - You should use a button to let the user confirm their answer.
- Using JavaScript, add logic so that the text field changes color when a user confirms their answer.
  - If the user types an incorrect answer and presses the confirmation button, the text field should turn red and text should appear beneath the question that says “Incorrect”.
  - If the user types the correct answer and presses the confirmation button, the input field should turn green and text should appear beneath the question that says “Correct!”.

## Some Screenshots from the Program 
![image](https://user-images.githubusercontent.com/95561298/180748135-11817d42-d383-4640-824a-85a6b93ec868.png)

![image](https://user-images.githubusercontent.com/95561298/180748337-3a30be24-e61c-41b4-80e1-1c955976adea.png)

# Week 9: Flask (Finance)
Finance is a web application that is created for CS50 Problem Set 9. The web application enables the users to invest in stocks. The web application has 7 functionalities, which are register, login/logout, deposit, quote, buy, sell, and history. Firstly, the user is able to register for an account and log in to the web application. The user can then deposit funds, check stock prices, buy stocks, sell stocks, and check transaction history. All the id/password, portfolio, and transaction history of the users are stored in a database by using SQLite. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/95561298/181178624-780a6853-e198-426f-87c5-95b508b82771.gif" width="80%" height="80%"/>
<p>

## Tech Stack Used
- Frontend: HTML, CSS, JavaScript 
- Backend: Python, SQLite
- Frameworks: Flask, Bootstrap
- API: IEX (for stocks' real-time price)

## Information about Finance 
Finance has 7 functionalities:
1) **Register**: The user is required to register for an account with an id and password before they can invest in stocks. 
2) **Login / Logout**: The user is able to log in and log out from the web application. 
3) **Deposit**: The user is able to deposit extra funds into the account for them to invest in stocks. 
4) **Quote**: The user is able to check for the real-time prices of a particular stock based on the stock's symbol. 
5) **Buy**: The user is able to buy a particular stock based on the stock's symbol  
6) **Sell**: The user is able to sell a particular stock that they have purchased. 
7) **History**: The user is able to check the transaction history such as buying or selling stock. 

# Final Project (Food Wheel) 
Not sure what to eat for dinner tonight? Always worried about what to eat after studying or working? No worries, Food Wheel is here to help you to solve the problem! Food Wheel is a web application that helps people to decide what to eat! The users can add all their favorite foods onto the food wheel and let the food wheel decides the dinner for them. Other than that, the users can also remove their favorite foods from the food wheel. In other words, users are allowed to customize their own food wheels by adding and removing their favorite foods on the food wheel. The food wheel will expand and shrink depending on the number of foods on the food wheel.

## Tech Stack Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python, SQLite
- Frameworks: Flask, Bootstrap

## Functionalities
In this web application, it consists of 4 sections with different functionalities:
1) ``Wheel``: The food wheel that consists of all the user's favorite foods to pick from.
2) ``Add``: The food will be added to the food wheel.
3) ``Remove``: The food will be removed from the food wheel.
4) ``History``: The history that keeps track of all the foods added and removed from the wheel.

Visit the video demo here!: https://www.youtube.com/watch?v=r1k6uTqmVLE

That's all! This was CS50! 



