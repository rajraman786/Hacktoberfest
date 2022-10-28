import sys
import argparse
import subprocess
import os
import time
import random
import threading
import re
import random
from urllib.parse import urlsplit



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BADFAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BG_ERR_TXT  = '\033[41m' # For critical errors and crashes
    BG_HEAD_TXT = '\033[100m'
    BG_ENDL_TXT = '\033[46m'
    BG_CRIT_TXT = '\033[45m'
    BG_HIGH_TXT = '\033[41m'
    BG_MED_TXT  = '\033[43m'
    BG_LOW_TXT  = '\033[44m'
    BG_INFO_TXT = '\033[42m'

    BG_SCAN_TXT_START = '\x1b[6;30;42m'
    BG_SCAN_TXT_END   = '\x1b[0m'
# Legends
proc_high = bcolors.BADFAIL + "●" + bcolors.ENDC
proc_med  = bcolors.WARNING + "●" + bcolors.ENDC
proc_low  = bcolors.OKGREEN + "●" + bcolors.ENDC
def vul_info(val):
    result =''
    if val == 'c':
        result = bcolors.BG_CRIT_TXT+" critical "+bcolors.ENDC
    elif val == 'h':
        result = bcolors.BG_HIGH_TXT+" high "+bcolors.ENDC
    elif val == 'm':
        result = bcolors.BG_MED_TXT+" medium "+bcolors.ENDC
    elif val == 'l':
        result = bcolors.BG_LOW_TXT+" low "+bcolors.ENDC
    else:
        result = bcolors.BG_INFO_TXT+" info "+bcolors.ENDC
    return result

def vul_remed_info(v1,v2,v3):
    print(bcolors.BOLD+"Vulnerability Threat Level"+bcolors.ENDC)
    print("\t"+vul_info(v2)+" "+bcolors.WARNING+str(tool_resp[v1][0])+bcolors.ENDC)
    print(bcolors.BOLD+"Vulnerability Definition"+bcolors.ENDC)
    print(v3)
    print("\t"+bcolors.BADFAIL+str(tools_fix[v3-1][1])+bcolors.ENDC)
    print(bcolors.BOLD+"Vulnerability Remediation"+bcolors.ENDC)
    print("\t"+bcolors.OKGREEN+str(tools_fix[v3-1][2])+bcolors.ENDC)



def helper():
        print("\033[33mInformation:")
        print("------------")
        print("\t./vf.py example.com: Scans the domain example.com.")     
        print("\t./vf.py --help     : Displays this help context.")
        print("\033[33mInteractive:")
        print("------------")
        print("\tCtrl+C: Skips current test.")
        print("\tCtrl+Z: Quits Scanning.")

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'

# Scan Time Elapser
intervals = (
    ('h', 3600),
    ('m', 60),
    ('s', 1),
    )
def display_time(seconds, granularity=3):
    result = []
    seconds = seconds + 1
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append("{}{}".format(value, name))
    return ' '.join(result[:granularity])


def terminal_size():
    try:
        rows, columns = subprocess.check_output(['stty', 'size']).split()
        return int(columns)
    except subprocess.CalledProcessError as e:
        return int(20)
       
def url_maker(url):
    if not re.match(r'http(s?)\:', url):
        url = 'http://' + url
    parsed = urlsplit(url)
    host = parsed.netloc
    if host.startswith('www.'):
        host = host[4:]
    return host
    
def clear():
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K") #clears until EOL

def logo():

    logo="""\033[31m
                     ▌ ▐·▄• ▄▌▄▄▌   ▐ ▄       ▄▄▄ ▪   ▐ ▄ ·▄▄▄▄    ▄▄▄ .▄▄▄  
                    ▪█·█▌█▪██▌██•  •█▌▐█    ▐▄▄· ██ •█▌▐█ ██▪ ██  ▀▄.▀·▀▄ █·
                    ▐█▐█•█▌▐█▌██▪  ▐█▐▐▌    ██▪ ▐█· ▐█▐▐▌ ▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
                     ███ ▐█▄█▌▐█▌▐▌██▐█▌    ██▌.▐█▌ ██▐█▌ ██. ██ ▐█▄▄▌▐█•█▌
                    . ▀   ▀▀▀ .▀▀▀ ▀▀ █▪    ▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀▀▀•  ▀▀▀ .▀  ▀
                                   Let's SCAN Your WEB 


    """+'\033[31m'
    print(logo)
    print(f"                    \033[31m  VulN FindeR v1.0          \033[32m [Author: RAMAN RAJ | KUNAL KANOTRA ] [https://github.com/rajraman786]")    

    
