-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Query the description took place on Humphrey Street, July 28, 2021.
SELECT description
  FROM crime_scene_reports
 WHERE month = 7
   AND day = 28
   AND street = "Humphrey Street";
-- There are three witnesses

-- Query the transcript given by the three witnesses in the interview
SELECT name, transcript
  FROM interviews
 WHERE month = 7
   AND day = 28
   AND year = 2021;
-- The name of hree witnesses = Ruth, Eugene, Raymond

-- 1) Query the data based on Ruth's transcript
SELECT id, hour, minute, activity, license_plate
  FROM bakery_security_logs
 WHERE month = 7
   AND day = 28
   AND year = 2021
   AND hour = 10
   AND minute BETWEEN 15 AND 25;
-- Total suspected license_plate = 8

-- Identify the suspected people based on license_plate
SELECT *
  FROM people
 WHERE license_plate IN
       (SELECT license_plate
          FROM bakery_security_logs
         WHERE month = 7
           AND day = 28
           AND year = 2021
           AND hour = 10
           AND minute BETWEEN 15 AND 25);
-- Current suspected people based on license plate = Vanessa, Barry, Iman, Sofia, Luca, Diana, Kelsey, Bruce

-- 2) Query the data based on Eugene's transcript
SELECT *
  FROM atm_transactions
 WHERE atm_location = "Leggett Street"
   AND month = 7
   AND day = 28
   AND year = 2021
   AND transaction_type = "withdraw";
-- Total people withdrew money = 8

-- Identify the suspected people based on withdrawal transactions
SELECT *
  FROM people
 WHERE id IN
       (SELECT person_id
          FROM bank_accounts
         WHERE account_number IN
               (SELECT account_number
                  FROM atm_transactions
                 WHERE atm_location = "Leggett Street"
                   AND month = 7
                   AND day = 28
                   AND year = 2021
                   AND transaction_type = "withdraw"));
-- Current suspected people based on withdrawal transactions = Kenny, Iman, Benista, Taylor, Brooke, Luca, Diana, Bruce
-- Similar suspected people based on the transcripts by Ruth and Eugene = Iman, Luca, Diana, Bruce

-- 3) Query the data based on Raymond's transcript
SELECT *
  FROM phone_calls
 WHERE duration < 60
   AND month = 7
   AND day = 28
   AND year = 2021;
-- Total people called others = 9

-- Identify the suspected caller based on phone calls
SELECT *
  FROM people
 WHERE phone_number IN
       (SELECT caller
          FROM phone_calls
         WHERE duration < 60
           AND month = 7
           AND day = 28
           AND year = 2021);
-- Current suspected people based on phone calls = Kenny, Sofia, Benista, Taylor, Diana, Kelsey, Bruce, Carina
-- Similar suspected people based on the transcripts by Ruth, Eugene, and Raymond = Diana, Bruce

-- Identify the suspected receiver based on phone calls
SELECT *
  FROM people
 WHERE phone_number IN
       (SELECT receiver
          FROM phone_calls
         WHERE duration < 60
           AND month = 7
           AND day = 28
           AND year = 2021
           AND (caller = "(770) 555-1861" OR caller = "(367) 555-5533"));
-- Suspected accomplice = Philip (with Diana), Robin (with Bruce)

-- Identify the ID of the earliest flight
SELECT *
  FROM flights
 WHERE month = 7
   AND day = 29
   AND year = 2021;
-- ID of earliest flight = 36

-- 1) Final solution: The THIEF is = Bruce
-- Bruce is identified as the thief by matching the passport number based on the earliest flight on the next day
SELECT name
  FROM people
 WHERE passport_number IN
       (SELECT passport_number
          FROM passengers
         WHERE flight_id = 36)
   AND (name = "Diana" OR name = "Philip" OR name = "Bruce" OR name = "Robin");

-- 2) Final solution: The city the thief ESCAPED TO = New York City
-- New York City is identified as the city the thief escaped to by matching the destination airport ID based on the earliest flight on the next day
SELECT city
  FROM airports
 WHERE id IN
       (SELECT destination_airport_id
          FROM flights
         WHERE id = 36);

-- 3) Final solutoin: The ACCOMPLICE is = Robin
-- Robin is identified as the accomplice by matching the phone call where Bruce is the caller
SELECT name
  FROM people
 WHERE phone_number IN
       (SELECT receiver
          FROM phone_calls
         WHERE duration < 60
           AND month = 7
           AND day = 28
           AND year = 2021
           AND caller = "(367) 555-5533");