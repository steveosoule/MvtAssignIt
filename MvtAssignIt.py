import sublime_plugin
from xml.dom.minidom import parseString
import re

class MvtAssignItCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selections = self.view.sel()
    for selection in selections:
      if not selection.empty():
        tag = self.view.substr(selection)
        new_tag = self.transform_tag( tag );
        self.view.replace(edit, selection, new_tag)
  def transform_tag(self, tag):
    new_tag = ''
    dom = parseString( re.sub('^<mvt:item', '<mvt_item', tag) )
    params = dom.getElementsByTagName('mvt_item')[0].attributes["params"].value
    params = params.split('|')

    assign_type = params[0]
    variable = params[1]
    value = params[2]

    variable = re.sub("^l\.all_settings:", 'l.settings:', variable)
    match = re.match('^[^(l\.|g\.)]', variable)
    variable = 'g.' + variable if match else variable
    value = "'" + value + "'" if assign_type == 'sassign' else value
    value = re.sub("l\.all_settings:", 'l.settings:', value)
    new_tag = '<mvt:assign name="%s" value="%s" />' % (variable, value)

    return new_tag