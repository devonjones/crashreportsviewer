#!/usr/bin/python
# vim:foldmethod=indent
from knewton.schema.base import *
from knewton.schema.run import execute

class FeedbackTypes(TableBase):
	def __init__(self, conn):
		TableBase.__init__(self, conn, "feedback_types")
		CreateFeedbackTypes(self, 1)

class CreateFeedbackTypes(TableUpdate):
	def run_up(self):
		if not self.table_exists():
			sql = '\n'.join([
				"CREATE TABLE %s (" % self.parent.name,
				"  id INT(11) NOT NULL AUTO_INCREMENT,",
				"  name VARCHAR(128),",
				"  field_name varchar(128),",
				"  PRIMARY KEY (id)",
				") ENGINE=InnoDB AUTO_INCREMENT=14171 DEFAULT CHARSET=utf8"])
			self.curs.execute(sql)

	def run_down(self):
		self.drop_table()

if __name__ == "__main__":
	execute(FeedbackTypes, 'crashreports/database.yml')
