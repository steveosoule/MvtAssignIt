# MvtAssign It - Sublime Text Plugin

Sublime Text plugin allows you to convert Toolkit, Toolbelt, and Sebenza Tools variable assignments into Miva's default variable assignments.

### For Example

#### This:

```
<mvt:item name="toolkit" params="sassign|foo|bar" />
<mvt:item name="toolkit" params="vassign|foo|l.all_settings:bar" />
<mvt:item name="toolkit" params="mvassign|foo|'bar' $ '!'" />
<mvt:item name="ry_toolbelt" param="assign|g.foo|toupper('bar')" />
<mvt:item name="sebenzatools" param="var|foo|'bar'" />
```

#### Becomes:
```
<mvt:assign name="g.foo" value="'bar'" />
<mvt:assign name="g.foo" value="l.settings:bar" />
<mvt:assign name="g.foo" value="'bar' $ '!'" />
<mvt:assign name="g.foo" value="toupper('bar')" />
<mvt:assign name="g.foo" value="'bar'" />
```
## Features

* Automatically converts `l.all_settings` variable references to `l.settings`
* Convert multiple items at once
* Works with Sublime Text 2 & Sublime Text 3
* Works on:
	* **Toolkit**
	    *  sassign `<mvt:item name="toolkit" params="sassign|foo|bar" />`
	    *  vassign `<mvt:item name="toolkit" params="vassign|foo|l.all_settings:bar" />`
	    *  mvassign `<mvt:item name="toolkit" params="mvassign|foo|'bar' $ '!'" />`
    *  **Toolbelt**
        *  assign `<mvt:item name="ry_toolbelt" param="assign|g.foo|'bar'" />`
    *  **Sebenza Tools**
        *  var `<mvt:item name="sebenzatools" param="var|foo|'bar'" />`

## Installation Instructions

Clone this repo into your Sublime Text Packages directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages`. You should now have a new directory: `C:\Users\YOUR_USERNAME\AppData\Roaming\Sublime Text 2\Packages\MvtAssignIt`

## Usage Instructions

1. Select the toolkit item(s)
2. `Ctrl` + `Shft` + `P` to bring up the Command Palette
3. Select the "MvtAssign It" option
4. Voila, your item has been converted

## Why is this important?

Simply put, `mvt:assign` is **faster**.

Using the `/benchmarks/benchmark.mvt` code I tested how long it would take to iterate through an `mvt:while` loop for N numbers of times. At the maximum recorded number (10,000) `mvt:assign` was roughly **20 seconds faster** than Toolbelt's assign and **25 seconds faster** than Toolkit's mvassign!

| Iterations                   | mvt:assign      | Toolkit        | Toolbelt       |
|------------------------------|-----------------|----------------|----------------|
| 1                            | 0.000171 sec.   | 0.000574 sec.  | 0.000361 sec.  |
| 10                           | 0.000164 sec.   | 0.001843 sec.  | 0.001613 sec.  |
| 100                          | 0.000309 sec.   | 0.022553 sec.  | 0.018862 sec.  |
| 1,000                        | 0.001952 sec.   | 0.184801 sec.  | 0.135798 sec.  |
| 10,000                       | 0.021111 sec.   | 1.675808 sec.  | 1.313019 sec.  |
| 100,000                      | 0.232023 sec.   | 25.186679 sec. | 20.041977 sec. |
| 1,000,000                    | 1.956414 sec.   | 3000\* sec.     | 3000\* sec.     |

\* 5 min. timeout was reached