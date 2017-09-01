import os


class indextemplate(object):
	def __init__(self,topics,weeks,times):
		self.title = 'Welcome 7Bers'
		self.topics = topics
		self.weeks = weeks
		self.times = times
		self.weeknums = [x.split(' ')[1] for x in self.weeks]
		self.flatweeks = ['w' + x for x in self.weeknums]
		self.root = '/home/kceades/Documents/teaching/physics7b'
		if not os.path.isdir(self.root):
			os.makedirs(self.root)

		self.data = ''

		self.PopHead()
		self.PopBody()

		self.PublishData()

	def FlatLower(self,s):
		"""
		Makes s lowercase and flattens it by removing spaces
		"""
		wordlist = s.lower().split(' ')
		rstring = ''
		for word in wordlist:
			rstring = rstring + word
		return rstring

	def PopHead(self):
		"""
		Populates the data string with the head
		"""
		self.data = self.data + \
"""<!DOCTYPE html>


<html lang='en-US'>

<head>
	<title>""" + self.title + """</title>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width,initial-scale=1'>
	<link rel='stylesheet' href='stylesheets/style.css?'>
</head>

<body>

<h1>Physics 7B Discussion File Repository</h1>

<a href='index.html'><img src='images/home.png'></a>

<p>This site is for storing and accessing the various files distributed in Sections 301 and 303. Hopefully this will make things easier for you all rather than digging through old emails. The material is sorted two different ways, by week and by topic.</p>

<p><a href='#byweek'>View material by week</a> or <a href='#bytopic'>view material by topic</a>.</p>

		""".format()

	def PopBody(self):
		"""
		Populates the data string with the body, including the problems and the
		solutions
		"""
		self.data = self.data + \
		"""
<h2 id='byweek'>Material by Week</h2>

<div class='main'>
		"""

		for i in range(len(self.weeks)):
			self.data = self.data + \
			"""
<a href='weeks/w""" + self.weeknums[i] + '/' + self.flatweeks[i] + """.html'>""" + self.weeks[i] + ': ' + self.times[i] + """</a>
			"""

		self.data = self.data + \
		"""
</div>

<h2 id='bytopic'>Material by Topic</h2>

<div class='main' id='bytopic'>
		"""

		for archtopic in self.topics:
			for topic in self.topics[archtopic]:
				self.data = self.data + \
				"""
<a href='topics/"""+archtopic+'/'+self.FlatLower(topic)+""".html'>"""+topic+"""</a>
				"""

		self.data = self.data + \
		"""
</div>

</body>

</html>""".format()

	def PublishData(self):
		"""
		Publishes the html file that has been fed to the template
		"""
		savefile = os.path.join(self.root,'index.html')

		file = open(savefile,'w')
		file.write(self.data)
		file.close()


class weektemplate(object):
	def __init__(self,week,days,times):
		"""
		Constructor for the topic template
		"""
		# creates all the 
		self.week = week
		self.weeknum = self.week.split(' ')[1]
		self.flatweek = 'w' + self.weeknum
		self.days = days
		self.times = times
		self.root = '/home/kceades/Documents/teaching/physics7b/weeks'
		if not os.path.isdir(self.root):
			os.makedirs(self.root)

		self.data = ''

		self.PopHead()
		self.PopHeader()
		self.PopBody()

		self.PublishData()

	def PopHead(self):
		"""
		Populates the data string with the head
		"""
		self.data = self.data + \
		"""
<!DOCTYPE html>


<html lang='en-US'>

<head>
	<title>""" + self.week + ': ' + self.times + """</title>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width,initial-scale=1'>
	<link rel='stylesheet' href='../../stylesheets/style.css?'>
</head>

		""".format()

	def PopHeader(self):
		"""
		Populates the data string with the first part of the body, the header
		containing the title in an h1 tag and the description of the page in
		the first few lines, as well as the link to the home in the picture
		"""
		self.data = self.data + \
		"""
<body>

<h1>""" + self.week + ': ' + self.times  + """</h1>

<a href='../../index.html'><img src='../../images/home.png'></a>

<p>This page contains the material for week """ + self.weeknum + """.</p>

		""".format()

	def PopBody(self):
		"""
		Populates the data string with the body, including the problems and the
		solutions
		"""
		self.data = self.data + \
		"""
<div class='pagecontainer'>

<div class='left'>

<h3>Problems:</h3>

		"""

		for day in self.days:
			self.data = self.data + \
			"""
<a href='""" + self.flatweek + 'd' + day + """.pdf'>Day """ + day + """ (p)</a>
			"""

		self.data = self.data + \
		"""
</div>

<div class='right'>

<h3>Solutions:</h3>

		"""

		for day in self.days:
			self.data = self.data + \
			"""
<a href='""" + self.flatweek + 'd' + day + """sol.pdf'>Day """ + day + """ (s)</a>
			"""

		self.data = self.data + \
		"""
</div>

</div>

</body>

</html>
		""".format()

	def PublishData(self):
		"""
		Publishes the html file that has been fed to the template
		"""
		savedir = self.root + '/' + self.flatweek
		if not os.path.isdir(savedir):
			os.makedirs(savedir)
		savename = self.flatweek + '.html'
		savefile = os.path.join(savedir,savename)

		file = open(savefile,'w')
		file.write(self.data)
		file.close()


