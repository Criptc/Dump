from rsa.prime import is_prime
import threading
from time import sleep
import time
from os import system

ps = []
qs = []
total_primes = 0

def find_p_primes():
	global ps
	p_primes = []
	for i in range(int('1' + '0' * 163), int('1' + '0' * 164)-1):  # yes, very inefficent, I know
		if is_prime(i):
			global total_primes
			total_primes += 1
			print(f'prime found! {i}\ntotal primes: {total_primes}\n\n')
			p_primes.append(i)
	ps = p_primes
	
def find_q_primes():
	global qs, total_primes
	q_primes = []
	for i in range(int('1' + '0' * 144), int('1' + '0' * 145)-1):
		if is_prime(i):
			global total_primes
			total_primes += 1
			print(f'prime found! {i}\ntotal primes: {total_primes}\n\n')
			q_primes.append(i)
	qs = q_primes

prime_pairs = []

sleep(0.2)
system('clear')
print('finding primes...\n\n')

p_thread = threading.Thread(target=find_p_primes)
q_thread = threading.Thread(target=find_q_primes)

start = time.time()
p_thread.start()
q_thread.start()

q_thread.join()
q_end = time.time()
print(f'all possible q primes found!\n\t\tprimes: {len(qs)}\n\ttime (sec): {q_end - start}\n\n')
sleep(0.2)
p_thread.join()
p_end = time.time()
print(f'all possible p primes found!\n\t\tprimes: {len(ps)}\n\ttime (sec): {p_end - start}\n\n')
sleep(0.2)


with open('p_primes.txt', 'w') as pfile:
	pfile.write('[\n\t')
	for i in ps:
		pfile.write("{" + i + "},\n\t")
	pfile.write('{}\n]')

with open('q_primes.txt', 'w') as qfile:
	qfile.write('[\n\t')
	for i in qs:
		qfile.write("{" + i + "},\n\t")
	qfile.write('{}\n]')

print('\nprimes written to files succsessfully')
