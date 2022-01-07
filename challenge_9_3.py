import csv

film_list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

# simple_film_list = ["Top Gun", "Risky Business", "Minority Report"]


with open("test4.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in range (3):
        w.writerow(film_list[i])

