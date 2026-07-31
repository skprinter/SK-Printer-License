import requests

LICENSE_URL = "https://raw.githubusercontent.com/skprinter/SK-Printer-License/main/license.json"

def check_license():
    try:
        response = requests.get(LICENSE_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
