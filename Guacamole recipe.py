#  Recipe for guacamole
#  link = https://www.theendlessmeal.com/wprm_print/60146
#  Ingredients:
#  1 cloves roasted garlic
#  3 ripe avocados
#  1 lime
#  salt to taste
#
#  pseudocode
#  Data:
#  enter variables for Garlic(gar), Avocados(avo), and lime(Lim)
#  input number of servings
#  Processing:
#  Change variables gar, avo, and lim to be multiplied by servings
#  convert string to int and format calculated amounts
#  print recipe, format as string, add string salt to taste, directions
#
avo = 3
gar = 1
lim = 1
serv = int(input('how many servings? '))
avo = format(avo * serv, '.1f')
gar = format(gar * serv, '.1f')
lim = format(lim * serv, '.1f')
print(str('You need ' + avo + ' avocados, ' + gar + ' cloves of garlic, and ' + lim + ' limes plus salt to taste'))
