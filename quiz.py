from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc9OjEBCuTDJGNyNYGnmi2AmiwqBmQ3Yhvh4xhGZukqjmcC0WH9jtlcOcDoaCg8LduDD3vC0IvhCdF4GAZ9L9O_34kxYe9ygK8Q9vEtRK5JqNCw_gQ1Qn7kNJw85jZ5MIbJMcyk-Ztx8r3UYN67yl1jPW31SyGdCoDdDM-BKmgMmSTtBo='
f = Fernet(key)
print(f.decrypt(message))