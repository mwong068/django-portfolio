from projects.lists import Projects
import pytest

@pytest.fixture
def project():
  return Projects

def test_constructor():
  a = Projects()
  assert isinstance(a, Projects)
  assert len(a) == 0

def test_push(project):
  project.push(3)
  assert len(project) == 1
  project.push(5)
  assert len(project) == 2

def test_pop(project):
  stack.push('hello')
  stack.push('goodbye')
  assert stack.pop() == "goodbye"
  assert stack.pop() == "hello"