media_team=[
    {
        'Age':20,
        'Name': 'Michael',
        'expertise': 'Anchor'
    },
    {
        'Age':22,
        'Name': 'John', 
        'expertise': 'Camera'
    },
    {
        'Age':21,
        'Name': 'Sarah',
        'expertise': 'Editing'
    },
    {
        'Age':23,
        'Name': 'Tabitha',
        'expertise': 'Sound'
    }

]
def confirm_expertise(team, expertise):
    for member in team:
        if member['expertise'] == expertise:
            return True
    return False