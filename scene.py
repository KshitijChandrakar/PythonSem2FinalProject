from MyFunctions import EmptyFunction
'''
Scene is a subset of Environment



'''

class scene():

    def handleExp(self, E):
        # print("Error =", type(E))
        # print(self.excep)
        # pas
        try:
            self.excep[E][0](self.excep[E][1])
        except KeyError:
            pass
        pass
    def initialise(self):
        try:
            for i in self.initialise1:
                i()
        except TypeError:
            pass
    def __init__(self, renderFunction, event = None, excep = None, eventFunction = None, initialise=None, uninitialse=None):
        self.initialise1 = initialise

        self.Initialised = 0

        self.uninitialse = uninitialse
        self.renderFunction = renderFunction
        self.events = event #events = {eventType: what To do in case of event}
        self.excep = excep #Exceptions that scens raise
        self.eventFunction = eventFunction #A function to call with event as the parameter
    def render(self):
        self.renderFunction()
        pass
    def handleEvent(self, event):
        try:

            self.events[event][0](self.events[event][1])
            pass
        except KeyError:
            #print("Oops", currentScene)
            pass
        pass
    pass
