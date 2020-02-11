from setuptools import setup

setup(

	name='snapshotalyzer-100',
	version='0.1',
	author="Ronald Guthrie",
	author_email="ronald.guthrie@digitaldefense.com",
	description="Snapshotalyzer 100 is a tool to manage AWS EC2 snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="https://github.com/ron-at-ddi/snapshotalyzer-100",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
	
)
