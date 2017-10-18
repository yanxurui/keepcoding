def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class MyClass():
  pass


if __name__ == '__main__':
    m = MyClass()
    n = MyClass()
    print(type(m))
    print(m==n)