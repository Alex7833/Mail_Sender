# Mail Sender in python3

## Installation

```sh
git clone https://github.com/AlexRandomed/Mail_Sender
cd Mail_Sender
pip3 install -r requirements.txt
```

## Configuration

/!\ If you have a gmail account /!\

1. Go to <https://myaccount.google.com/lesssecureapps>
2. Allow your account to access less secure applications


## Usage

```sh
python3 send_mail.py
```

## Examples

```
python3 send_mail.py

███╗   ███╗ █████╗ ██╗██╗        ██████╗███████╗███╗  ██╗██████╗ ███████╗██████╗    
████╗ ████║██╔══██╗██║██║       ██╔════╝██╔════╝████╗ ██║██╔══██╗██╔════╝██╔══██╗  
██╔████╔██║███████║██║██║       ╚█████╗ █████╗  ██╔██╗██║██║  ██║█████╗  ██████╔╝  
██║╚██╔╝██║██╔══██║██║██║        ╚═══██╗██╔══╝  ██║╚████║██║  ██║██╔══╝  ██╔══██╗   
██║ ╚═╝ ██║██║  ██║██║███████╗  ██████╔╝███████╗██║ ╚███║██████╔╝███████╗██║  ██║ 
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ╚═════╝ ╚══════╝╚═╝  ╚══╝╚═════╝ ╚══════╝╚═╝  ╚═╝  


To address (separated by space) : test@gmail.com test2@gmail.com
Number of message : 2
Votre message : Hello world !

Message to : test@gmail.com
[-] 1 : message sent
[-] 2 : message sent
[+] All emails have been sent to test@gmail.com 
----------------------------


Message to : test2@gmail.com
[-] 1 : message sent
[-] 2 : message sent
[+] All emails have been sent to test2@gmail.com 
----------------------------

[+] All emails have been sent to all mail address
```

## Contributing

1. Fork it (<https://github.com/AlexRandomed/Mail_Sender/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
