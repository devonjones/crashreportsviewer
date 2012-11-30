#!/usr/bin/python
# vim:foldmethod=indent
from knewton.schema.base import *
from knewton.schema.run import execute

class Feedback(TableBase):
	def __init__(self, conn):
		TableBase.__init__(self, conn, "feedback")
		CreateFeedback(self, 1)

class CreateFeedback(TableUpdate):
	def run_up(self):
		if not self.table_exists():
			sql = '\n'.join([
				"CREATE TABLE %s (" % self.parent.name,
				"  id INT(11) NOT NULL AUTO_INCREMENT,",
				"  feedback_type_id INT(11) NOT NULL,",
				"  crash_id INT(11) NOT NULL,",
				"  status INT(11) NOT NULL,",
				"  PRIMARY KEY (id),",
				"  FOREIGN KEY (feedback_type_id)",
				"   REFERENCES feedback_types(id)",
				"   ON DELETE CASCADE,",
				"  FOREIGN KEY (crash_id)",
				"   REFERENCES crashes(id)",
				"   ON DELETE CASCADE",
				") ENGINE=InnoDB AUTO_INCREMENT=14171 DEFAULT CHARSET=utf8"])
			self.curs.execute(sql)

	def run_down(self):
		self.drop_table()

if __name__ == "__main__":
	execute(Feedback, 'crashreports/database.yml')
