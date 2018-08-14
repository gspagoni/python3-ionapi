# python3-ionapi 

in order to use this example you need to have installed [python3](https://www.python.org/downloads/ "download python")

once installed python open a command window and type 

python --version

unzip the python3-ionapi file in a folder

create a folder in your drive and unzip the chromedriver.zip file
open the oauth2.py file and replace the path in the command
```python
chrome_driver = 'E:/chromedriver_win32/chromedriver.exe'
```
with the path of the created folder

open a command window and go to the folder where you have unzipped the python3-ionapi file

```python
pip install selenium
```

after selenium has been installed 
type python oauth2.py

![image](https://user-images.githubusercontent.com/22134155/44078414-b2cc0a0a-9fa6-11e8-84b0-ef765e3896af.png)

provide a folder that contains files with extension .ionapi

![image](https://user-images.githubusercontent.com/22134155/44078825-c6c8cede-9fa7-11e8-8dab-ac7f361c33b8.png)

![image](https://user-images.githubusercontent.com/22134155/44078956-18b4b5a0-9fa8-11e8-89cf-67ccc5a2c53a.png)

type a number corrisponding to the file you want to use
if the file doesn't contain the redirect URL you are prompted to enter it

![image](https://user-images.githubusercontent.com/22134155/44079954-d88f18a0-9faa-11e8-884f-80681b87ead6.png)

![image](https://user-images.githubusercontent.com/22134155/44083033-3a2cd7fc-9fb3-11e8-99ab-fc1c0097cea4.png)


the script reads the file and display the details and open a browser

![image](https://user-images.githubusercontent.com/22134155/44080075-36e2c56e-9fab-11e8-8716-64c0a5892685.png)

![image](https://user-images.githubusercontent.com/22134155/44080164-81570556-9fab-11e8-855b-fcfe27ad18ae.png)

provide your credential

![image](https://user-images.githubusercontent.com/22134155/44082161-bfb64168-9fb0-11e8-956a-50b7bb433ec1.png)

allow

the script makes the authentication and call the api for displaying the user details
and close the browser

![image](https://user-images.githubusercontent.com/22134155/44082282-0833ce60-9fb1-11e8-9d12-cfd4f6fbbf8e.png)

![image](https://user-images.githubusercontent.com/22134155/44083203-99443208-9fb3-11e8-817e-1c8a4eb45d2c.png)
