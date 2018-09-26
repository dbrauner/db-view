import os
import sys

suffix = ''
sub = "nfe-status-service"

if len(sys.argv) > 1:
    suffix = str(sys.argv[1])
    sub += '-' + suffix
    os.popen('cf_login_' + suffix).read()
o = os.popen('cf a').read()

lines = o.split('\n')


status_service = next((s for s in lines if sub in s), None)

service_name = status_service.split()[0]

service_env = os.popen('cf env ' + service_name).read()

service_env_trim = service_env.split("\n", 4)[4]


lines = service_env_trim.split('\n')

dbname = next((s for s in lines if 'dbname' in s), None)
print(dbname)

username = next((s for s in lines if 'username' in s), None)
print(username)

password = next((s for s in lines if 'password' in s), None)
print(password)
