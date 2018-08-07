from fman import DirectoryPaneListener, show_alert
from fman.fs import is_dir, iterdir
from fman.url import join

class JavaPackagesNavigation(DirectoryPaneListener):
	def on_command(self, command_name, args):
		if command_name == 'open_directory':
			realUrl = args['url']
			url = getURL(realUrl)
			if url != realUrl:
				return command_name, {'url': url}

def getURL(url):
	files = list(iterdir(url))
	if len(files) == 1:
		newUrl = join(url, files[0])
		if is_dir(newUrl):
			url = getURL(newUrl)
	return url