class Spinner:
    busy = False
    delay = 0.005 # 0.05

    @staticmethod
    def spinning_cursor():
        while 1:
            #for cursor in '|/-\\/': yield cursor #←↑↓→
            #for cursor in '←↑↓→': yield cursor
            #for cursor in '....scanning...please..wait....': yield cursor
            for cursor in ' ': yield cursor
    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay
        self.disabled = False

    def spinner_task(self):
        inc = 0
        try:
            while self.busy:
                if not self.disabled:
                    x = bcolors.BG_SCAN_TXT_START+next(self.spinner_generator)+bcolors.BG_SCAN_TXT_END
                    inc = inc + 1
                    print(x,end='')
                    if inc>random.uniform(0,terminal_size()): #30 init
                        print(end="\r")
                        bcolors.BG_SCAN_TXT_START = '\x1b[6;30;'+str(round(random.uniform(40,47)))+'m'
                        inc = 0
                    sys.stdout.flush()
                time.sleep(self.delay)
                if not self.disabled:
                    sys.stdout.flush()

        except (KeyboardInterrupt, SystemExit):
            print("\n\t"+ bcolors.BG_ERR_TXT+"VulNFindeR received a series of Ctrl+C hits. Quitting..." +bcolors.ENDC)
            sys.exit(1)

    def start(self):
        self.busy = True
        try:
            threading.Thread(target=self.spinner_task).start()
        except Exception as e:
            print("\n")
        
    def stop(self):
        try:
            self.busy = False
            time.sleep(self.delay)
        except (KeyboardInterrupt, SystemExit):
            print("\n\t"+ bcolors.BG_ERR_TXT+"VulNFindeR received a series of Ctrl+C hits. Quitting..." +bcolors.ENDC)
            sys.exit(1)

# End ofloader/spinner class

# Instantiating the spinner/loader class
spinner = Spinner()
tool_names = [    #1
                ["host","Host - Checks for existence of IPV6 address.","host",1],
 #3
                ["wp_check","WordPress Checker - Checks for WordPress Installation.","wget",1],
                 #10
                ["dnsrecon","DNSRecon - Attempts Multiple Zone Transfers on Nameservers.","dnsrecon",1],
#13
                ["whois","WHOis - Checks for Administrator's Contact Information.","whois",1],
                #42
                ["nmap_telnet","Nmap [TELNET] - Checks if TELNET service is running.","nmap",1],

                #43
                ["nmap_ftp","Nmap [FTP] - Checks if FTP service is running.","nmap",1],
                #67
                ["nmap_sqlserver","Nmap - Checks for MS-SQL Server DB","nmap",1],

                #68
                ["nmap_mysql", "Nmap - Checks for MySQL DB","nmap",1],

                #69
                ["nmap_oracle", "Nmap - Checks for ORACLE DB","nmap",1],

                #70
                ["nmap_rdp_udp","Nmap - Checks for Remote Desktop Service over UDP","nmap",1],

                #71
                ["nmap_rdp_tcp","Nmap - Checks for Remote Desktop Service over TCP","nmap",1]
            ]

tool_cmd   = [

                #1
                ["host ",""],
                 #3
                ["wget -O /tmp/temp_wp_check --tries=1 ","/wp-admin"],
#10
                ["dnsrecon -d ",""],
                #13
                ["whois ",""],
                #42
                ["nmap -p23 --open -Pn ",""],

                #43
                ["nmap -p21 --open -Pn ",""],
                #67
                ["nmap -p1433 --open -Pn ",""],

                #68
                ["nmap -p3306 --open -Pn ",""],

                #69
                ["nmap -p1521 --open -Pn ",""],

                #70
                ["nmap -p3389 --open -sU -Pn ",""],

                #71
                ["nmap -p3389 --open -sT -Pn ",""]
                ]
