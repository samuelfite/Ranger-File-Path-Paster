# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import *

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

# You can import any python module as needed.
import os

# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!


class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()




class touch_selected_files_paths(Command):
    ''':touch_paths <paste_dir>
    Command to paste the names of the selected paths in the current directory,
    with / replaced with __ for compatability. Used for gathering
    files/directories to sync/scan
    '''
    def execute(self):
        from os.path import join, expanduser, lexists
        # paste file in current dir
        base_filename = self.fm.thisdir.path + '/'

        # get all paths leading to marked(selected) files
        for selected_path in self.fm.marked_file_dir:
            #get ranger directory object for selected dir
            if self.fm.directories[selected_path] is not None:
                for selection in self.fm.directories[selected_path].get_selection():

                    final_filename = str( selection ).replace( '/', '+-+' ) 
                    if 'Directory' in str( type( selection ) ):
                        final_filename += '+-+'

                    final_filename = base_filename + final_filename
                    self.fm.notify( str(final_filename) )

                    if not lexists( final_filename ):
                        open( final_filename, 'a' ).close()
                    else:
                        self.fm.notify( "file/directory exists!", bad=True )
            else:
                self.fm.notify( "could not find path: " + str(selected_path), bad=True )
