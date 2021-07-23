# darkskull - Malware 
![image](https://user-images.githubusercontent.com/65406173/126813287-6e373379-9163-4a07-983d-31ee17678f3b.png)

Python malware to steal all files with the defined extension, delete the original content, share and then auto-destroy all the evidences.

## How it Works:
Inside the defined directory, darkskull will get all files with the passed extension. All contents of these files will be deleted and passed to a text file that will be sent to the defined email. When finished the theft and sharing, the text file and source code will self-destruct, leaving no trace behind.

## First instructions:
1º Change the content of fromaddr and frompass to the email you will use to send the content.(Do not use your personal email, and enable the use of less secure apps)

2º Put the SMTP address and port of the e-mail service chosen by you.(Example 'smtp.gmail.com', 587)
  
## How to Run:

-t or --target: extension you want to steal.(Example: -t java)

-m or --mail: e-mail you want to receive the information.(Example: -m mail@address)

-d or --directory: directory that will do the search.(Example: --directory ../)



