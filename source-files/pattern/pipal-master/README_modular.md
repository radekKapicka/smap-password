# Pipal Goes Modular

Copyright(c) 2022, Robin Wood <robin@digi.ninja>

This is a short doc to explain how the new modular checker and splitter system
works. It isn't finished yet so may well still change so I'll try to keep this
guide up-to-date.

Please get in touch if you have any questions, suggestions or general comments
about this new modular approach.

## Checkers

Checkers are the most important part of Pipal, they take the passwords and
perform the analysis on them. Originally they were all built into the main
script so were hard to maintain and it was even harder to add new ones so I
broke them out into their own modules called Checkers.

They are set up in the same style as Apache handles vhosts in some Linux
distributions, there is a checkers_available directory and a checkers_enabled
directory. To enable a checker simply symlink it into the enabled directory and
it will be used by the system. This will allow users who don't care about, say
Hashcat masks, to not have to spend processor cycles generating them. On a small
list this probably won't make much difference but it will on a large one.

To create a symlink you can use the following commands:

## Enable the basic checker

```bash
cd checkers_enabled
ln -s ../checkers_available/basic.rb .
```

## Enable the basic checker and make sure it is ran first (assuming no 00 files)

```bash
ln -s ../checkers_available/basic.rb 01basic.rb
```

## Enable all checkers

```bash
ln -s ../checkers_available/*rb .
```

The other good thing about the way Checkers now work is that it is easy to write
new ones. To see how simple a Checker can be take a look at the
windows_complexity_checker.rb file in checkers_available. 25 lines get you a
checker for default Windows complexity, to change this to cover your own rules
simply clone the file, update the regex, the name and a few bits of copy and
then symlink it into place.

If you want to check for a list of items then this is even easier, check out
colour_checker.rb, it is just 15 lines long. Give it a name, the list and a
description and the rest is taken care of for you.

The --list-checkers parameter will show you a list of all Checkers which are
available along with a brief description. I'd like to extend this so each
Checker will also contain a more detailed description which can also be
requested.

## Splitters

What about if you want to process a file that doesn't just contain passwords,
maybe it has usernames in it as well. The default action is to treat each new
line in the file as a password but with a custom Splitter you can now define
what is the password and what is extra data. You can then write a custom Checker
which can understand the extra data and off you go. Any existing Checkers which
don't care about extra data will just ignore it but your custom one will be able
to handle it.

As an example of this I've created a Splitter called pipe_pass_user.rb, as it
sounds, this is a pipe (|) separated file with the password first followed by
the username. The code again is fairly simple, a class with a static method
called split, that takes the line from the file and splits it down to the
password and the username. The password is returned on its own with the username
going in an associative array. The Checker username.rb is the only one which
currently understands how to handle the username field in the extras array and
it will take it and do various comparisons between the username and the
password.

Only a single splitter can be used at once. To do this symlink the Splitter you
want to use to a file called custom_splitter.rb in the main Pipal directory. It
will then be picked up automatically.
