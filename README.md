# Last-Write-Wins-Element-Set
The following is a description of the Last Write Wins (LWW) set from Wikipedia (https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#LWW-Element-Set_(Last-Write-Wins-Element-Set)):

'LWW-Element-Set is similar to 2P-Set in that it consists of an "add set" and a "remove set", with a timestamp for each element. Elements are added to an LWW-Element-Set by inserting the element into the add set, with a timestamp. Elements are removed from the LWW-Element-Set by being added to the remove set, again with a timestamp. An element is a member of the LWW-Element-Set if it is in the add set, and either not in the remove set, or in the remove set but with an earlier timestamp than the latest timestamp in the add set. Merging two replicas of the LWW-Element-Set consists of taking the union of the add sets and the union of the remove sets. When timestamps are equal, the "bias" of the LWW-Element-Set comes into play. A LWW-Element-Set can be biased towards adds or removals. The advantage of LWW-Element-Set over 2P-Set is that, unlike 2P-Set, LWW-Element-Set allows an element to be reinserted after having been removed.'

This repository implements this set as a python class LWW, with the following usage:

from LWW import LWW

lww = LWW()  #initiate the set.  options include bias='add' for when the timestamp of the last add and the last removal are    the same (which chooses the last add), and the precision of the timestamp, time_precision, with a default of seven decimal places.

lww.add('element1')  #add an element
lww.remove('element1')  #remove the element
lww.remove('element2')  #it is also possible to remove an element that has not been added
lww.add('element1')  #add an element that has previously been deleted

lww.update()  #calculate the current value of the set, which is ['element1']

lww2 = LWW()  #initiate a second set
lww2.remove('element1')
lww2.add('element2')

lww.merge_with(lww2) #merge both LWW's
lww.update()   #calculate the current value of the set, whiCh is ['element2']

