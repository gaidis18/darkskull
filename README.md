# Darkskull

![27 07 2021_23 28 17_REC](https://user-images.githubusercontent.com/65406173/127254110-00f86717-8fa4-4962-8938-1366635ad1d7.gif)

Python malware to steal all files with the defined extension, share, delete and then auto-destroy all the evidences.

## How it Works:
Inside all the directories that are bundled with the malware, darkskull will get all files with the passed extension. All of these files will be deleted and subscribed to a text file that will be sent to the defined email. When finished the theft and sharing, the text file and source code will self-destruct, leaving no trace behind.

## First instructions:
1º Change the content of fromaddr and frompass to the email you will use to send the content.(Do not use your personal email, and enable the use of less secure apps)

2º Put the SMTP address and port of the e-mail service chosen by you.(Example 'smtp.gmail.com', 587)
  
## How to Run:

-t or --target: extension you want to steal.(Example: -t java)

-m or --mail: e-mail you want to receive the information.(Example: -m mail@address)



