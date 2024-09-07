#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the 2019 Facebook Breach.")


#Introduces breach
print("Would you like to learn about the 2019 Facebook Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organizations response, or (c) I would like to hear your refelection")
  topic = input()
  
  if topic.lower() == "a":
    print("In 2019, malicious actors scraped personal information of 553 million people from Facebook’s platform including phone numbers, full names, locations, some email addresses, and other details from user profiles. They did so by exploiting a vulnerability in a feature on the platform that allowed users to find each other by phone number.")
  
  elif topic.lower() == "b":
    print("Facebook had detected and fixed the issue, deeming it unnecessary to notify users of whose personal data had been compromised in a breach, as the information was already publicly available --- users could not resolve the issue alone.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective for you. Are you excited to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach connects to confidentiality because Facebooks users’ data had been compromised due to malicious actors.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization’s response because I think Facebook should have let users know there was a breach immediately so users could have been on alert.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by saying the data leak still leaves users vulnerable as their information can be misused. My advice would be to find out whether your personal information was leaked in the breach, by checking the online data tracking tool website, HaveIBeenPwnd.")

  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")