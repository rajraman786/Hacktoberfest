import whois # pip install python-whois
import sys

if (len(sys.argv)<2):
    print("usage: " + sys.argv[0] + "<url>")
    sys.exit()
def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

# test with Google domain name
domain_name = sys.argv[1]
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    # print the registrar
    print("Domain registrar:", whois_info.registrar)


    # print the WHOIS server
    print("WHOIS server:", whois_info.whois_server)


    # get the creation time
    print("Domain creation date:", whois_info.creation_date)
    # get expiration date
    print("Expiration date:", whois_info.expiration_date)

    # print all other info
    print(whois_info)