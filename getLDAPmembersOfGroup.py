from ldap3 import Server, Connection #pip install ldap3
from ldap3.core.exceptions import LDAPSocketOpenError
import json

ldap_server=f"ldap://<LDAP_SERVER>:389"
ldap_base = 'CN=ITAll,OU=....'
bind_account = 'CN=ldap-account,OU=Service Accounts,DC=...'
bind_password = '<LDAP_PASSWORD>'

def ldap():
    try:
        ldap_connection = Connection(ldap_server, bind_account, bind_password)
        if ldap_connection.bind() == True:
            if ldap_connection.search(ldap_base, '(objectclass=group)', attributes=['member']) == True:
                response = json.loads(ldap_connection.response_to_json())
                return response
            else:
                response = 'Error getting group members'
                return None
    except LDAPSocketOpenError:
        response = 'Unabled to connect to the LDAP server!'
        return response

output = ldap()
print(output)