tool_resp   = [
                #1
                ["Does not have an IPv6 Address. It is good to have one.","i",1],
 #3
                ["WordPress Installation Found. Check for vulnerabilities corresponds to that version.","i",2],
#10
                ["Zone Transfer Successful using DNSRecon. Reconfigure DNS immediately.","h",3],
 #13
                ["Whois Information Publicly Available.","i",4],
 #42
                ["Telnet Service Detected.","h",5],

                #43
                ["FTP Service Detected.","c",6],
                 #67
                ["MS-SQL DB Service Detected.","l",7],

                #68
                ["MySQL DB Service Detected.","l",7],

                #69
                ["ORACLE DB Service Detected.","l",7],

                #70
                ["RDP Server Detected over UDP.","h",8],

                #71
                ["RDP Server Detected over TCP.","h",8]
]
tool_status = [
                #1
                ["has IPv6",1,proc_low," < 15s","ipv6",["not found","has IPv6"]],
 #3
                ["wp-login",0,proc_low," < 30s","wpcheck",["unable to resolve host address","Connection timed out"]],
  #10
                ["[+] Zone Transfer was successful!!",0,proc_low," < 20s","dnsreconzt",["Could not resolve domain"]],
#13
                ["Admin Email:",0,proc_low," < 25s","whois",["No match for domain"]],
 #42
                ["open",0,proc_low," < 15s","nmaptelnet",["Failed to resolve"]],

                #43
                ["open",0,proc_low," < 15s","nmapftp",["Failed to resolve"]],
#67
                ["open",0,proc_low," < 15s","nmapmssql",["Failed to resolve"]],

                #68
                ["open",0,proc_low," < 15s","nmapmysql",["Failed to resolve"]],

                #69
                ["open",0,proc_low," < 15s","nmaporacle",["Failed to resolve"]],

                #70
                ["open",0,proc_low," < 15s","nmapudprdp",["Failed to resolve"]],

                #71
                ["open",0,proc_low," < 15s","nmaptcprdp",["Failed to resolve"]]
]
tools_fix = [
                    [1, "Not a vulnerability, just an informational alert. The host does not have IPv6 support. IPv6 provides more security as IPSec (responsible for CIA - Confidentiality, Integrity and Availablity) is incorporated into this model. So it is good to have IPv6 Support.",
                            "It is recommended to implement IPv6. More information on how to implement IPv6 can be found from this resource. https://www.cisco.com/c/en/us/solutions/collateral/enterprise/cisco-on-cisco/IPv6-Implementation_CS.html"],
                   [3, "It is not bad to have a CMS in WordPress. There are chances that the version may contain vulnerabilities or any third party scripts associated with it may possess vulnerabilities",
                            "It is recommended to conceal the version of WordPress. This resource contains more information on how to secure your WordPress Blog. https://codex.wordpress.org/Hardening_WordPress"],
                             [10, "Zone Transfer reveals critical topological information about the target. The attacker will be able to query all records and will have more or less complete knowledge about your host.",
                            "Good practice is to restrict the Zone Transfer by telling the Master which are the IPs of the slaves that can be given access for the query. This SANS resource  provides more information. https://www.sans.org/reading-room/whitepapers/dns/securing-dns-zone-transfer-868"],
                     [13, "This attack works by opening multiple simultaneous connections to the web server and it keeps them alive as long as possible by continously sending partial HTTP requests, which never gets completed. They easily slip through IDS by sending partial requests.",
                            "If you are using Apache Module, `mod_antiloris` would help. For other setup you can find more detailed remediation on this resource. https://www.acunetix.com/blog/articles/slow-http-dos-attacks-mitigate-apache-http-server/"],
                    [32, "Through this deprecated protocol, an attacker may be able to perform MiTM and other complicated attacks.",
                            "It is highly recommended to stop using this service and it is far outdated. SSH can be used to replace TELNET. For more information, check this resource https://www.ssh.com/ssh/telnet"],
                    [33, "This protocol does not support secure communication and there are likely high chances for the attacker to eavesdrop the communication. Also, many FTP programs have exploits available in the web such that an attacker can directly crash the application or either get a SHELL access to that target.",
                            "Proper suggested fix is use an SSH protocol instead of FTP. It supports secure communication and chances for MiTM attacks are quite rare."],
                    [47, "Since the attacker has knowledge about the particular type of backend the target is running, they will be able to launch a targetted exploit for the particular version. They may also try to authenticate with default credentials to get themselves through.",
                            "Timely security patches for the backend has to be installed. Default credentials has to be changed. If possible, the banner information can be changed to mislead the attacker. The following resource gives more information on how to secure your backend. http://kb.bodhost.com/secure-database-server/"],
                    [48, "Attackers may launch remote exploits to either crash the service or tools like ncrack to try brute-forcing the password on the target.",
                            "It is recommended to block the service to outside world and made the service accessible only through the a set of allowed IPs only really neccessary. The following resource provides insights on the risks and as well as the steps to block the service. https://www.perspectiverisk.com/remote-desktop-service-vulnerabilities/"]
]
tools_precheck = [
                    ["wapiti"], ["whatweb"], ["nmap"], ["golismero"], ["host"], ["wget"], ["uniscan"], ["wafw00f"], ["dirb"], ["davtest"], ["theHarvester"], ["xsser"], ["dnsrecon"],["fierce"], ["dnswalk"], ["whois"], ["sslyze"], ["lbd"], ["golismero"], ["dnsenum"],["dmitry"], ["davtest"], ["nikto"], ["dnsmap"], ["amass"]
                 ]

