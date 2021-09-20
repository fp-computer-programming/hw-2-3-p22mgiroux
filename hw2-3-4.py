# Author: MOG 9/17/21

# Population on 9/23/20
starting_population = 331832432
# Net gain of one person every 25 seconds
one_person = 25

day_in_seconds = 60 * 60 * 24
number_of_days = 365

final_population = starting_population + (day_in_seconds * number_of_days // one_person)

print("The final population {} days after a population of {}, is {}".format(number_of_days, starting_population,final_population))