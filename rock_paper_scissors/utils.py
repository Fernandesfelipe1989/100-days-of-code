options = ('rock', 'paper', 'scissors')
conditions = {
    'paper': {
        'win': 'rock',
        'lose': 'scissors',
    },
    'rock': {
        'win': 'scissors',
        'lose': 'paper',
    },
    'scissors': {
        'win': 'paper',
        'lose': 'rock',
    }
}
images_options = {
    'paper': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    'rock':  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    'scissors': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
}
