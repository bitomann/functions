# Define four Python functions named run, swing, slide, and hide_and_seek. 
# Each function should take varying number of children's names as the argument.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Ariel", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(name):
    print(f"{name} can't run?")

def swing(name):
    print(f"{name} took a swing at me!")

def slide(name):
    print(f"{name} has a slide.")

def hide_and_seek(name):
    print(f"{name} got lost playing hide and seek...")


 # Loop through all the kids and print that the child performed the activity.

for kid in running_kids:
     run(kid)
for kid in swinging_kids:
     swing(kid)
for kid in sliding_kids:
     slide(kid)
for kid in hiding_kids:
     hide_and_seek(kid)
