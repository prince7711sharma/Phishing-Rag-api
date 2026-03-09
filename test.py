from rag_detector import detect_url

urls = [

"https://google.com",
"https://github.com",
"http://paypal-login-secure-update.com",
"http://verify-bank-account-login.com"

]

for url in urls:

    result = detect_url(url)

    print(url, "→", result)