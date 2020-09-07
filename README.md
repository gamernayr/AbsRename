**AbsRename**
By Ryan Epp

---
**Features:**
Batch rename files to comply with media services like Plex or Jellyfin. 

**Example:**
- Choose a formatting option
  - Option 1: Changing a specific portion
    - Better suited for adding a character (an 'E' for example to enable absolute ordering), word, or numbering changes
  - Option 2: Set the name one by one
    - Unable to set custom episode names for each episode, but better for overall formatting
    - Since it runs through each file in order, using the built in count works just fine
- Set the working directory
  - This can be done through the program, as there is a very lite python navigation shell
  - Alternatively, copy paste your directory into line 3
    - If you arent using this method, make sure to comment line 3 out
- Navigate and make sure that the folder you are in is the right using 'ls'
- Type 'run' and let the magic happen

**Requirements:**
- Python 3 enabled terminal

**Bugs/Needs Improvement:**
- The entire process is clunky, but the script is written and ready to be used with few changes

**Notes:**
- Although this was originally meant to be used for changing large amounts of episode filenames, it's a good template for renaming files in numerical order. 
