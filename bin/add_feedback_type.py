#!/usr/bin/env python
import sys
import os
import MySQLdb
from optparse import OptionParser
from knewton.config import fetch_config
from knewton.schema.utils import db_connect

def select_feedback_type(curs, name):
	sql = '\n'.join([
		"SELECT *",
		" FROM feedback_types",
		" WHERE name = %s"])
	curs.execute(sql, [name])
	return curs.fetchall()

def insert_feedback_type(curs, name, field_name):
	sql = '\n'.join([
		"INSERT INTO feedback_types",
		" (name, field_name)",
		" VALUES",
		" (%s, %s)"])
	curs.execute(sql, [name, field_name])

def create_feedback_type(curs, name, field_name):
	recs = select_feedback_type(curs, name)
	if len(recs) > 0:
		sys.stderr.write("Feedback Type of %s already exists\n" % name)
		sys.exit(1)
	insert_feedback_type(curs, name, field_name)
	
def create(conn, name, field_name):
	curs = conn.cursor(MySQLdb.cursors.DictCursor)
	try:
		create_feedback_type(curs, name, field_name)
		conn.commit()
	finally:
		conn.rollback()
		conn.close()

def main():
	parser = optionParser()
	(options, args) = parser.parse_args()
	if len(args) != 2:
		sys.stderr.write("usage: %prog [options] [name] [field name]\n")
		sys.exit(1)
	yf = fetch_config('crashreports/database', options.config)
	conn = db_connect(yf['database'])
	create(conn, args[0], args[1])
 
def optionParser():
	usage = "usage: %prog [options] [name] [field name]\n\n"
	usage += "lets you create new feedback types."
	parser = OptionParser()
	parser.add_option(
		"-c", "--config", dest="config",
		 help="database config file (default crashreports/database)")
	parser.set_defaults(schema = False)
	return parser

if __name__ == "__main__":
	main()

