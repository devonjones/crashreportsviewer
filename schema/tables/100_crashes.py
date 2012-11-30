#!/usr/bin/python
# vim:foldmethod=indent
from knewton.schema.base import *
from knewton.schema.run import execute

class Crashes(TableBase):
	def __init__(self, conn):
		TableBase.__init__(self, conn, "crashes")
		CreateCrashes(self, 1)

class CreateCrashes(TableUpdate):
	def run_up(self):
		if not self.table_exists():
			sql += "CREATE TABLE crashes ("
			sql += "  id int(11) NOT NULL AUTO_INCREMENT,"
			sql += "  added_date int(11) NOT NULL,"
			sql += "  status int(11) NOT NULL,"
			sql += "  issue_id varchar(32) NOT NULL,"
			sql += "  report_id text NOT NULL,"
			sql += "  app_version_code text NOT NULL,"
			sql += "  app_version_name text NOT NULL,"
			sql += "  package_name text NOT NULL,"
			sql += "  file_path text NOT NULL,"
			sql += "  phone_model text NOT NULL,"
			sql += "  android_version text NOT NULL,"
			sql += "  build text NOT NULL,"
			sql += "  brand text NOT NULL,"
			sql += "  product text NOT NULL,"
			sql += "  total_mem_size int(11) NOT NULL,"
			sql += "  available_mem_size int(11) NOT NULL,"
			sql += "  custom_data text NOT NULL,"
			sql += "  stack_trace text NOT NULL,"
			sql += "  initial_configuration text NOT NULL,"
			sql += "  crash_configuration text NOT NULL,"
			sql += "  display text NOT NULL,"
			sql += "  user_comment text NOT NULL,"
			sql += "  user_app_start_date datetime DEFAULT NULL,"
			sql += "  user_crash_date datetime DEFAULT NULL,"
			sql += "  dumpsys_meminfo text NOT NULL,"
			sql += "  dropbox text NOT NULL,"
			sql += "  logcat text NOT NULL,"
			sql += "  eventslog text NOT NULL,"
			sql += "  radiolog text NOT NULL,"
			sql += "  is_silent text NOT NULL,"
			sql += "  device_id text NOT NULL,"
			sql += "  installation_id text NOT NULL,"
			sql += "  user_email text NOT NULL,"
			sql += "  device_features text NOT NULL,"
			sql += "  environment text NOT NULL,"
			sql += "  settings_system text NOT NULL,"
			sql += "  settings_secure text NOT NULL,"
			sql += "  shared_preferences text NOT NULL,"
			sql += "  PRIMARY KEY (id),"
			sql += "  KEY crashes_issue_id_index (issue_id)"
			sql += ") ENGINE=MyISAM AUTO_INCREMENT=14171 DEFAULT CHARSET=utf8"
			self.curs.execute(sql)

	def run_down(self):
		self.drop_table()

if __name__ == "__main__":
	execute(Crashes, '../database.yml')
