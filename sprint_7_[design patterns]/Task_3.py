"""Imagine you are creating an application that shows the data about all different types of vehicles present. It takes the data from APIs of different vehicle organizations in XML format and then displays the information.
But suppose at some time you want to upgrade your application with a Machine Learning algorithms that work beautifully on the data and fetch the important data only. But there is a problem, it takes data in JSON format only.
It will be a really poor approach to make changes in Machine Learning Algorithm so that it will take data in XML format.

For solving the problem we defined above, you can use Adapter Method that helps by creating an Adapter object.
To use an adapter in your code:

Client should make a request to the adapter by calling a method on it using the target interface.
Using the Adaptee interface, the Adapter should translate that request on the adaptee.
Result of the call is received the client and he/she is unaware of the presence of the Adapter’s presence."""


class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self._object = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self._object, attr)

    def original_dict(self):
        return self.__dict__






