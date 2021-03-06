# Creatures
<p>A series of plugins for Blender for additional (Object->Add->Mesh) buttons to insert starter shapes for a number of animals: sized and proportioned accurately so that artists can focus more time on adding details.
I wanted these starter shapes and figured I'd go ahead and share them with others. This is still a work in progress so more creatures will be forthcoming (and eventually/hopefully some riggings ready to go with them) and perhaps with improvements/updates to the creatures already posted here.</p>


<h2>SAMPLE:</h2>

![screenshot](https://user-images.githubusercontent.com/50467171/83958606-c1717400-a841-11ea-8fcb-c87571796221.png)



<h2>INSTALL:</h2>
 
 Under Clone/Download select the option to "download ZIP" then simply open blender and go to Edit -> Preferences, and under the Add-ons tab select the "Install" button, navigate to where the downloaded zip folder ("Creatures-Master") is located and select it without extracting the files to install all the meshes and context menu. Don't forget to check the box to enable the addon after installing it.






<h2>SOME NOTES:</h2>


<h4>Full vs. Half Models</h4>

<blockquote>
 Representing living creatures these meshes all possess bilateral symmetry. To take advantage of the symmetry only half of the model was created. To finish out the other half: Insert a half model and apply a mirror modifier (see figures below --the defaults should be fine, just make sure x-axis is selected), and then work on symmetrical details can be carried out simply on one half of the model. When ready click the "apply" button in the modifier to generate the other half of the model and finish out any asymmetrical details for the finished character.
 
 ![half_mesh_1](https://user-images.githubusercontent.com/50467171/83579334-f9597e00-a506-11ea-9d8e-9dddfbe70cae.png)
![half_mesh_2](https://user-images.githubusercontent.com/50467171/83579335-f9f21480-a506-11ea-8974-11e8b9fa2e76.png)
![half_mesh_3](https://user-images.githubusercontent.com/50467171/83579337-f9f21480-a506-11ea-929b-ca4f9a35c1f9.png)
![half_mesh_4](https://user-images.githubusercontent.com/50467171/83579340-fa8aab00-a506-11ea-8f20-ae2962f9ca73.png)
![half_mesh_5](https://user-images.githubusercontent.com/50467171/83579342-fa8aab00-a506-11ea-8f78-2cd66f05dcfe.png)
![half_mesh_6](https://user-images.githubusercontent.com/50467171/83948247-f2be5580-a7e9-11ea-9735-fbf9c25a23fb.png)
![half_mesh_7](https://user-images.githubusercontent.com/50467171/83948249-f520af80-a7e9-11ea-9e08-1df12479d0a2.png)
 </blockquote>

<h4>CreatureMenu.py</h4>
  
  <blockquote>
 The intended menus have not all been created yet, but here is a context menu to consolidate these add mesh buttons. It's intended to be a context menu in the 3D viewport, but I haven't put a default hot-key in it yet, I set to (alt Right Press) while testing. To do this after installing, in Edit -> Preferences choose the Keymap tab, and expand the list items for 3D View -> Object Mode, and at the bottom of the list select the "Add New" button. For the identifier (box that probably says 'none' by default) enter "wm.call_menu" then in the name field that appears after inputting the type enter "OBJECT_MT_creature_menu" and finally use the available options to choose how the context menu will be accessed.


![hot_key_1](https://user-images.githubusercontent.com/50467171/83681432-67a64b00-a5b0-11ea-832f-adfe4ec53bd2.png)
![hot_key_2](https://user-images.githubusercontent.com/50467171/83681431-670db480-a5b0-11ea-92bc-33d80af8c9f3.png)
</blockquote>


    

  <h4>add_tiger.py:</h4>
  
   <blockquote>Images of several different species of tigers were used to create this (2 Sumatran and 1 Bengal), the dimensions were an average taken across "all" species of tigers a few minutes of searching could turn up.</blockquote>




  <h4>add_wolf.py:</h4>
  
   <blockquote>The images used to create this mesh were of Gray Wolves inhabiting the western US. Dimensions were the average of google results for 'dimensions of gray wolf'</blockquote>


  <h4>add_box_turtle.py:</h4>
  
   <blockquote>The images used to create this object were all of Eastern Box Turtles, Dimensions were the average of google results for 'dimensions of eastern box turtle'</blockquote>
   

 
 <h4>add_iguana.py:</h4>
   <blockquote>The images were of green iguanas, and while searching for some I noticed that the length of spikes in various areas and flappy thing seem to be unique like a fingerprint to each iguana, so on the mesh I merely marked them, but that is definitely something you may want to do a quick search for and get an idea of the ranges for them when detailing an iguana model.
   The dimensions were determined by averaging the results from searching google for 'dimensions of an iguana'</blockquote>
   
   
<h4>add_elephant.py</h4>
<blockquote>
 The images used were all of african elephants, and the sizes were set based off the average results from searching google for "dimensions of african elephant"
 </blockquote>



<h4>add_rabbit.py</h4>
<blockquote>
 The images used were all of cottontail rabbits, and the sizes were based off averages determined from searching google for "dimensions of a cottontail rabbit"
 
 A 'ready to hop' posture was selected and the upper part of the rear leg was made a little small to keep all vertices and faces visible, this will need expanded slightly when adding details.
 </blockquote>
 
 
 <h4>add_bullfrog.py</h4>
 <blockquote>
 The images used were all of American Bullfrogs, and sizes likewise were determined by searching google for "average dimensions of american bullfrog"
 
 To put it in the normal relaxed position for a bullfrog the rear legs were made a little thin so that all faces and vertices would be visible, these will need thickened slightly (pressed together for this posture) when detailing a model.
 
 </blockquote>


<h4>General:</h4>
  
<blockquote>
the negative y axis is forward on all models.
 
After adding the mesh to the 3D View area it is highly recommended to go to the object menu and select "shade smooth"

For the smaller animals it is definitely a good idea to scale it up to work with when adding detials, it can be easily scaled back down for usage. Zooming alone is kind of lacking on the small scales. While testing I changed the model's scale factor to 5.0 on all axes and after completing changed them back to 1.0 to get the actual size of the model.
</blockquote>
   



