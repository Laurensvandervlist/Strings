# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1 + ' ' + str(goal_0) + ',' + ' ' + scorer2 + ' ' + str(goal_1)
print(scorers)
report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
print(report)

player = 'Ronald Koeman'
first_name = player[:(player.find(' '))]
print(first_name)

last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)

name_short = (player[0]) + '. ' + (player[player.find(' ')+1:])
print(name_short)

first_name_len = len(player[:(player.find(' ')-1)])
chant = (first_name + '! ') * (first_name_len) + first_name + '!'
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)