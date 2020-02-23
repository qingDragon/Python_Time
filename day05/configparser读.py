import configparser

conf = configparser.ConfigParser()
conf.read("ha.conf")


print(conf.defaults())
print(conf.sections())

print(conf['bitbucket.org']['user'])