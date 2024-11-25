# my progress of learning how to write manim code to create some animations some fixes and my changes are listed below

## change 1 -> getting the light mode to work
fix -> you just go to config file which is at in my case C:/Users/Bakul/manim/manim.cfg (create one if its not there already)
add this code

```
[scene]
background_color = WHITE    
```

this changes the default background color to white you may write the code to change to black if you want that but personal preference was white

and at the start of every file you write this

```
config.background_color = WHITE
```
to change it to white

```
config.background_color = BLACK 
```
to change it back to black