# MvtAssign It

This plugin allows you to convert Toolkit variable assignments into Miva's default variable assignments. This works for Toolkit's mvassign, vassign, and sassign

### For Example

```
<mvt:item name="tooltit" param="mvassign|foo|'Bar'" />
```

Becomes

```
<mvt:assign name="g.foo" value="'Bar'" />
```

## Installation Instructions

Clone this repo into your Sublime Text Packages directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages`. You should now have a new directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages\MvtAssignIt`