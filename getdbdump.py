import mechanize, sys, codecs, datetime # apt-get install python-mechanize

PHPMYADMIN_URL = "http://someserver/phpmyadmin"
MYSQL_USERNAME = "myuser"
MYSQL_PASSWORD = "mypass"
SERVER_NUMBER_IN_DROPDOWN = 4
MYSQL_DB_NAME = "mydb"
OUTPUT_FILE = "dbdump.sql"

br = mechanize.Browser()
print "Logging into phpmyadmin..."
br.open(PHPMYADMIN_URL)
br.select_form(name="login_form")
br["pma_username"] = MYSQL_USERNAME
br["pma_password"] = MYSQL_PASSWORD
br["server"] = [str(SERVER_NUMBER_IN_DROPDOWN)]
br.submit()

br.follow_link(url_regex="main.php")
br.follow_link(url_regex="server_export.php")
br.select_form(name="dump")
br["db_select[]"] = [MYSQL_DB_NAME]
print "Downloading database dump..."
resp = br.submit()
fp = codecs.open(OUTPUT_FILE, encoding="utf8", mode="w")
fp.write(resp.read().decode("utf8").replace("CREATE DATABASE ", "CREATE DATABASE IF NOT EXISTS "))
fp.close()
