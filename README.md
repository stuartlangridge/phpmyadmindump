# phpmyadmindump
Export a database dump from MySQL on the command line, if you only have access to phpmyadmin.

Sometimes, especially on shared hosting, you may not have access to the actual MySQL database you're working with; the MySQL server may only be available on the host's internal network, and instead you have access to phpmyadmin to do admin tasks.

However, if you want to take a backup from a script, this is annoying; you can sign into phpmyadmin in the browser and do an export, but that's not scriptable.

So, a short Python app to export a database dump from the command line by talking to phpmyadmin.

You'll need to edit this a bit to make it work for you. In particular, you'll need to identify the number of the server in the server dropdown in phpmyadmin's login screen and set that in the script.
