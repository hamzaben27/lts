import os
import subprocess
class pivotel:
    def __init__(self):
        pass
        #remember
        #ci on cas de confidencialite fait elemenier root_pwd


        ################################################################################################################
    def build(self,ver,pack,pwd):
        os.chdir("/home/ghost/PycharmProjects/pfe/shell")
        ver="./"+ver
        print(ver)
        list = []
        list.append(ver);list.append(pack);list.append("cf_cli_install.sh");list.append(pwd)
        print("list =")
        print(list)
        #list.append("./");list.append(ver);list.append(" ");list.append(pack);list.append(" ");list.append(pwd)
        #subprocess.call(list)
        cmd="".join(list)
        print ("cmd = "+cmd)
        subprocess.call(list)
        #os.system('./verifier_la_instalation_des_logiciel.sh cf-cli cf_cli_install.sh darkle09')
        #os.system(cmd)
       # os.system('./%s %s %s'% (self.verifier_package_install,self.package_to_install,self.root_pwd))

        #os.system(cool)

        ################################################################################################################
    def run(self,email,pwd,nom_app):
        #os.system('cf api https://api.ng.bluemix.net')
        #os.system('cf login -a https://api.ng.bluemix.net -u koudjil1@live.fr -p "Darkle09&"')
        list = []
        list.append('cf ');
        list.append('login -a ');
        list.append('https://api.run.pivotal.io -u ');
        list.append(email);
        list.append(' -p ');
        list.append("\"" + pwd + "\"");  # list.append(' -s koudjil')
        a = "".join(list)
        print (a)

        #os.system(a)
        #login= subprocess.check_output([a],shell=True,stderr=subprocess.STDOUT)
        try:
            login = subprocess.getoutput(a)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command login '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        try:
            deploy = subprocess.getoutput("cf push "+nom_app)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command deploy '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        try:
            apps = subprocess.getoutput("cf apps")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                "command apps '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        os.system("xdg-open https://"+nom_app+".cfapps.io")

        return login,deploy,apps

        ################################################################################################################
    def config(self,dirctory,nom_app):
        print ("derictory ", dirctory)
        list = [];
        list.append(dirctory)
        # subprocess.call(dirctory)
        os.chdir(dirctory)
        os.system("pwd")
        fichiers=os.listdir(dirctory)
        print (fichiers)
        exist= "package.json" in fichiers
        print("exist valeur ==",exist)

        Fichier = open('manifest.yml', 'w')
        Fichier.write("--- \n")
        Fichier.write("applications: \n")
        Fichier.write("- name : "+nom_app+"\n")
        Fichier.write("  memory : 128M \n")

        if "package.json" in fichiers:
            Fichier.write("  buildpack : https://github.com/cloudfoundry/nodejs-buildpack.git \n")#donner le buildpack pour nodejs
        elif "requirements.txt" in fichiers:
            Fichier.write("  buildpack : https://github.com/cloudfoundry/python-buildpack.git \n")#donner le buildpack pour python
        elif "composer.json" in fichiers:
            Fichier.write("  buildpack : https://github.com/cloudfoundry/php-buildpack.git \n")#donner le buildpack pour php
        # Fichier.write("  instances : 2 \n")
        Fichier.close()



#pivotel_instance = pivotel()
#pivotel_instance.build('verifier_la_instalation_des_logiciel.sh','cf-cli','darkle09')
#pivotel_instance.config("/home/ghost/Téléchargements/app test/nodejs/node-js-getting-started")
#pivotel_instance.run()