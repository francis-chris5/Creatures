# Creatures
A series of plugins for Blender for additional (Object->Add->Mesh) buttons to insert starter shapes for a number of animals: sized and proportioned accurately so that artists can focus more time on adding details.
I wanted these starter shapes and figured I'd go ahead and share them with others. This is still a work in progress so more creatures will be forthcoming (and eventually/hopefully some riggings ready to go with them) along with improvements/updates to the creatures already posted here.


SAMPLE:

![CreaturesScreenshot](https://user-images.githubusercontent.com/50467171/83375187-09a11a00-a39c-11ea-8c29-83639bec0c94.png)



INSTALL:
 
 After downloading the files, simply open blender and go to Edit -> Preferences, and under the Add-ons tab select the "Install" button then navigate to where the zipped folder with the files is located and select it (do not unzip/extract the files). Don't forget to check the box to enable the addon after installing it.

SOME NOTES:


  add_tiger.py:
  
   Images of several different species of tigers were used to create this (2 Sumatran and 1 Bengal), the dimensions were an average taken across "all" species a few minutes of searching could turn up.


------------------------------------------------------------------------------------------------------------

  add_wolf.py:
  
   The images used to create this mesh were of Gray Wolves inhabiting the western US. Dimensions were the average of google results for 'dimensions of gray wolf'

------------------------------------------------------------------------------------------------------------

  add_box_turtle.py:
  
   The images used to create this object were all of Eastern Box Turtles, Dimensions were the average of google results for 'dimensions of eastern box turtle'

------------------------------------------------------------------------------------------------------------

  General:
  
   I've been using Unity game engine lately so -y is forward on all models
   
   These were all constructed on the creatures left side with a mirror modifier, so it is recommened to delete the right side and apply a mirror modifier to keep symmetries when adding details (I may add in a half version of all the creatures for this purpose soon)
   
   After adding the mesh to the 3D View area make sure to go to the object menu and select "shade smooth"
   
-------------------------------------------------------------------------------------------------------------

CreatureMenu.py
  
  The intended menus have not all been created yet, but here is a context menu to consolidate these add mesh buttons. It's intended to be a context menu in the 3D viewport, but I haven't put a default hot-key in it yet, I set to (alt Right Press) while testing. To do this after installing all the add-mesh addons, in Edit -> Preferences choose the Keymap tab, and expand the list items for 3D View -> Object Mode, and at the bottom of the list select the "Add New" button. For the identifier (box that probably says 'none' by default) enter "wm.call_menu" then in the name field enter "object.Creatures" and finally use the available options to choose how the context menu will be accessed.

--------------------------------------------------------------------------------------------------------------
    
