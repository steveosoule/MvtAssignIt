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