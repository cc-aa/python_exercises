__author__ = 'Red'

gasgals = float(raw_input("How much gasoline : "))

lit = gasgals * 3.7854
barrels = gasgals/19.5
co2produced = gasgals * 20
ethanolreqd = (gasgals * 115000)/75700
price = gasgals * 4.0

print "You entered %f \n which is %.2f literes and \n required %.2f barrels to produce \n " \
      "which produces %.2f lbs of CO2 \n and costs %.2f dollars \n Equivalent Ethanaol required would be %.2f"\
      %(gasgals, lit, barrels, co2produced, price, ethanolreqd)

