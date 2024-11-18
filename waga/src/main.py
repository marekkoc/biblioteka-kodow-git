"""
Project: Daily weight analysis.

The main script.

Copyright: Marek

Created: 2024.11.17
Modified: 2024.11.18
"""
from years import Y24
from years import Y23
from years import Y22
from years import Y21
from years import Y20
from years import Y19
from years import Y18
from years import Y17



print()
years = [
Y24(),
Y23(),
Y22(),
Y21(),
]

for y in years:
    print(y.sheet.to_numpy().mean())