def get_parser():

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true', 
                        help='Show help message and exit.')
    parser.add_argument('-u', '--update', action='store_true', 
                        help='Update VulNFindeR.')
    parser.add_argument('-s', '--skip', action='append', default=[],
                        help='Skip some tools', choices=[t[0] for t in tools_precheck])
    parser.add_argument('-n', '--nospinner', action='store_true', 
                        help='Disable the idle loader/spinner.')
    parser.add_argument('target', nargs='?', metavar='URL', help='URL to scan.', default='', type=str)
    return parser

tool_checks = (len(tool_names) + len(tool_resp) + len(tool_status)) / 3 # Cross verification incase, breaks.
tool_checks = round(tool_checks)

# Tool Head Pointer: (can be increased but certain tools will be skipped)
tool = 0

# Run Test
runTest = 1

# For accessing list/dictionary elements
arg1 = 0
arg2 = 1
arg3 = 2
arg4 = 3
arg5 = 4
arg6 = 5

# Detected Vulnerabilities [will be dynamically populated]
xp_vul_list = list()
xp_vul_num = 0
xp_vul = 0

# Total Time Elapsed
xp_total_elapsed = 0

# Tool Pre Checker
xp_avail_tools = 0

# Checks Skipped
xp_skipped_checks = 0

if len(sys.argv) == 1:
    logo()
    helper()
    sys.exit(1)

args_namespace = get_parser().parse_args()
if args_namespace.help or (not args_namespace.update \
    and not args_namespace.target):
    logo()
    helper()
