import hmac
import hashlib




voucher = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa82402309aa3e0d59870cbfbbb3b19cb0be20c2241afc031f53918bb09a3f3bfa'
voucher_id = voucher[:32]
signature = voucher[32:]
expected_signature = hmac.new(b'sup3r_s3cr3t_k3y', voucher_id.encode('utf-8'), hashlib.sha256).hexdigest()
print(expected_signature)
if hmac.compare_digest(expected_signature, signature) == True:
        print('oook')
