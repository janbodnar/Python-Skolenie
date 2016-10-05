#!/usr/bin/python3

# teams.py

teams = { 
      0: ("Ajax Amsterdam", "Inter Milano"),
      1: ("Real Madrid", "AC Milano"),
      2: ("Dortmund", "Sparta Praha")
}

results = ("2:3", "3:3", "2:1")


for i in teams:
    
   line = teams[i][0].ljust(16) + "-".ljust(5) + teams[i][1].ljust(16) + results[i].ljust(3)
   print(line)
