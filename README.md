### SQL-Chat

![image1](https://discord-gui-docs-media.netlify.app/media/image1.png)

**[System Requirements]{.underline}**

**Minimum Hardware requirement:**

1)  For Server/Database:

-   10mbps internet connection (for this project, 4gbps connection was
    used)

-   Any 64 bit processor (for this project, an arm64 processor was used)

-   At least 10GB of storage (minimum for any mysql server)

-   At least 1gb of ram (for MySQL to run smoothly and manage
    connections)

2)  For Client/GUI:

-   A 500MHz processor (minimum for python to run smoothly)

-   128MB of ram (recommended 512MB ram for the application alone)

-   6MB of storage (to store userinfo, project files, and a complete
    python installation)

**Minimum Software requirements:**

1)  For Server/Database:

-   MySQL version 8.0.23 (or any version higher installed)

-   An open port for MySQL connections (port: 3306 was used here)

2)  For Client/GUI:

-   Python 3 must be installed

-   System must have PyPI packages "mysql-connector-python", "pillow"
    > and "requests" pre installed

**Important note:**

It is recommending that this code is executed using the dockerfile and
virtual environment or the compiled exe (Note, this is no longer
avalible as of 11:11 AM 30-Jun-23 as the repo is no longer maintained),
if these are used instead of the source code, most of the requirements
can be ignored.

**[User Manual/Instructions:]**

**Logging in:**

On running the program for the first time, you will be greeted with the
login page, where you can enter your login information, i.e username and
password, if you do not already have an account, you can register within
this page itself. Note that this page is only visible once when the code
is ran for the first time, after this, all your login info is stored in
the user.info file, and every time the code is ran, it will skip this
page unless the login info is outdated or invalid or has been changed.

**Home Page:**

The homepage has many clickables that perform different functions, the
gear on the top right is for managing your account/profile, the list of
rooms shows rooms of two types: private and global rooms. Right clicking
on the private rooms will open the room editor gui and left clicking on
any room will open it. Note that you can only see those rooms which you
actively have access to. The bottom right features a textbox, and 2
buttons, this can be used to search rooms and access unlisted rooms,
i.e, public rooms that exist but don't show up on the room list. The
plus sign can also allow you to access the room creation gui.

**Room Creation:**

To create a room, you must enter an id for that room and also a privacy
setting, which is global by default, this id must be unique, there are 3
privacy settings to choose from:

1)  Global: Global rooms are visible to everyone and show up in
    everybody's room list, anyone can enter these at any time to
    participate in them

2)  Unlisted: Anyone can enter these rooms but they do not show up in
    anybody's room list, to enter it, one must enter the room's unique
    id on the bottom of the homepage

3)  Private: These rooms are only accessible by a small group of people
    (max. 10), you can decide who has and doesn't have access to these
    rooms in the room editor interface. These rooms are the only ones
    that are editable later on too. They show up as red on the screens
    of those who can access them

Once this data is filled, simply click on the "create room" button.

**Room Editing:**

This gui is only accessible for private rooms, and only by those users
who have access to the private room itself, it allows you to remove and
add people to a private room and also change the private room's
settings, once all desired changes have been added, simply press "save",
note that changing the privacy setting of a private room will make the
room no longer editable

**Profile editor:**

This gui allows you to change aspects about your profile like your
username and password, however for any changes to be implemented you
must first enter your current password as a safety measure

**Chat GUI:**

This is a live chat interface that you can use to send and receive
messages, messages sent by the same person will show up under their
username and a timestamp for the messages is also often given.

**Error management:**

­­­­The application focuses on a simplified user experience and is quite
robust, if an error were to occur, the user will be notified via the gui
itself as shown below: ![Graphical user interface, text Description
automatically
generated](https://discord-gui-docs-media.netlify.app/media/image2.png){width="5.354913604549432in"
height="1.3126837270341207in"} ![Text Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image3.png){width="6.5in"
height="0.9847222222222223in"}

**[Modules and Functions]{.underline}**

Built in modules used:

1)  Tkinter -- used for GUI

2)  Random -- used for token generation for unique identification of
    users

3)  Pickle -- used to store user login information in a non human
    readable format

4)  Time -- used to send and display timestamps in the gui

5)  Threading -- used to stop mysql connections from interfering with
    tkinter's mainloop

PyPI modules used:

1)  MySQL connector -- used to access remote database

2)  Pillow -- used to display images in the gui

3)  Requests -- used to obtain the ip address of the user using ipify
    api

**[Program Output]{.underline}**

**Login Screen:**

![Graphical user interface, application, Teams Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image4.png){width="2.897976815398075in"
height="3.0877252843394576in"}

**Home Page:**

![Graphical user interface, text Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image5.png){width="3.7018689851268594in"
height="1.9373698600174978in"}

**Room Creation GUI:**

![Graphical user interface, application Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image6.png){width="3.4379615048118985in"
height="2.9256375765529308in"}

**Profile Editor:**

![Graphical user interface, website Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image7.png){width="3.1305489938757654in"
height="2.403028215223097in"}

**Chat Room Interface:**

![Graphical user interface, text Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image8.png){width="4.436823053368329in"
height="3.9561668853893264in"}

**Room Editor:**

![Graphical user interface Description automatically
generated](https://discord-gui-docs-media.netlify.app/media/image9.png){width="5.143277559055118in"
height="2.194686132983377in"}

**[Limitations:]{.underline}**

1)  In the current release of the code, only one user can be logged in
    at a time per installation of the client code, this is because a
    formal user management system has not been setup in the current
    version, instead, all the data is stored in a pickled binary file
    named "user.info", in order to log out of one's account, one must
    delete this file

**Possible fix:** Implement a user management system within the gui

![Graphical user interface, text, application, email Description
automatically
generated](https://discord-gui-docs-media.netlify.app/media/image10.png){width="2.5060509623797027in"
height="3.5473458005249343in"}

2)  On decompiling the exe or going through the source code one can find
    the mysql user login information and mis-use of this may give a
    person unfiltered access to the app's database.

**Possible Fix:** Using sockets to manage requests for sending and
receiving data packages, and adding authentication information in all
dta packages that are transferred
