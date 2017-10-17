import sublime
import sublime_plugin
import re

class OneLineCopyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = ''

        for region in self.view.sel():
            if not region.empty():
                selection += self.view.substr(region)

        if selection:
            sublime.set_clipboard(self.sanitize_selection(selection))

    def sanitize_selection(self, selection):
        return ' '.join(re.sub(r'[ ]{2,}', '', selection).splitlines())
