from flask import Blueprint, render_template, request
import requests, os 
from dotenv import load_dotenv
load_dotenv()

views = Blueprint('views', __name__, template_folder='public', static_url_path='', static_folder='static')

@views.route('/')
def index():
    userip = request.headers.get('X-forwarded-for', request.remote_addr)
    callapi = requests.get(f'https://ipinfo.io/{userip}/json?{os.getenv('TOKEN')}')
    ip = callapi.json()

    if ip.get("status"):
        return render_template('ratelimit.html')


    isp = " ".join(ip["org"].split()[1:])

    if any(
        x.lower() in isp.lower() for x in [
            "Google",
            "Cloudflare",
            "Amazon",
            "Microsoft",
            "Oracle",
            "Hetzner",
            "OVH",
            "DigitalOcean",
            "Linode",
            "Vultr",
            "Leaseweb",
            "Contabo",
            "NordVPN",
            "ExpressVPN",
            "Mullvad",
            "ProtonVPN",
            "Surfshark",
            "Windscribe",
            "VyprVPN",
            "Tor",
            "The Onion Router",
            "Tailscale",
            "Private Internet Access",
            "CyberGhost",
            "PureVPN",
            "IPVanish",
            "StrongVPN"
        ]
    ):
        proxy = "Yes"
    else:
        proxy = "No"

    if "." in userip:
        ipv = "IPv4"
    else:
        ipv = "IPv6"

    loc_x = ip["loc"].split(",")[0]
    loc_y = ip["loc"].split(",")[1]

    country_name = requests.get(f'https://restcountries.com/v3.1/alpha/{ip["country"]}')

    if country_name.status_code == 200:
        country_name = country_name.json() 
        ip.update(
            {
                "country_name": country_name[0]["name"]["common"],
                "country_official_name": country_name[0]["name"]["official"],
                "country_flag": country_name[0]["flags"]["png"]
            }
        )
    else:
        ip.update({"country_name": "Unknown"})

    ip.update(
        {
            "proxy": proxy,
            "ipv": ipv,
            "isp": isp,
            "x": loc_x,
            "y": loc_y
        }
    )

    return render_template('index.html', ip=ip)
