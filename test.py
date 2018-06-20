from hunterio_db import get_account_info, read_companies_csv, out_path, inject_contacts
from api_keys import API_KEYS
from settings import CB_PATH, NUM

if __name__ == "__main__":
    if not get_account_info():
        exit(1)

    companies = read_companies_csv(CB_PATH, out_path)
    num = NUM if NUM < len(companies) else len(companies)
    count = 0
    key_idx = 0
    while count < num:
        available = int(API_KEYS[key_idx]["available"])

        if available == 0:
            print("Out of available api_keys! Please add more api_keys OR wait until the reset date!")
            break

        api_key = API_KEYS[key_idx]["api_key"]
        inject_contacts(companies[count:available if available < num else num], api_key)
        count += available
        key_idx += 1

    get_account_info()
    print("Woohoo! Mission complete!")