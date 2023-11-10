from project import *

def main():
    test_inserttask()
    test_deletetask()
    test_viewAllTasks()
    test_marktaskcompleted()
    test_viewAllPendingTasks()
    test_viewAllCompletedTasks()

def test_inserttask():
    first = None
    first = inserttask("Complete udemy course" , first)
    assert first is not None
    first = inserttask("Stay Hydrated" , first)
    assert first is not None

def test_deletetask():
    first = inserttask("cs50" , None)
    first = deletetask("cs50" , first)
    assert first == None
    first = inserttask("freecodecamp" , first)
    first = inserttask("odin Project" , first)
    first = deletetask("Odin Project" , first)
    assert first is not None
    first = deletetask("free" , first)
    assert first is not None
    first = deletetask("freecodecamp" , first)
    assert first is None


def test_viewAllTasks():
    first = None
    assert viewAllTasks(first) == None
    first = inserttask("Eat Well" , first)
    assert viewAllTasks(first) == ['1.Eat Well | Status : P']


def test_marktaskcompleted():
    first = None
    first = marktaskcompleted("Training Session" , first)
    assert first == None
    first = inserttask("Training Session" , first)
    first = marktaskcompleted("Training Sessio" , first)
    assert first is not None
    first = marktaskcompleted("Training Session" , first)
    assert first is not None

def test_viewAllPendingTasks():
    first = None
    PendingTasks = viewAllPendingTasks(first)
    assert PendingTasks == None
    first = inserttask("Nodejs Basics" , first)
    first = inserttask("learn react Basics " , first)
    PendingTasks = viewAllPendingTasks(first)
    assert PendingTasks == ['1.learn react Basics ','2.Nodejs Basics' , ]
    first = marktaskcompleted("Nodejs Basics" , first)
    PendingTasks = viewAllPendingTasks(first)
    assert PendingTasks == ["1.learn react Basics "]

def test_viewAllCompletedTasks():
    first = None
    CompletedTasks = viewAllCompletedTasks(first)
    assert CompletedTasks == None
    first = inserttask("Nodejs Basics" , first)
    first = inserttask("learn react Basics " , first)
    CompletedTasks = viewAllCompletedTasks(first)
    assert CompletedTasks == []
    first = marktaskcompleted("Nodejs Basics" , first)
    CompletedTasks = viewAllCompletedTasks(first)
    assert CompletedTasks == ["1.Nodejs Basics"]

main()



