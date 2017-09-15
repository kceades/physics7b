"""
Written by Kevin Caleb Eades (kceades)
Fall 2017
"""


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
		self.RunArchtopics()
		self.RunWeekFiles()
		self.RunIndex()

	def RunTopicFiles(self):
		"""
		Goes through all the topic files and publishes the topic pages
		"""
		for file in self.topic_files.files:
			fdata = topicparser(file)
			a = fdata.datadict
			if a['archtopic'] not in self.topics:
				self.topics[a['archtopic']] = [a['topic']]
			else:
				self.topics[a['archtopic']].append(a['topic'])

		# sort the topics dictionary, first by archtopic then by topic
		keylist = list(self.topics.keys())
		keylist.sort()
		new_dict = {}
		for key in keylist:
			current_list = self.topics[key]
			current_list.sort()
			new_dict[key] = current_list
		self.topics = new_dict

		# actually create and publish the pages
		for file in self.topic_files.files:
			fdata = topicparser(file)
			a = fdata.datadict
			ftemp = templates.topictemplate(a['archtopic'],a['topic']\
				,self.topics[a['archtopic']],a['problems'])

	def RunArchtopics(self):
		"""
		Goes through the archtopics and creates master pages for them
		with all the topics
		"""
		for archtopic in self.topics:
			ftemp = templates.archtemplate(archtopic,self.topics[archtopic])

	def RunWeekFiles(self):
		"""
		Goes through all the week files and publishes the week pages
		"""
		for file in self.week_files.files:
			fdata = weekparser(file)
			a = fdata.datadict
			self.weeks.append(a['week'])
			self.times.append(a['time'])
			ftemp = templates.weektemplate(a['week'],a['days'],a['time'])

	def RunIndex(self):
		"""
		Creates the index html page
		"""
		# sorting the weeks so they appear from most recent to oldest on the
		# page
		tempvar = [(self.weeks[i],self.times[i]) for i in range(len(self.weeks)\
			)]
		short_var = [x for x in tempvar if len(x[0])==6]
		long_var = [x for x in tempvar if len(x[0])==7]
		short_var.sort()
		long_var.sort()
		tempvar = short_var + long_var
		sorted_weeks = [x[0] for x in tempvar][::-1]
		sorted_times = [x[1] for x in tempvar][::-1]

		# actual call to the templates file to make the page
		indtemp = templates.indextemplate(self.topics,sorted_weeks,sorted_times)


if __name__ == '__main__':
	"""
	Uses the above classes to autobuild the website when builder.py is run
	"""
	x = constructpages()