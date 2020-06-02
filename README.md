# Creatures
<p>A series of plugins for Blender for additional (Object->Add->Mesh) buttons to insert starter shapes for a number of animals: sized and proportioned accurately so that artists can focus more time on adding details.
I wanted these starter shapes and figured I'd go ahead and share them with others. This is still a work in progress so more creatures will be forthcoming (and eventually/hopefully some riggings ready to go with them) along with improvements/updates to the creatures already posted here.</p>


<h2>SAMPLE:</h2>

![screenshot](https://user-images.githubusercontent.com/50467171/83578884-ccf13200-a505-11ea-98e9-c802c2f1ec64.png)



<h2>INSTALL:</h2>
 
 Under Clone/Download select the option to "download ZIP" then simply open blender and go to Edit -> Preferences, and under the Add-ons tab select the "Install" button, navigate to where the downloaded zip folder ("Creatures-Master") is located and select it without extracting the files to install all the meshes and context menu. Don't forget to check the box to enable the addon after installing it.






<h2>SOME NOTES:</h2>


<h4>CreatureMenu.py</h4>
  
  <blockquote>The intended menus have not all been created yet, but here is a context menu to consolidate these add mesh buttons. It's intended to be a context menu in the 3D viewport, but I haven't put a default hot-key in it yet, I set to (alt Right Press) while testing. To do this after installing, in Edit -> Preferences choose the Keymap tab, and expand the list items for 3D View -> Object Mode, and at the bottom of the list select the "Add New" button. For the identifier (box that probably says 'none' by default) enter "wm.call_menu" then in the name field that appears after inputting the type enter "OBJECT_MT_creature_menu" and finally use the available options to choose how the context menu will be accessed.</blockquote>


    

  <h4>add_tiger.py:</h4>
  
   <blockquote>Images of several different species of tigers were used to create this (2 Sumatran and 1 Bengal), the dimensions were an average taken across "all" species of tigers a few minutes of searching could turn up.</blockquote>




  <h4>add_wolf.py:</h4>
  
   <blockquote>The images used to create this mesh were of Gray Wolves inhabiting the western US. Dimensions were the average of google results for 'dimensions of gray wolf'</blockquote>


  <h4>add_box_turtle.py:</h4>
  
   <blockquote>The images used to create this object were all of Eastern Box Turtles, Dimensions were the average of google results for 'dimensions of eastern box turtle'</blockquote>
   

 
 <h4>add_iguana.py:</h4>
   <blockquote>The images were of green iguanas, and while searching for some I noticed that the length of spikes in various areas and flappy thing seem to be unique like a fingerprint to each iguana, so on the mesh I merely marked them, but that is definitely something you may want to do a quick search for and get an idea of the ranges for them when detailing an iguana model.
   The dimensions were determined by averaging the results from searching google for 'dimensions of an iguana'</blockquote>



  <h4>General:</h4>
  
   <blockquote>I've been using Unity game engine lately so -y is forward on all models
   
   These were all constructed on the creatures left side with a mirror modifier, so it is recommened to delete the right side and apply a mirror modifier to keep symmetries when adding details (I may add in a half version of all the creatures for this purpose soon)
   
   After adding the mesh to the 3D View area make sure to go to the object menu and select "shade smooth"</blockquote>
   



