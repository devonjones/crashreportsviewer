#!/usr/bin/python
# vim:foldmethod=indent
from knewton.schema.base import *
from knewton.schema.run import execute

class Crashes(TableBase):
	def __init__(self, conn):
		TableBase.__init__(self, conn, "crashes")
		CreateCrashes(self, 1)
		CreateIssueIdIndex(self, 2)
		AppVersionCodeToInteger(self, 3)
		CreateStatusIndex(self, 4)
		PackageNameToVarchar(self, 5)
		CreatePackageNameIndex(self, 6)
		CreateAppVersionCodeIndex(self, 7)
		AppVersionNameToiVarchar(self, 8)

class CreateCrashes(TableUpdate):
	def run_up(self):
		if not self.table_exists():
			sql = '\n'.join([
				"CREATE TABLE %s (" % self.parent.name,
				"  id INT(11) NOT NULL AUTO_INCREMENT,",
				"  added_date INT(11) NOT NULL,",
				"  status INT(11) NOT NULL,",
				"  issue_id VARCHAR(32) NOT NULL,",
				"  report_id text NOT NULL,",
				"  app_version_code text NOT NULL,",
				"  app_version_name text NOT NULL,",
				"  package_name text NOT NULL,",
				"  file_path text NOT NULL,",
				"  phone_model text NOT NULL,",
				"  android_version text NOT NULL,",
				"  build text NOT NULL,",
				"  brand text NOT NULL,",
				"  product text NOT NULL,",
				"  total_mem_size INT(11) NOT NULL,",
				"  available_mem_size INT(11) NOT NULL,",
				"  custom_data text NOT NULL,",
				"  stack_trace text NOT NULL,",
				"  initial_configuration text NOT NULL,",
				"  crash_configuration text NOT NULL,",
				"  display text NOT NULL,",
				"  user_comment text NOT NULL,",
				"  user_app_start_date DATETIME DEFAULT NULL,",
				"  user_crash_date DATETIME DEFAULT NULL,",
				"  dumpsys_meminfo text NOT NULL,",
				"  dropbox text NOT NULL,",
				"  logcat text NOT NULL,",
				"  eventslog text NOT NULL,",
				"  radiolog text NOT NULL,",
				"  is_silent text NOT NULL,",
				"  device_id text NOT NULL,",
				"  installation_id text NOT NULL,",
				"  user_email text NOT NULL,",
				"  device_features text NOT NULL,",
				"  environment text NOT NULL,",
				"  settings_system text NOT NULL,",
				"  settings_secure text NOT NULL,",
				"  shared_preferences text NOT NULL,",
				"  PRIMARY KEY (id),",
				") ENGINE=InnoDB AUTO_INCREMENT=14171 DEFAULT CHARSET=utf8"])
			self.curs.execute(sql)

	def run_down(self):
		self.drop_table()


class CreateIssueIdIndex(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"CREATE INDEX crashes_issue_id_index",
			" ON crashes (issue_id)"])
		print sql
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" DROP INDEX crashes_issue_id_index"])
		self.curs.execute(sql)

class AppVersionCodeToInteger(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE app_version_code app_version_code INT(11)"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE app_version_code app_version_code TEXT"])
		self.curs.execute(sql)

class CreateStatusIndex(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"CREATE INDEX crashes_status_index",
			" ON crashes (status)"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" DROP INDEX crashes_status_index"])
		self.curs.execute(sql)

class PackageNameToVarchar(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE package_name package_name VARCHAR(1024) NOT NULL"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE package_name package_name TEXT"])
		self.curs.execute(sql)

class CreatePackageNameIndex(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"CREATE INDEX crashes_package_name_index",
			" ON crashes (package_name)"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" DROP INDEX crashes_package_name_index"])
		self.curs.execute(sql)

class CreateAppVersionCodeIndex(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"CREATE INDEX app_version_code",
			" ON crashes (app_version_code)"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" DROP INDEX crashes_app_version_code_index"])
		self.curs.execute(sql)

class AppVersionNameToiVarchar(TableUpdate):
	def run_up(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE app_version_name app_version_name VARCHAR(1024) NOT NULL"])
		self.curs.execute(sql)

	def run_down(self):
		sql = '\n'.join([
			"ALTER TABLE %s" % self.parent.name,
			" CHANGE app_version_name app_version_name TEXT"])
		self.curs.execute(sql)

if __name__ == "__main__":
	execute(Crashes, 'crashreports/database.yml')
