import os
import templates


class weekfiles(object):
	def __init__(self):
		"""
		Constructor for the pagefiles object
		"""
		self.root = '/home/kceades/Documents/teaching/physics7b'
		self.filedir = self.root + '/weekfiles'

		self.PopFiles()

	def PopFiles(self):
		"""
		Populates the files by looking through the self.filedir directory
		for all the topic files
		"""
		if not os.path.isdir(self.filedir):
			self.files = []
		else:
			self.files = []
			for file in os.listdir(self.filedir):
				self.files.append(os.path.join(self.filedir,file))


class topicfiles(object):
	def __init__(self):
		"""
		Constructor for the pagefiles object
		"""
		self.root = '/home/kceades/Documents/teaching/physics7b'
		self.filedir = self.root + '/topicfiles'

		self.PopFiles()

	def PopFiles(self):
		"""
		Populates the files by looking through the self.filedir directory
		for all the topic files
		"""
		if not os.path.isdir(self.filedir):
			self.files = []
		else:
			self.files = []
			for file in os.listdir(self.filedir):
				self.files.append(os.path.join(self.filedir,file))


class weekparser(object):
	def __init__(self,file):
		"""
		Constructor for the parser object
		"""
		self.file = file
		self.datadict = {'week':None,'days':None,'time':None}

		self.PopSections()

	def PopSections(self):
		"""
		Populates the parameters for the sections and the data in preparation
		for the templates file
		"""
		cfile = open(self.file,'r')
		for line in cfile:
			if line=='\n':
				continue
			cline = line.split(':')
			name = cline[0]
			data = cline[1]
			if data[-1:]=='\n':
				data = data[:-1]
			if name=='days':
				days = data.split(';')
				self.datadict[name] = days
			else:
				self.datadict[name] = data
		cfile.close()

class topicparser(object):
	def __init__(self,file):
		"""
		Constructor for the parser object
		"""
		self.file = file
		self.datadict = {'archtopic':None,'topic':None,'problems':None}

		self.PopSections()

	def PopSections(self):
		"""
		Populates the parameters for the sections and the data in preparation
		for the templates file
		"""
		cfile = open(self.file,'r')
		for line in cfile:
			if line=='\n':
				continue
			cline = line.split(':')
			name = cline[0]
			data = cline[1]
			if data[-1:]=='\n':
				data = data[:-1]
			if name=='problems':
				probs = data.split(';')
				self.datadict['problems'] = probs
			else:
				self.datadict[name] = data
		cfile.close()


class constructpages(object):
	def __init__(self):
		"""
		Constructor for populating all the website files
		"""
		self.topic_files = topicfiles()
		self.week_files = weekfiles()
		self.topics = {}
		self.weeks = []
		self.times = []

		self.RunTopicFiles()
		self.RunWeekFiles()
		self.RunIndex()

	def RunTopicFiles(self):
		"""
		Goes through all the files and publishes the data
		"""
		for file in self.topic_files.files:
			fdata = topicparser(file)
			a = fdata.datadict
			if a['archtopic'] not in self.topics:
				self.topics[a['archtopic']] = [a['topic']]
			else:
				self.topics[a['archtopic']].append(a['topic'])
		for file in self.topic_files.files:
			fdata = topicparser(file)
			a = fdata.datadict
			ftemp = templates.topictemplate(a['archtopic'],a['topic']\
				,self.topics[a['archtopic']],a['problems'])

	def RunWeekFiles(self):
		"""
		Goes through all the files and publishes the data
		"""
		for file in self.week_files.files:
			fdata = weekparser(file)
			a = fdata.datadict
			self.weeks.append(a['week'])
			self.times.append(a['time'])
			ftemp = templates.weektemplate(a['week'],a['days'],a['time'])

	def RunIndex(self):
		indtemp = templates.indextemplate(self.topics,self.weeks,self.times)


if __name__ == '__main__':
	x = constructpages()