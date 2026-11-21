subject=CN=localhost
issuer=CN=localhost
notBefore=Nov 17 00:52:56 2026 GMT
notAfter=Dec 17 00:52:56 2026 GMT

curl: (60) SSL certificate OpenSSL verify result: self-signed certificate (18)
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.

The -k tag  allows curl to connect to HTTPS servers without checking the site's TLS certification first.

A self-verified web certificate proves nothing because no trusted authority has approved or verified who owns the server.

Real websites get TLS certificates by requesting them from a verified certificate authority and proving they control or own the domain name.

Let's Encrypt issued the certificate. 4A's certificate was self-signed. 

Let's Encrypt vouched this time after Tailscale proved control by publishing a DNS record.A laptop in the next row could not open the address because it was not in the instructors tailnet. The name points to a private tailscale address so the certificate doesn't help anyone who can't access the network.
