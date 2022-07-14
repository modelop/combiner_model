# modelop.slot.0: in-use
# modelop.slot.1: in-use
# modelop.slot.2: in-use
# modelop.slot.4: in-use

RECORD = [[], [], []]

def begin():
  # Do stuff here

# modelop.score
def action(data, slot_number):
   global RECORD
   
   if !RECORD[0].empty() and !RECORD[1].empty() and !RECORD[2].epmty():
      yield RECORD[0].pop().update(RECORD[1].pop()).update(RECORD[2].pop())
   else:
      yield None
      
