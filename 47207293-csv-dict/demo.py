'''
https://stackoverflow.com/questions/47207293/csv-creating-a-login-system-python-not-properly-reading-from-csv-file
'''

# Get user and password from csv file
with open('data.csv') as f:
    content_lines = (x.strip().split(',') for x in f) # filer lines with enough data
    user_pass = {user: password for user, password in
                 [content[:2] for content in content_lines
                  if len(content) >= 2]
                 }

import getpass

logged_in = False
while not logged_in:

    user = raw_input('Username:')
    password = getpass.getpass('Password:')

    logged_in = user_pass.get(user, None) == password

print 'logged in \o/'
