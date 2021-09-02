# conga_office
Python library thought to active "conga-office" in order to appear online to your employer while grabbing a coffee or  having creativity sessions.

# Installation
You can install the package using pip
`pip install conga-office`

# Usage
## Moving mouse's pointer
Import the module

`from conga_office.tools import activate_conga_office`

Then run any of the available modes:
* Move mouse pointer from right to left for 10 seconds: `activate_conga_office(duration=10, pattern='linear')` or `activate_conga_office(duration=10)` 
* Move mouse pointer in diamond shape for 20 seconds: `activate_conga_office(duration=20, pattern='diamond')`
* Move mouse pointer in circles for 5 seconds: `activate_conga_office(duration=5, pattern='circle')`
* Move mouse pointer in randomly for 10 seconds: `activate_conga_office(duration=10, pattern='random')`

To move faster or slower set `speed='turbo'` or `speed='slow'` respectively. E.G.
`activate_conga_office(duration=10, pattern='diamond', speed='turbo')`

## Sending corporate jargon via Teams
This is a function only available for Windows 10 users who use Microsoft Teams. If you want yo send 
10 messages at intervals of 2 seconds (it is recommended at least 2 seconds of interval between messages)
to a contact whose id is `a_name.a_surname` then apply the following code:

```
from conga_office.tools import send_bs_via_teams
send_bs_via_teams(
  contact_id = 'a_name.a_username', 
  number_of_bs_statements = 5, 
  intervals_in_secs=2)
```

# Future endeavors
* Create flamboyant Power Point presentations.
* Build internal colloquial bs generator.
