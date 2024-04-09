-- Keep a log of any SQL queries you execute as you solve the mystery.

--Given Information: Date of theft: 28.07, street: Humphrey Street
--Information to find: Who is the thief?, Where does the thief escaped to?, Who was his accompliance who helped him get out of town?
--Conclusion: Destination of escape: New York City, Thief: Bruce, Accompliance: Robin


--1.Get all missing and maybe useful information of the table to complete the date, look for clues, and for having the id of the crime report maybe for later -> Date: 28.07.2021 / id of description: 295
SELECT description, year, id
FROM crime_scene_reports
WHERE month = '7'
AND day = '28'
AND street = 'Humphrey Street';

--Conclusion: ->time: 10:15 am, ->location:Humphrey Street bakery, ->witnesses: three, present at the bakery when theft took place
--->interviews: on same day (28.07.2021), each witness mentions bakery in transcriptions

--2.Look at the interviews to get the three witnesses and more information
SELECT transcript, name
FROM interviews
WHERE year = '2021'
AND month = '7'
AND day = '28'
AND transcript LIKE '%bakery%';

--Conclusion: Ruth: Thief left within time range 10:15 - 10:25, Eugene: Saw the thief earlier at ATM Leggett Street withdrawing some money, Raymond: As thief was leaving bakery call for less than minute.
--Thief said the person on the other end should purchase fligth tickets for earliest flight tomorrow. Used pronoun "they" so both taking the flight?

--2.1.Look for the name of the people who left between 10:15 - 10:25
SELECT name
FROM people
    JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = '2021'
AND month = '7'
AND day = '28'
AND hour = '10'
AND minute BETWEEN '15' AND '25'
AND activity = 'exit'
ORDER BY name ASC;

--Conclusion: Names of People: Barry, Bruce, Diana, Iman, Kelsey, Luca, Sofia, Vanessa

--2.2.Look for matching names at the ATM Leggett Street
SELECT name
FROM people
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE atm_transactions.year = '2021'
AND atm_transactions.month = '7'
AND atm_transactions.day = '28'
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street'
AND minute BETWEEN '15' AND '25'
AND activity = 'exit'
ORDER BY name ASC;

--Conclusion: Names of People left 10:15-10:25 and withdrawed on Leggett Street same day: Bruce, Diana, Iman, Luca

--2.3.Look for earliest flight on next day and the destination
SELECT destination_airport_id, hour, minute
FROM flights
WHERE year = '2021'
AND month = '7'
AND day = '29'
ORDER BY hour ASC, minute ASC
LIMIT 1;

--Conclusion: Destination Airport ID : 4

--2.4.Find destination of the escape
SELECT city
FROM airports
WHERE id = '4';

--Conclusion: New York City

------------------------------------------------------------------------Destination of escape: New York City ---------------------------------------------------------------------------------

--3.1.Get the fligth ID from the taken flight and the passengers and their seats (assumption thief and accompliance sitting next to each other -> Luca=Thief, Kelsey=accompliance)
SELECT flight_id, name, seat
FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    JOIN flights ON flights.id = passengers.flight_id
WHERE year = '2021'
AND month = '7'
AND day = '29'
AND hour = '8'
AND minute = '20'
AND destination_airport_id = '4'
ORDER BY name ASC;

--Conclusion: List of names: Bruce, Luca. assumption Luca and=Thief, Kelsey=accompliance has to be prooved

--3.2.Get phone numbers from Bruce and Kelsey
SELECT name, phone_number
FROM people
WHERE name IN ('Luca','Kelsey');

--Conclusion: Luca: (389) 555-5198, Kelsey: (499) 555-9472

--3.3.Try proof of call between Luca and Kelsey
SELECT caller, receiver
FROM phone_calls
WHERE year = '2021'
AND month = '7'
AND day = '28'
AND duration < 60
ORDER BY caller ASC;

--Conclusion: Proof failed. No calls from Luca at the day of the crime. -> Bruce has to be the thief

----------------------------------------------------------------------------------------Thief:Bruce--------------------------------------------------------------------------------------

--4.1.Get phone_number from Bruce
SELECT phone_number
FROM people
WHERE name = 'Bruce';

--Conclusion: Bruce: (367) 555-5533

--4.2.Look for the accompliance/receiver of a call from Bruce at the given day with duration under 60sec
SELECT receiver
FROM phone_calls
WHERE caller = '(367) 555-5533'
AND year = '2021'
AND month = '7'
AND day = '28'
AND duration < 60
ORDER BY caller ASC;

--Conclusion: receiver: (375) 555-8161

--4.3.Get name of accompliance
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';

--Receiver of call: Robin. Robin has to be the accompliance

--------------------------------------------------------------------------------Accompliance:Robin---------------------------------------------------------------------------------

--With data of the buyers from flight tickets there could be grasped more evidence against Bruce and Robin.
--Use of the pronoun "they" not vaild -> reasonable because testimony or intention from thief
--Would have been possible to search for the phone_numbers of Bruce and Luca after 3.1. and compare both of them to the calls at the day of the crime at 3.3.
