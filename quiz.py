from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdA9ZAFtzrCEd4L9BQ0TrseGuugk1d40_vDcafKwhfjCwEchwIJl0kr-wCp0Qk7ElOHwZeJmDu-HjwUR0eXOE5Qtgj1hLGrYe74TqAozevU-GbkLc5hOgmhr58qTetUCQanVScV-wSqiiybhMyO_XBs8UO6BpzPJAcJyPbzYiRQQrl-9I='
f = Fernet(key)
print(f.decrypt(message))