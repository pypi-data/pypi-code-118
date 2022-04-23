import pathlib
import setuptools

HERE=pathlib.Path(__file__).parent

README=(HERE / 'README.md').read_text()

setuptools.setup(
	name='CapiPy',
	version='1.0.42',
	author='David Roura Padrosa', 
	author_email='davidrourap@gmail.com',
	description='Computer assistance for protein immobilization with Python',
	long_description=README,
	long_description_content_type='text/markdown',
	url='https://github.com/drou0302/CapiPy',
	packages=['CapiPy'],
	package_data={'CapiPy':['ncfiles/*.png', 'ncfiles/*.cfg', 'utils/*.py']},
	install_requires=['PySimpleGUI', 'numpy', 'BioPython'],
	include_package_data=True,
	include_package_date=True, 
	zip_safe=False,
	classifiers=[
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 
		'Operating System :: OS Independent']
)
