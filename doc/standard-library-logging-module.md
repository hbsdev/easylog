# The Python logging module

Part of the standard library, available for python 3.x, logfile rotation

* 3.4 Basic-tutorial: https://docs.python.org/3.4/howto/logging.html#logging-basic-tutorial
* 3.4 Advanced tutorial: https://docs.python.org/3.4/howto/logging.html#logging-advanced-tutorial
* 3.4 Cookbook: https://docs.python.org/3.4/howto/logging-cookbook.html#logging-cookbook

#### Alternatives

* There is the warnings module which is built into python, see at the bottom of this page
* Logbook has a basic interface similar to the logging module: http://pythonhosted.org/Logbook/
* For python 2.x there is twiggy, https://twiggy.readthedocs.org/en/latest/ and https://github.com/wearpants/twiggy

### Basic concepts

The logging module from the python standard library provides so called "loggers". Loggers are organized in a tree-like hierarchy.

- There is always the unnamed root logger.
- All other loggers are named loggers and are descendants of the root logger.
- Each logger passes log messages on to its parents, and each parent gets the chance to process the message
- So no matter what you do, all messages will eventually reach the root logger

## Loggers are globally shared and identified by their name

New loggers are created with the getLogger() function. For example

   s1 = logging.getLogger('mylog1.sub1')

creates a logger sub1 which is a child of mylog1 which itself is a child of the (unnamed) root logger. When logging to the s1 logger, it will pass on the message to its parent, and its parent will pass the message to the root logger. So 3 loggers get a chance to process the message: mylog1.sub1, mylog and also the root logger.

## Logging to a file

You can configure a logger to log to a file using the basicConfig() function

   logging.basicConfig(filename='debuglog.txt',level=logging.DEBUG, name='debug0')


## The warnings module

* There is the warnings module which is built into python and used internally but can also by used from your code.

Should be used in library code if the issue is avoidable and the client application should be modified to eliminate the warning:

      warnings.warn()

## All loggers are global

Because the loggers are global to the current python process, it is always possible that another
module is configuring the same logger before or after you do it. If the unnamed root logger this is
minimized, because named loggers are easier to distinguish.

## Configuration can be difficult after first use

If the root logger is used without configuring it first, a standard configuration is applied to it,
so it can work out of the box. But after that it would be necesary to remove all handlers from the root logger
to be able to configure it from the start.

---

Markdown editor: http://dillinger.io/