from abc import ABC, abstractmethod

class InputBus(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class SpatialData(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class VideoFrames(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class Audio(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class SceneState(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class SceneSimulator(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class ShortTermMemory(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class Judge(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class AcceptedOut(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class OutputGenerators(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass

class OutputBus(ABC):
@abstractmethod
def getData(self):
pass
def putData(self):
pass