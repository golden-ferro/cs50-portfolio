-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
--'July 28, 2024  Humphrey Street 10:15am bakery, three witnesses, Littering took place at 16:36'
SELECT transcript FROM interviews WHERE year = 2024 AND month = 7 AND day >= 28;
--'within ten minutes, get into a car in the bakery
--Emma bakery, this morning saw the thief there withdrawing some money at the atm
--earliest flight out of Fiftyville tomorrow'
SELECT activity, license_plat FROM bakery_security_logs WHERE year = 2024 AND month = 7 AND day = 28 AND hour = 10;
--5P2BI95
--5P2BI95
--94KL13X
--6P58WS2
--4328GD8
--G412CB7
--L93JTIZ
--322W7JE
--0NTHK55
SELECT name, phone_number, passport_number, license_plate
FROM people
WHERE license_plate IN (
'5P2BI95',
'5P2BI95',
'94KL13X',
'6P58WS2',
'4328GD8',
'G412CB7',
'L93JTIZ',
'322W7JE',
'0NTHK55'
);
--+---------+----------------+-----------------+---------------+
--|  name   |  phone_number  | passport_number | license_plate |
--+---------+----------------+-----------------+---------------+
--| Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
--| Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
--| Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
--| Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
--| Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
--| Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
--| Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
--+---------+----------------+-----------------+---------------+

SELECT caller, receiver
FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
  AND duration < 60;
+----------------+----------------+
|     caller     |    receiver    |
+----------------+----------------+
| (130) 555-0289 | (996) 555-8899 |
| (499) 555-9472 | (892) 555-8872 |
| (367) 555-5533 | (375) 555-8161 |
| (499) 555-9472 | (717) 555-1342 |
| (286) 555-6063 | (676) 555-6554 |
| (770) 555-1861 | (725) 555-3243 |
| (031) 555-6622 | (910) 555-3251 |
| (826) 555-1652 | (066) 555-9701 |
| (338) 555-6650 | (704) 555-2131 |
+----------------+----------------+
-- Sofia, Diana, Kelsey e Bruce
SELECT passport_number FROM people WHERE name IN ('Sofia', 'Diana', 'Kelsey', 'Bruce');
+-----------------+
| passport_number |
+-----------------+
| 1695452385      |
| 3592750733      |
| 8294398571      |
| 5773159633      |
+-----------------+
SELECT origin_airport_id, destination_airport_id, hour, passport_number
FROM flights
JOIN passengers ON flights.id = passengers.flight_id
WHERE year = 2024 AND month = 7 AND day = 29
  AND passport_number IN ('1695452385', '3592750733', '8294398571', '5773159633') ;
+-------------------+------------------------+------+-----------------+
| origin_airport_id | destination_airport_id | hour | passport_number |
+-------------------+------------------------+------+-----------------+
| 8                 | 6                      | 16   | 3592750733      |
| 8                 | 4                      | 8    | 1695452385      |
| 8                 | 4                      | 8    | 5773159633      |
| 8                 | 4                      | 8    | 8294398571      |
+-------------------+------------------------+------+-----------------+
-- Sofia, Kelsey, Bruce
SELECT name
FROM people
WHERE id IN (
  SELECT person_id
  FROM bank_accounts
  WHERE account_number IN (
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2024 AND month = 7 AND day = 28
      AND atm_location = 'Leggett Street'
      AND transaction_type = 'withdraw'
  )
);
+---------+
|  name   |
+---------+
| Kenny   |
| Iman    |
| Benista |
| Taylor  |
| Brooke  |
| Luca    |
| Diana   |
| Bruce   |
+---------+
--Bruce 
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';
-- Robin
SELECT city FROM airports WHERE id = 4;
-- New York City
