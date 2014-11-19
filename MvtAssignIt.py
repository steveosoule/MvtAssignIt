import sublime_plugin
from xml.dom.minidom import parseString
import re

class MvtAssignItCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selections = self.view.sel()
    # Loop over currently selected text
    for selection in selections:
      if not selection.empty():
        tag = self.view.substr(selection)
        new_tag = self.transform_tag( tag );
        if new_tag:
          self.view.replace(edit, selection, new_tag)
  def transform_tag(self, tag):
    new_tag = ''
    dom = parseString( re.sub('^<mvt:item', '<mvt_item', tag) )

    # Check item name and list out params
    item_name = dom.getElementsByTagName('mvt_item')[0].attributes["name"].value
    params = dom.getElementsByTagName('mvt_item')[0].attributes["param"].value.split('|')
    assign_type = params[0]
    variable = params[1]
    value = params[2]

    # Only update the assignment functions
    if item_name not in ['ry_toolbelt', 'toolkit', 'sebenzatools'] or assign_type not in ['sassign', 'mvassign', 'vassign', 'assign', 'var']:
      return False

    # prepare global and local variable prefixes,
    # change l.all_settings to l.settings
    variable = re.sub("^l\.all_settings:", 'l.settings:', variable)
    match = re.match('^[^(l\.|g\.)]', variable)
    variable = 'g.' + variable if match else variable
    value = "'" + value + "'" if assign_type == 'sassign' else value
    value = re.sub("l\.all_settings:", 'l.settings:', value)

    # Output new mvt:assign tag
    new_tag = '<mvt:assign name="%s" value="%s" />' % (variable, value)

    return new_tag