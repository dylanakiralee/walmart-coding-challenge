# Walmart Coding Challenge

Movie Theater Seating Challenge (2020) for Walmart Labs.

### Assumptions

- After doing some research I found that the most desirable seats were in the center of the rows that are 1/2 to 2/3 away from the screen. Some articles said only that 2/3 away was most desirable.
    - As a result, I gave 2/3 the highest desirability, followed by all the rows down to 1/2, and then alternating higher and lower until I ran out of rows.
- I gave priority to the first reservations in the input file, evaluating each request one by one.
- I assumed that the safety restrictions don't apply within parties, so all members of a party can sit next to one another.

### Instructions for Executing

1. Navigate to the directory where theater.py is located.
2. Run the command `python theater.py input.txt` where input.txt contains the reservation requests.
3. Check the file output.txt for the seating assignments.

### Improvements

- Create a more robust algorithm that considers multiple requests when making assignments, instead of just the current one.
- 