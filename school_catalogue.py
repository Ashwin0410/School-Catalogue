class School:
  def __init__(self,name,level,numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents
  def getname(self):
    return self._name
  def getlevel(self):
    return self._level
  def getnumberOfStudents(self):
    return self._numberOfStudents    
  def setnumberOfStudents(self,n):
    self._numberOfStudents = n
  def __repr__(self):
    return f"A {self._level} school named {self._name} with {self._numberOfStudents} students"
s = School("DAV","Middle",250)
print(s)  
print(s.getname())
print(s.getlevel())
print(s.getnumberOfStudents())
s.setnumberOfStudents(100)
print(s.getnumberOfStudents())
print(s)

class PrimarySchool(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,"Primary",numberOfStudents)
    self._pickupPolicy = pickupPolicy
  @property
  def pickupPolicy(self):
    return self._pickupPolicy
  def __repr__(self):
    return f"{super().__repr__()} and Pickup Policy is {self._pickupPolicy}"

# ps = PrimarySchool("UoL",250,"Pickup at 3.00PM")
# print(ps)

class HighSchool(School):
  def __init__(self,name,numberOfStudents,sportsTeams):
    super().__init__(name,"High",numberOfStudents)
    self._sportsTeams = sportsTeams
  
  
  @property
  def sportsTeams(self):
    return self._sportsTeams
  def __repr__(self):
    return f"{super().__repr__()} and information about sports team is {self._sportsTeams}"
  
hs = HighSchool("UoL","1000","Cricket and TT")
print(hs)
  
    
    
