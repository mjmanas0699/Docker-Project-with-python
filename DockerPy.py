import os
os.system("tput setaf 2") 
print("\t\t\t WELCOME TO OUR DOCKER Project")
print("\t\t\t-------------------------------") 
os.system("tput setaf 7") 
print("""Caution : Before going ahead you Should Have Docker & Docker  & Compose
             Type yes To Install
             Type no  If You've Already""")
     
print()    
     
docins=input("Your Input ? ")
if docins=="yes":   #IF YES then
 
   os.system(" sudo echo [docker]  > /etc/yum.repos.d/dockerCe.repo")
  
   os.system(" sudo echo baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ >> /etc/yum.repos.d/dockerCe.repo" )

   os.system("sudo echo gpgcheck=0  >> /etc/yum.repos.d/dockerCe.repo")

   os.system("sudo  yum install docker-ce --nobest -y")

   os.system("sudo rm -f /etc/yum.repos.d/docekrCe.repo ")
  
   os.system("sudo systemctl start docker")
  

   os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
   
   os.system('sudo chmod +x /usr/local/bin/docker-compose')

     
else:
     pass

while True:
      os.system("clear")
      os.system("tput setaf 7")
      print("""
         press 1 To Lunch Website on Local System (Wordpress)
         PRESS 2 Use Terminal Online (Ubuntu)
         Press 3 To See Running Containers Name 
	 Press 4 To remove docker and docker compose
         press 5 to exit  
         
         """)

      print("ENTER THE NO. IN BETWEEN ABOVE MENTION", end=" ")
      os.system("tput setaf 7") 
      usript=input("") #variable for all conditions

      if usript=="1":
      
         os.system("sudo wget https://raw.githubusercontent.com/mjmanas0699/linuxpy/master/docker-compose.yml")
         os.system(" docker-compose up -d ")
         os.system(" sudo rm -f docker-compose.yml") 
         a=os.popen(" sudo hostname -I | awk '{print $1}'").read() #store command in var(a)
         
         os.system("tput setaf 4")
         print('Use This IP On Web browser {}'.format(a),end="")
         print("ON THIS PORT -> :8080")
         os.system("tput setaf 7")


      elif usript=="2" : 
           os.system(" sudo docker pull sspreitzer/shellinabox")
           cn=input("Enter new container name")
           du=input("User name (Use While Login)-")
           dp=input("please enter Password-")
           dpo=input("please enter free port no -")
           os.system("docker  run --name {} -d -p {}:4200 -e SIAB_PASSWORD={} -e SIAB_USER={} -e SIAB_SUDO=true -e SIAB_SSL=false  sspreitzer/shellinabox:latest".format(cn,dpo,dp,du))
           os.system("tput setaf 4")
           a=os.popen(" sudo hostname -I | awk '{print $1}'").read() #store command in var(a)
           print('Use This IP On Web browser {}'.format(a),end="")
           print("ON THIS PORT -> {}".format(dpo))
           os.system("tput setaf 7")
      elif usript=="3" : 
           print("Might Take Some Time")
           os.system("sudo docker ps --format '{{.Names}}'")
           

      elif usript=="5" : 
           
           break 
      elif usript=="4" : 

           rdk=input("Are You Sure ?")

           if rdk=="yes":
              os.system("sudo yum remove docker-ce.x86_64")
              os.system("sudo rm /usr/local/bin/docker-compose")
           elif rdk=="no":
                print("Chill :)")

      input("\nSuccesfully Run")
     
        

 



