skeleton-python
===============

Downloading
-----------

check out this sample codes::

  $ git clone https://github.com/MiCHiLU/skeleton-python.git

and move into the skeleton-python directory::

  $ cd skeleton-python

Installing tools
----------------

Installing Ruby Gemfile::

  $ gem install bundler
  $ bundle install

Installing Node.js package.json::

  $ curl http://npmjs.org/install.sh | sudo sh
  $ npm install

Making virtualenv for Python::

  $ mkvirtualenv --python=`which python3.3` skeleton-python
  (skeleton-python)$

Installing pip requirements into the Python virtualenv::

  (skeleton-python)$ pip install -r requirements/base.txt
