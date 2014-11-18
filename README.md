# MvtAssign It - Sublime Text Plugin

This Sublime Text plugin allows you to convert Toolkit variable assignments into Miva's default variable assignments. This works for Toolkit's mvassign, vassign, and sassign

### For Example

#### This:
```
<mvt:item name="tooltit" param="mvassign|foo|'Bar'" />
```

#### Becomes:
```
<mvt:assign name="g.foo" value="'Bar'" />
```

## Installation Instructions

Clone this repo into your Sublime Text Packages directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages`. You should now have a new directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages\MvtAssignIt`

## Usage Instructions

1. Select the toolkit item(s)
2. `ctrl` + `shft` + `p` to bring up the Command Palette
3. Type in, "MvtAssign It" and select it.
4. Voila, your item has been converted