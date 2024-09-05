
def ipLookUp():

    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL
    GRAY = Fore.LIGHTBLACK_EX
    BIGYELLOW = Fore.LIGHTYELLOW_EX

    IpBanner = """
    ██╗██████╗ 
    ██║██╔══██╗
    ██║██████╔╝
    ██║██╔═══╝ 
    ██║██║     
    ╚═╝╚═╝     
    """.replace("█", f"{BIGYELLOW}█{RESET}")
    print(IpBanner)
    ip_address = input(f"{BIGYELLOW}┌─[ ~ {Fore.RED}{pseudo}{BIGYELLOW}]\n└─── {Fore.WHITE}Enter Ip Address:{RESET} ")
    response = requests.get(f'http://ipinfo.io/{ip_address}/json').json()
    ipp = response.get("ip")
    network = response.get("network")
    version = response.get("version")

    city = response.get("city")
    region = response.get("region")
    country = response.get("country")
    postal = response.get("postal")


    loc = response.get("loc")
    timezone = response.get("timezone")

    org = response.get("org")

    print(f"\n  {CYAN}•────────{RESET} Ip Information ({ipp}) {CYAN}────────•")
    print(f"  {CYAN}│")
    print(f"  {CYAN}├• {GRAY}City:{RESET} {BIGYELLOW}{city}")
    print(f"  {CYAN}├• {GRAY}Region:{RESET} {BIGYELLOW}{region}")
    print(f"  {CYAN}├• {GRAY}Country Name:{RESET} {BIGYELLOW}{country}")
    print(f"  {CYAN}├• {GRAY}Postal Code:{RESET} {BIGYELLOW}{postal}")
    print(f"  {CYAN}│")
    print(f"  {CYAN}├• {GRAY}Coordinates:{RESET} {BIGYELLOW}{loc}")
    print(f"  {CYAN}├• {GRAY}Timezone:{RESET} {BIGYELLOW}{timezone}")
    print(f"  {CYAN}└• {GRAY}ORG:{RESET} {BIGYELLOW}{org}{RESET}\n")

ipLookUp()