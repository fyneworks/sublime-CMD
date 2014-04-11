import sublime
import sublime_plugin
import os

# Borrowed from http://bit.ly/1iDl6f6
def current_dir(window):
    """
    Return the working directory in which the window's commands should run.

    In the common case when the user has one folder open, return that.
    Otherwise, return one of the following (in order of preference):
        1) One of the open folders, preferring a folder containing the active
           file.
        2) The directory containing the active file.
        3) The user's home directory.
    """
    folders = window.folders()
    if len(folders) == 1:
        return folders[0]
    else:
        active_view = window.active_view()
        active_file_name = active_view.file_name() if active_view else None
        if not active_file_name:
            return folders[0] if len(folders) else os.path.expanduser("~")
        for folder in folders:
            if active_file_name.startswith(folder):
                return folder
        return os.path.dirname(active_file_name)


class CmdLaunchCommand(sublime_plugin.WindowCommand):
	def run(self, paths=None, isHung=False):
		dir = current_dir(self.window)

		if not dir:
			return
		
		command = 'cd %s & start cmd' % (dir)
		os.system(command)
