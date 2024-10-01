from setuptools import setup, find_packages

setup(
    name='password_strength_tool',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'check_password=password_strength.strength_checker:main',
        ],
    },
    description='A tool to assess the strength of a password',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/password_strength_tool',  # Update with your repo link
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
install_requires=[
    'tkinter',  # Note: Tkinter is usually included with Python    
],