class topictemplate(object):
	def __init__(self,archtopic,topic,othertopics):
		"""
		Constructor for the topic template
		"""
		# creates all the 
		self.archtopic = archtopic
		self.topic = topic
		self.othertopics = [x for x in othertopics if x!=self.topic]
		self.root = '/home/kceades/Documents/teaching/physics7b/topics'
		if not os.path.isdir(self.root):
			os.makedirs(self.root)

		self.data = ''

		self.PopHead()
		self.PopHeader()
		self.PopBody()

		self.PublishData()

	def FlatLower(self,s):
		"""
		Makes s lowercase and flattens it by removing spaces
		"""
		wordlist = s.lower().split(' ')
		rstring = ''
		for word in wordlist:
			rstring = rstring + word
		return rstring

	def PopHead(self):
		"""
		Populates the data string with the head
		"""
		self.data = self.data + \
		"""
<!DOCTYPE html>


<html lang='en-US'>

<head>
	<title>""" + self.topic + """</title>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width,initial-scale=1'>
	<link rel='stylesheet' href='../../stylesheets/style.css?'>
</head>

		""".format()

	def PopHeader(self):
		"""
		Populates the data string with the first part of the body, the header
		containing the title in an h1 tag and the description of the page in
		the first few lines, as well as the link to the home in the picture
		"""
		self.data = self.data + \
		"""
<body>

<h1>""" + self.topic + """</h1>

<a href='../../index.html'><img src='../../images/home.png'></a>

<p>This page contains material about """ + self.topic.lower() + """</p>

		""".format()

	def PopBody(self):
		"""
		Populates the data string with the body, including the problems and the
		solutions
		"""
		self.data = self.data + \
		"""

<div class='pagecontainer'>

<div class='left'>

<h3>Problems:</h3>

<a href='""" + self.FlatLower(self.topic) + """.pdf'>""" + self.topic + """ (p)</a>

</div>

<div class='right'>

<h3>Solutions:</h3>

<a href='""" + self.FlatLower(self.topic) + """sol.pdf'>""" + self.topic + """ (s)</a>

</div>

</div>

		"""

		if self.othertopics!=[]:
			self.data = self.data + \
			"""
<p class='ot'>Related topics under in """ + self.archtopic + """:</p>

<div class='main'>
			"""
			for ot in self.othertopics:
				self.data = self.data + \
				"""
<a href='""" + self.FlatLower(ot) + """.html'>""" + ot + """</a>
				"""

		self.data = self.data + \
		"""
</div>

</body>

</html>
		""".format()

	def PublishData(self):
		"""
		Publishes the html file that has been fed to the template
		"""
		savedir = self.root + '/' + self.archtopic
		if not os.path.isdir(savedir):
			os.makedirs(savedir)
		savename = self.FlatLower(self.topic) + '.html'
		savefile = os.path.join(savedir,savename)

		file = open(savefile,'w')
		file.write(self.data)
		file.close()