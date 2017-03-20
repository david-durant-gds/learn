class Bus_Company:
    """Bus_Company class"""

    # READ THIS - IMPORTANT
    """
    Elements outside the __init__ method are static elements.
    It means, they belong to the class.
    Elements inside the __init__ method are elements of the object (self)
    They don't belong to the class.
    """

    #LIST OF BUSSES TO BE ADDED

    #this is the constructor
    def __init__(self):
      self.company_name = ""
      self.company_manager = ""

      # EXAMPLE (TO BE REMOVED) OF HOW TO MAKE A LINK TO ANOTHER OBJECT INSTANCE
      self.example_bus = Bus()

    #this is the getter function for company name
    def get_company_name(self):
      return self.company_name

    #this is te setter function for compamny name
    def set_company_name(self, new_name_company):
      self.company_name = new_name_company

    #this is the getter function for company manager
    def get_company_manager(self):
      return self.company_manager

    #this is te setter function for compamny manager
    def set_company_manager(self, new_name_manager):
      self.company_manager = new_name_manager

class Bus:
    """Bus class"""
    #missing bus route which is an instance of route

    #this is the constructor
    def __init__(self):
      self.bus_number = ""
      self.bus_driver = ""

    #this is the getter function for bus_number
    def get_bus_number(self):
      return self.bus_number

    #this is te setter function for bus_number
    def set_bus_number(self, new_bus_number):
      self.bus_number = new_bus_number

    #this is the getter function for bus_driver
    def get_bus_driver(self):
      return self.bus_driver

    #this is te setter function for bus_driver
    def set_bus_driver(self, new_bus_driver):
      self.bus_driver = new_bus_driver

class Route:
    """route class"""
    #missing list of stops
    route_name = ""
    route_start_time = ""
    route_end_time = ""

    #this is the constructor
    def __init__(self):
        pass

    #this is the getter function for route name
    def get_route_name(self):
     return route_name

    #this is te setter function for route name
    def set_route_name(self, new_route_name):
     route_name = new_route_name

    #this is the getter function for route_start_time
    def get_route_start_time(self):
      return route_start_time

    #this is te setter function for route_start_time
    def set_route_start_time(self, new_route_start_time):
     route_start_time = new_route_start_time

     #this is the getter function for route_nd_time
     def get_route_end_time(self):
       return route_end_time

     #this is te setter function for route_end_time
     def set_route_end_time(self, new_route_end_time):
      route_end_time = new_route_end_time

class Stop:
    """Bus_Company class"""

    #dictionary of times to other stops
    stop_name= ""

    #this is the constructor
    def __init__(self):
        pass

    #this is the getter function for stop name
    def get_stop_name(self):
     return stop_name

    #this is te setter function for stop name
    def set_stop_name(self, new_stop_name):
     stop_name = new_stop_name
