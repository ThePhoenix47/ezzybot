from setuptools import setup, find_packages

#Don't actually use this ATM, this is only so I can keep track of install requires


setup(name='ezzybot',
      version='0.0.1',
      description="Python IRC framework",
      url='',
      author='EzzyBot team',
      author_email='me@lukej.me',
      license='GNU',
      packages=find_packages(),
      install_requires=['thingdb'],
      include_package_data=True,
      zip_safe=False)