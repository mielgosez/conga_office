# conga_office
Python library thought to active "conga-office" in order to appear online to your employer while grabbing a coffee or  having creativity sessions.

# Installation
`pip install conga-office`

# Usage
Import the module

`from conga_office.tools import activate_conga_office`

Then run any of the available modes:
* Move mouse pointer from right to left for 10 seconds: `activate_conga_office(duration=10, pattern='linear')` or `activate_conga_office(duration=10)` 
* Move mouse pointer in diamond shape for 20 seconds: `activate_conga_office(duration=20, pattern='diamond')`

To move faster or slower set `speed='turbo'` or `speed='slow'` respectively. E.G.
`activate_conga_office(duration=10, pattern='diamond', speed='turbo')`

# Future endeavors
* Move mouse in circles.
* Move mouse randomly.
* Corporate jargon.