elif args_namespace.target:

    target = url_maker(args_namespace.target)
    #target = args_namespace.target
    os.system('rm /tmp/te* > /dev/null 2>&1') # Clearing previous scan files
    os.system('clear')
    os.system('setterm -cursor off')
    logo()
    print(bcolors.BG_HEAD_TXT+"[ Checking Available Security Scanning Tools Phase... Initiated. ]"+bcolors.ENDC)

    unavail_tools_names = list()

    while (xp_avail_tools < len(tools_precheck)):
        precmd = str(tools_precheck[xp_avail_tools][arg1])
        try:
            p = subprocess.Popen([precmd], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
            output, err = p.communicate()
            val = output + err
        except:
            print("\t"+bcolors.BG_ERR_TXT+"VulNFindeR was terminated abruptly..."+bcolors.ENDC)
            sys.exit(1)
        
        # If the tool is not found or it's part of the --skip argument(s), disabling it
        if b"not found" in val or tools_precheck[xp_avail_tools][arg1] in args_namespace.skip :
            if b"not found" in val:
                print("\t"+bcolors.OKBLUE+tools_precheck[xp_avail_tools][arg1]+bcolors.ENDC+bcolors.BADFAIL+"...unavailable."+bcolors.ENDC)
            elif tools_precheck[xp_avail_tools][arg1] in args_namespace.skip :
                print("\t"+bcolors.OKBLUE+tools_precheck[xp_avail_tools][arg1]+bcolors.ENDC+bcolors.BADFAIL+"...skipped."+bcolors.ENDC)
            
            for scanner_index, scanner_val in enumerate(tool_names):
                if scanner_val[2] == tools_precheck[xp_avail_tools][arg1]:
                    scanner_val[3] = 0 # disabling scanner as it's not available.
                    unavail_tools_names.append(tools_precheck[xp_avail_tools][arg1])

        else:
            print("\t"+bcolors.OKBLUE+tools_precheck[xp_avail_tools][arg1]+bcolors.ENDC+bcolors.OKGREEN+"...available."+bcolors.ENDC)
        xp_avail_tools = xp_avail_tools + 1
        clear()
    unavail_tools_names = list(set(unavail_tools_names))
    if len(unavail_tools_names) == 0:
        print("\t"+bcolors.OKGREEN+"All Scanning Tools are available. Complete vulnerability checks will be performed by VulNFindeR."+bcolors.ENDC)
    else:
        print("\t"+bcolors.WARNING+"Some of these tools "+bcolors.BADFAIL+str(unavail_tools_names)+bcolors.ENDC+bcolors.WARNING+" are unavailable or will be skipped. VulNFindeR will still perform the rest of the tests. Install these tools to fully utilize the functionality of VulNFindeR."+bcolors.ENDC)
    print(bcolors.BG_ENDL_TXT+"[ Checking Available Security Scanning Tools Phase... Completed. ]"+bcolors.ENDC)
    print("\n")
    print(bcolors.BG_HEAD_TXT+"[ Preliminary Scan Phase Initiated... Loaded "+str(tool_checks)+" vulnerability checks. ]"+bcolors.ENDC)
    #while (tool < 1):
    while(tool < len(tool_names)):
        print("["+tool_status[tool][arg3]+tool_status[tool][arg4]+"] Deploying "+str(tool+1)+"/"+str(tool_checks)+" | "+bcolors.OKBLUE+tool_names[tool][arg2]+bcolors.ENDC,)
        if tool_names[tool][arg4] == 0:
            print(bcolors.WARNING+"\nScanning Tool Unavailable. Skipping Test...\n"+bcolors.ENDC)
            xp_skipped_checks = xp_skipped_checks + 1
            tool = tool + 1
            continue
        try:
            spinner.start()
        except Exception as e:
            print("\n")
        scan_start = time.time()
        temp_file = "/tmp/temp_"+tool_names[tool][arg1]
        cmd = tool_cmd[tool][arg1]+target+tool_cmd[tool][arg2]+" > "+temp_file+" 2>&1"

        try:
            subprocess.check_output(cmd, shell=True)
        except KeyboardInterrupt:
            runTest = 0
        except:
            runTest = 1

        if runTest == 1:
                spinner.stop()
                scan_stop = time.time()
                elapsed = scan_stop - scan_start
                xp_total_elapsed = xp_total_elapsed + elapsed
                #print(bcolors.OKBLUE+"\b...Completed in "+display_time(int(elapsed))+bcolors.ENDC+"\n")
                sys.stdout.write(ERASE_LINE)
                print(bcolors.OKBLUE+"\nScan Completed in "+display_time(int(elapsed))+bcolors.ENDC, end='\r', flush=True)
                print("\n")
                #clear()
                xp_tool_output_file = open(temp_file).read()
                if tool_status[tool][arg2] == 0:
                    if tool_status[tool][arg1].lower() in xp_tool_output_file.lower():
                        #print "\t"+ vul_info(tool_resp[tool][arg2]) + bcolors.BADFAIL +" "+ tool_resp[tool][arg1] + bcolors.ENDC
                        vul_remed_info(tool,tool_resp[tool][arg2],tool_resp[tool][arg3])
                        xp_vul_list.append(tool_names[tool][arg1]+"*"+tool_names[tool][arg2])
                else:
                    if any(i in xp_tool_output_file for i in tool_status[tool][arg6]):
                        m = 1 # This does nothing.
                    else:
                        #print "\t"+ vul_info(tool_resp[tool][arg2]) + bcolors.BADFAIL +" "+ tool_resp[tool][arg1] + bcolors.ENDC
                        vul_remed_info(tool,tool_resp[tool][arg2],tool_resp[tool][arg3])
                        xp_vul_list.append(tool_names[tool][arg1]+"*"+tool_names[tool][arg2])
        else:
                runTest = 1
                spinner.stop()
                scan_stop = time.time()
                elapsed = scan_stop - scan_start
                xp_total_elapsed = xp_total_elapsed + elapsed
                #sys.stdout.write(CURSOR_UP_ONE) 
                sys.stdout.write(ERASE_LINE)
                #print("-" * terminal_size(), end='\r', flush=True)
                print(bcolors.OKBLUE+"\nScan Interrupted in "+display_time(int(elapsed))+bcolors.ENDC, end='\r', flush=True)
                print("\n"+bcolors.WARNING + "\tTest Skipped. Performing Next. Press Ctrl+Z to Quit VulNFindeR.\n" + bcolors.ENDC)
                xp_skipped_checks = xp_skipped_checks + 1

        tool=tool+1

    print(bcolors.BG_ENDL_TXT+"[ Preliminary Scan Phase Completed. ]"+bcolors.ENDC)
    print("\n")