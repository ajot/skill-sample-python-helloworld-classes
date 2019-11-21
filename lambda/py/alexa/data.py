from gettext import gettext as _

# To access these in hello_world.py, do the following
# import gettext
# from alexa import data
# speak_output = _(data.WELCOME_MESSAGE)

WELCOME_MESSAGE = _(
    "Welcome, you can say Hello or Help. Which would you like to try?")
HELLO_MSG = _("Hello Python World from Classes!")
HELP_MSG = _("You can say hello to me! How can I help?")
GOODBYE_MSG = _("Goodbye!")
REFLECTOR_MSG = _("You just triggered {}")
ERROR = _("Sorry, I had trouble doing what you asked. Please try again.")
