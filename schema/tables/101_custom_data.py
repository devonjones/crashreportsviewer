#!/usr/bin/python
# vim:foldmethod=indent
from knewton.schema.base import *
from knewton.schema.run import execute

class CustomData(TableBase):
	def __init__(self, conn):
		TableBase.__init__(self, conn, "custom_data")
		CreateCustomData(self, 1)

class CreateCustomData(TableUpdate):
	def run_up(self):
		if not self.table_exists():
			sql = '\n'.join([
				"CREATE TABLE %s (" % self.parent.name,
				"  id INT(11) NOT NULL AUTO_INCREMENT,",
				"  crash_id INT(11) NOT NULL,",
				"  field_name VARCHAR(128) NOT NULL,",
				"  data text,",
				"  PRIMARY KEY (id),",
				"  KEY custom_data_field_name_index (field_name),",
				"  FOREIGN KEY (crash_id)",
				"   REFERENCES crashes(id)",
				"   ON DELETE CASCADE",
				") ENGINE=InnoDB AUTO_INCREMENT=14171 DEFAULT CHARSET=utf8"])
			self.curs.execute(sql)

	def run_down(self):
		self.drop_table()

if __name__ == "__main__":
	execute(CustomData, 'crashreports/database.yml')
