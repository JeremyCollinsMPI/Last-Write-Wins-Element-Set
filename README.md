# Last-Write-Wins-Element-Set
The following is a description of the Last Write Wins (LWW) set from Wikipedia (https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#LWW-Element-Set_(Last-Write-Wins-Element-Set)):

'LWW-Element-Set is similar to 2P-Set in that it consists of an "add set" and a "remove set", with a timestamp for each element. Elements are added to an LWW-Element-Set by inserting the element into the add set, with a timestamp. Elements are removed from the LWW-Element-Set by being added to the remove set, again with a timestamp. An element is a member of the LWW-Element-Set if it is in the add set, and either not in the remove set, or in the remove set but with an earlier timestamp than the latest timestamp in the add set. Merging two replicas of the LWW-Element-Set consists of taking the union of the add sets and the union of the remove sets. When timestamps are equal, the "bias" of the LWW-Element-Set comes into play. A LWW-Element-Set can be biased towards adds or removals. The advantage of LWW-Element-Set over 2P-Set is that, unlike 2P-Set, LWW-Element-Set allows an element to be reinserted after having been removed.'

This repository implements this set as a python class LWW, with the following usage:

## Example usage

from LWW import LWW

lww = LWW()  #initiate the set.  options include bias='add' for when the timestamp of the last add and the last removal are    the same (which chooses the last add), and the precision of the timestamp, time_precision, with a default of seven decimal places.

lww.add('element1')  #add an element

lww.remove('element1')  #remove the element

lww.remove('element2')  #it is also possible to remove an element that has not been added

lww.add('element1')  #add an element that has previously been deleted

lww.update()  #update the current value of the set, which is {'element1'}

print(lww.set) #print the current value of the set

lww2 = LWW()  #initiate a second set

lww2.remove('element1')

lww2.add('element2')

lww.merge_with(lww2) #merge both LWW's

lww.update()   #update the current value of the set, which is {'element2'}

lww.exists('element2')    #a method for checking whether an element exists in the set, without needing to call update()

## Attributes

.add_set: a dictionary of elements to be added, with timestamps

.remove_set: a dictionary of elements to be removed, with timestamps

.set: a set of the current members of the LWW set after update() is called

.bias: can be set 'add' to make adds prioritised over removes when they occur with the same timestamp, otherwise removes are prioritised

.time_precision: the number of decimal places of the timestamps (default 7)

## Methods

init(bias='add', time_precision=7): the bias is set to 'add' by default, but set to any other value (e.g. 'remove') will make the LWW biased to the remove timestamp.  time_precision sets the attribute .time_precision.

add(object): adds the object to the add_set with the current timestamp

remove(object): adds the object to the remove_set with the current timestamp

update(): takes the remove_set and add_set and updates the value of set

exists(object): uses the add_set and remove_set to return True if an object is in the element set, False otherwise

merge_with(LWW): finds the latest add timestamp for each element in the LWW and the LWW to be merged with, and the latest remove timestamp for each element.  a new add_set and remove_set are produced for the first LWW, with the latest add and remove timestamps.

## Tests

test1: adding and removing elements in a LWW

test2: merging two LWW's which have different elements

test3: merging two LWW's, one which has removed an element after it has been added to the other

test4: adding and removing an element simultaneously with a bias of adding

test5: adding and removing an element simultaneously with a bias of removing



