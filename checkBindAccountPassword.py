import ldap3
from ldap3.core.exceptions import LDAPException


def _ldap_login(username, password):
    try:
        with ldap3.Connection('ldap://<LDAP_SERVER>:389', user=username, password=password) as conn:
            print(conn.result["description"]) # "success" if bind is ok
            return True
    except LDAPException:
        print('Unable to connect to LDAP server')
        return False

_ldap_login("CN=ldap-account,OU=Service Accounts,DC=...", "<PASSWORD>")