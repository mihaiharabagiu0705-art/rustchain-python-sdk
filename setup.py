from setuptools import setup, find_packages
setup(name='rustchain-sdk', version='0.1.0', packages=find_packages(), install_requires=['httpx>=0.24.0'], author='Antigravity AI', description='Python SDK for RustChain', long_description=open('README.md').read(), long_description_content_type='text/markdown')
