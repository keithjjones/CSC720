# Here are all the alphanumeric characters:
alphanumbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9']

# Create our transition table
transition_table = dict()
transition_table['q0'] = dict()
transition_table['q0']['alphanumeric'] = 'q1'
transition_table['q0']['@'] = None
transition_table['q0']['.'] = None
transition_table['q1'] = dict()
transition_table['q1']['alphanumeric'] = 'q2'
transition_table['q1']['@'] = 'q3'
transition_table['q1']['.'] = None
transition_table['q2'] = dict()
transition_table['q2']['alphanumeric'] = 'q2'
transition_table['q2']['@'] = 'q3'
transition_table['q2']['.'] = None
transition_table['q3'] = dict()
transition_table['q3']['alphanumeric'] = 'q4'
transition_table['q3']['@'] = None
transition_table['q3']['.'] = None
transition_table['q4'] = dict()
transition_table['q4']['alphanumeric'] = 'q5'
transition_table['q4']['@'] = None
transition_table['q4']['.'] = 'q6'
transition_table['q5'] = dict()
transition_table['q5']['alphanumeric'] = 'q5'
transition_table['q5']['@'] = None
transition_table['q5']['.'] = 'q6'
transition_table['q6'] = dict()
transition_table['q6']['alphanumeric'] = 'q7'
transition_table['q6']['@'] = None
transition_table['q6']['.'] = None
transition_table['q7'] = dict()
transition_table['q7']['alphanumeric'] = 'q8'
transition_table['q7']['@'] = None
transition_table['q7']['.'] = 'q9'
transition_table['q8'] = dict()
transition_table['q8']['alphanumeric'] = 'q10'
transition_table['q8']['@'] = None
transition_table['q8']['.'] = 'q9'
transition_table['q9'] = dict()
transition_table['q9']['alphanumeric'] = 'q7'
transition_table['q9']['@'] = None
transition_table['q9']['.'] = None
transition_table['q10'] = dict()
transition_table['q10']['alphanumeric'] = 'q11'
transition_table['q10']['@'] = None
transition_table['q10']['.'] = 'q9'
transition_table['q11'] = dict()
transition_table['q11']['alphanumeric'] = 'q11'
transition_table['q11']['@'] = None
transition_table['q11']['.'] = 'q9'

# Our accept states:
accept_states = ['q8', 'q10']

# Out initial state:
initial_state = 'q0'

# Set our current state at the beginning
current_state = initial_state

# Get our test string
test_string = input('Give me a string to check: ')

# Iterate through each character and do the tests
for character in test_string:
    if character.lower() in alphanumbers:
        character = 'alphanumeric'
    elif character != '@' and character != '.':
        print("You entered a character not in our alphabet!")
        exit()

    # Go to the next state...
    current_state = transition_table[current_state][character]

    # If we don't have a valid state...
    if current_state is None:
        print("You fell out of the DFA.  This string is not accepted.")
        exit()

# Test to see if our final state is in the accept states...
if current_state in accept_states:
    print("Your string was accepted.")
else:
    print("Your string was NOT accepted.")

