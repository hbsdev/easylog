# Easylog

A thin convenience wrapper for very basic logger uses. Leaves the unnamed root logger alone and creates only named loggers.

This is a very small wrapper to create logger instances  for the python logging module from the standard library (https://docs.python.org/3.4/library/logging.html), see https://github.com/hbsdev/easylog/blob/master/doc/standard-library-logging-module.md

#### How to use this module

Currently only 2 handlers are supported. If you supply the path variable on creation,
a file logger ist created. If not, a console logger.

Loggers need always to be namend and are global to the current python process.

The loggers returned are from the standard library, so you are still able to do
anything with them that the logging module allows and mix freely.

#### Example

1) A console logger:

    >>> import easylog
    >>> log_c = easylog.create("logger2","DEBUG")
    >>> log_c.info("Logging on the console")

2) A file logger:

    >>> import easylog
    >>> log = easylog.create("file_logger","DEBUG",path="log/debuglog.txt")

3) Use it

    >>> log.info("This is an info message")

4) Use it when already initialized elsewhere:

    >>> # Assuming this is another file we are in now:
    >>> import easylog
    >>> log = easylog.get("logger_name") # must have been Initialized before!
    >>> log.info("This also goes to log/debuglog.txt")

#### Installation

To install the latest version:

    pip install https://github.com/hbsdev/easylog/archive/master.zip#egg=easylog --upgrade

You can now `import easylog` like in the examples.

