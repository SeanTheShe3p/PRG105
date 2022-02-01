#  Guacamole Recipe
#  Link: https://downshiftology.com/wprm_print/33907
#  servings: 4
#  Ingredients:
#  3 Avocados
#  1/2 small onion
#  2 Roma Tomatoes
#  3 Tablespoons chopped cilantro
#  1 Jalapeno
#  1 lime
#  1/2 teaspoon salt
#
#
avo = float(3 / 4)
oni = float((1 / 2) / 4)
tom = float(2 / 4)
cil = float(3 / 4)
jal = float(1 / 4)
lim = float(1 / 4)
sal = float(1 / 2)
serving = int(input('How many servings? '))
avo = avo * serving
oni = oni * serving
tom = tom * serving
cil = cil * serving
jal = jal * serving
lim = lim * serving
sal = sal * serving
avo = float(format(avo, '.1f'))
oni = float(format(oni, '.1f'))
tom = float(format(tom, '.1f'))
cil = float(format(cil, '.1f'))
jal = float(format(jal, '.1f'))
lim = float(format(lim, '.1f'))
sal = float(format(sal, '.1f'))
print('Guacamole Recipe')
print('servings: ' + str(serving))
if avo <= 1:
    print(' • ' + str(avo) + ' ripe avocado')
else:
    print(' • ' + str(avo) + ' ripe avocados')
if oni <= 1:
    print(' • ' + str(oni) + ' small diced onion')
else:
    print(' • ' + str(oni) + ' small diced onions')
if tom <= 1:
    print(' • ' + str(tom) + ' Roma tomato')
else:
    print(' • ' + str(tom) + ' roma tomatoes')
if cil <= 1:
    print(' • ' + str(cil) + ' tablespoon chopped cilantro')
else:
    print(' • ' + str(cil) + ' tablespoons chopped cilantro')
if jal <= 1:
    print(' • ' + str(jal) + ' seeded jalapeno')
else:
    print(' • ' + str(jal) + ' seeded jalapenos')
if lim <= 1:
    print(' • ' + str(lim) + ' lime')
else:
    print(' • ' + str(lim) + ' limes')
if sal <= 1:
    print(' • ' + str(sal) + ' teaspoon salt')
else:
    print(' • ' + str(sal) + ' teaspoon salt')
