 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
                    ©Copyright
     	CTFR - Sheila A. Berta (UnaPibaGeek)
             Personalizada por @Ux4hack
-----------------------------------------------------
"""
import re
import requests

version = 1.2

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="Target domain.")
	parser.add_argument('-o', '--output', type=str, help="Output file.")
	return parser.parse_args()

def banner():
	global version
	b = '''
	'''.format(v=version)
	print(b)
	
def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

def main():
#	banner()
	args = parse_args()

	subdomains = []
	target = clear_url(args.domain)
	output = args.output

	req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

	if req.status_code != 200:
		print("\033[1;31m  ERROR:\033[92m Información no disponible!") 
		exit(1)

	for (key,value) in enumerate(req.json()):
		subdomains.append(value['name_value'])

	
	print("\n\033[1;31m[!] ---- OBJETIVO:\033[97m {d} \033[1;31m ---- [!] \n".format(d=target))

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("\033[92m[\033[1;31m-\033[92m] \033[97m' {s}\033[97m'".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

	print("\n\n \033[1;31m[!] \033[33m Dtve_Web by Ux4hack...")


main()

