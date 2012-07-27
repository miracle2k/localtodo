localtodo
=========

.gitignore local todo files, but sync them through Dropbox.


What this is
------------

I like to use a ``LOCAL_TODO`` file for each of my projects as a
whiteboard for ideas, notes on what is currently being worked on
(useful when coming back to a project after some time), and things
in that vein.

Because these files are not under version control, I use Dropbox to
sync them across machines (this also serves as a backup).

What this script does is place such a file in a shared folder (for
example, managed by Dropbox), and then links this file into the
current directory.


How to use
----------

Install via::

    $ easy_install localtodo

Add the following line to your ``.gitignore`` file (or something
equivalent for the respective ignore mechanism of your version
control system)::

    /LOCAL_TODO*

The trailing wildcard will allows for multiple todo files, something
this script supports.

In your project directory, run::

    $ localtodo --to ~/Dropbox/todofiles
    Creating new empty file ~/Dropbox/todofiles/myproject

    I have established the following links for you:
        ./LOCAL_TODO --> ~/Dropbox/todofiles/myproject

Note: The ``--to`` argument is only required the first time and is
cached in ``~/.localtodo``.

As you can see, this created a new file in your chosen folder, and
created a link to it in the current directory.

By default, the name of the todo file will be inferred from the
basename of the current directory. You can also specify a custom name::

    $ localtodo foo
    Creating new empty file ~/Dropbox/todofiles/foo

    I have established the following links for you:
        ./LOCAL_TODO --> ~/Dropbox/todofiles/foo

If the todo file already exists, it will not be overridden. If
a LOCAL_TODO file already exists in the current directory, it will
be used and copied. So when you start working on your project on a
different machine, you again run the script::

    $ localtodo
    Found existing file ~/Dropbox/todofiles/foo

    I have established the following links for you:
        ./LOCAL_TODO --> ~/Dropbox/todofiles/foo

Multiple todo files for one project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's possible to create **sub-todos**::

    $ localtodo -s docs
    Creating new empty file ~/Dropbox/todos/myproject.docs

    I have established the following links for you:
        ./LOCAL_TODO.docs --> ~/Dropbox/todos/myproject.docs


When running ``localtodo``, it will find all the todo files related
to the current project, and link all of them into the current
directory.