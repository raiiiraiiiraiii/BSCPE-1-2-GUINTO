import pyfiglet

name = input("What is you name? ")
dream_job = input("What is your dream job? ")

name_art = pyfiglet.figlet_format("Hello " + name, font="banner")

dream_job_art = pyfiglet.figlet_format("Your Dream Job is: " + dream_job, font="banner")

print("\033[91m{}\033[00m".format(name_art))
print("\033[91m{}\033[00m".format(dream_job_art))