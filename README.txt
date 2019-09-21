# Ranger-File-Path-Paster
Plugin to paste the full absolute paths  of all of the file/dirs that you have selected

Install:
    Make sure to install ranger: https://github.com/ranger/ranger.git
    Should see folder /usr/local/lib/python2.7/dist-packages/ranger/
    
    run 'sudo chmod 777 auto_install.sh'
    restart ranger

WARNING: 
    The auto_install.sh script will overwrite:
        /usr/local/lib/python2.7/dist-packages/ranger/core/fm.py
        /usr/local/lib/python2.7/dist-packages/ranger/core/loader.py
        /usr/local/lib/python2.7/dist-packages/ranger/container/directory.py
        ~/.config/ranger/commands.py



Usage:
    Select files via <space>, then in directory of your choice run ":touch_selected_files_paths"
        which will create empty files with the selected files paths as the file name

    The command lives in ~/..config/ranger/commands.py which you are free to rename 

    In order to bind this command to a key, you will need to go to your rc.conf
        EX: map PP touch_selected_files_paths
