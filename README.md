# tmail
Free temporary email (python library)
```
pip install tmail
```

# Usage Example 
import library 
```py
import requests
from tmail import TMail

tm = TMail()
```
displays the mail name
```py
print('Your Mail: '+ tm.mail)
```
check incoming messages
```py
while True:
    try:
        boxmail = tm.messages()
        if len(boxmail) != 0:
            print(boxmail)
            break
        else:
            continue
    except requests.exceptions.ConnectionError:
        continue
```
