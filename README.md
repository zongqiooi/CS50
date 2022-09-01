# CS50's Introduction to Computer Science
CS50 is an introductory course to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web programming. Languages include C, Python, and SQL plus HTML, CSS, and JavaScript. Problem sets inspired by the arts, humanities, social sciences, and sciences. Course culminates in a final project. Designed for concentrators and non-concentrators alike, with or without prior programming experience. Two thirds of CS50 students have never taken CS before. Among the overarching goals of this course are to inspire students to explore unfamiliar waters, without fear of failure, create an intensive, shared experience, accessible to all students, and build community among students.

This CS50 repository contains all the labs and problem sets that I have submitted for all the coursework. Below summarizes some of the projects for the labs and problem sets. 

# Week 1: Scratch (Wizard Pong) 
Wizard Pong is a game that is created for CS50 Problem Set 0. The game is created by using Scratch. The users can press up and down keys to control the broomstick in the game. Score 8 points to win. 

## Some Screenshots from the Game 
<img src="https://user-images.githubusercontent.com/95561298/178139018-6e0da0f1-185c-4887-8dde-b528f854dd0e.png" height="400" width="550">
<img src="https://user-images.githubusercontent.com/95561298/178139025-4b98da6e-e2bc-4b92-9660-f7cc49a3e08e.png" height="400" width="550">

## Link
Visit this Scratch link to play the game!: https://scratch.mit.edu/projects/711721445/

# Week 2: C (Credit)
Credit is a program that is created for CS50 Problem Set 1. The program is used to check the types of credit cards and it is created by using C. The users will be prompted to enter a credit card number in integers. After that, the program will be classified whether the credit card number is AMEX (American Express), MASTERCARD, VISA, or INVALID. The validity of the Visa card is checked by using Luhn's Algorithm. 

## Information about Credit Cards
A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a quadrillion.)

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.

## Some Screenshots from the Program 
![cs50 pset 1 ss1](https://user-images.githubusercontent.com/95561298/178524440-8af3579e-5b1d-4d44-a48a-7468b3a8eb79.png)

# Week 3: Algorithms (Substitution)
Substitution is a program that is created for CS50 Problem Set 2. The program is used to encrypt plaintext into ciphertext and it is created by using C. The users have to run the C file with an extra command line argument known as "key", in the format of "./substitution key". Then, the users will be prompted to enter plaintext in strings. After that, the plaintext will be encrypted into ciphertext based on the "key" entered in the command line argument.

## Information about Substitution (Encryption)
In a substitution cipher, we “encrypt” (i.e., conceal in a reversible way) a message by replacing every letter with another letter. To do so, we use a key: in this case, a mapping of each of the letters of the alphabet to the letter it should correspond to when we encrypt it. To “decrypt” the message, the receiver of the message would need to know the key, so that they can reverse the process: translating the encrypt text (generally called ciphertext) back into the original message (generally called plaintext).

A key, for example, might be the string NQXPOMAFTRHLZGECYJIUWSKDVB. This 26-character key means that A (the first letter of the alphabet) should be converted into N (the first character of the key), B (the second letter of the alphabet) should be converted into Q (the second character of the key), and so forth.

A message like HELLO, then, would be encrypted as FOLLE, replacing each of the letters according to the mapping determined by the key.

## Some Screenshots from the Program 
![cs50 pset 2 ss1](https://user-images.githubusercontent.com/95561298/178780713-7ed243c2-bde3-45c6-ba51-61721e1e5970.png)


