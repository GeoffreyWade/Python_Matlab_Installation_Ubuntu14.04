#! /usr/bin/python

# this matlabConf.py python program is designed and created
# to perform the post MATLAB installation of the download and 
# installation of the package dependencies, and configure
# MATLAB-R2016a for the desktop environment on a Ubuntu 14.04
# TrustyTahr Linux Kernel (4.2.0-34-generic #39~14.04.1-Ubuntu).
# The system is customized w/ the Openbox Window manager/Desktop Environment,
# and the Gnome Display Manager.
# author:GeoWade

from subprocess import call

def pkgGet():

    # create the list of dependency packages to be installed
    # NOTE: matlab-support will prompt the user for
    # directory locations. The selections of /usr/local/MATLAB/R2016a
    # were chosen as the root of the MATLAB Install. No,no, and blank
    # were also chosen.
    pkgLst = ['build-essential', 'gfortran-4.8',
              'gfortran-4.8:amd64', 'libgfortran3:amd64', 
              'libgfortran-4.8-dev:amd64', 'matlab-support']
    
    apgtn = 'sudo apt-get -y install '
    for pkgLst1 in pkgLst:
        aptgn = apgtn + pkgLst1
        call(aptgn, shell=True)

    print 'The GNU fortran compiler and the 4.8 gcc compiles were installed.'

def remJdk():

    # create a list of arguments to be passed to the call function
    # to remove the jvm and jdk1.8.0 directories, and the alternatives
    remf = 'sudo rm -rf '    
    remLst = ['/usr/lib/jvm/jdk1.8.0/*', '/usr/lib/jvm',
              '/etc/altneratives/', '/usr/bin/',
              '/var/lib/dpkg/alternatives/']

    javbinLst = ['java', 'javac', 'javadoc', 'jar']
    numb = 0

    # create a list of java binaries to be iterated in a nested fashion
    for remLst1 in remLst:
        if (numb < 2):
            remjvmdr = remf + remLst1
            call(remjvmdr, shell=True)
        else:
            for javbin in javbinLst:
                remalt = remf + remLst1 + javbin
                call(remalt, shell=True)
        numb += 1
    
    print 'The 8u45 JDK has been deleted\n'

def scriptGet():

    # a list that contains the commands to be printed
    # to the script and that will be executed by the script
    gtscrp = ['#! /bin/sh', 'mkdir -p -m0755 fetchTmp',
              'cd fetchTmp', 
              'wget https://www.dropbox.com/s/'
              'h6bw3tibft3gs17/jdk-7u21-linux-x64.tar.gz',
              'cd -',
              'exit']

    gtscrpOpn = open('wgtArchives.sh', 'w')
    for gtscrp1 in gtscrp:
        gtscrpOpn.write(gtscrp1 + "\n\n")
    gtscrpOpn.close()    
    
    # part 1b: change mode of execution on the script and
    # execute the script
    chsrp = 'chmod 0755 wgtArchives.sh'
    exscrp = './wgtArchives.sh'

    call(chsrp, shell=True)
    call(exscrip, shell=True)
    
    print 'The Oracle jdk1.7.0 has been downloaded\n'

def remScript():

    # creat a list of commands to clean up,
    # and move the jdk into the 'HOME' directory
    mvfetch = ['sudo updatedb',
               'mv fetchTmp/* $HOME/', 
               'rm -rf $HOME/fetchTmp',
               'rm -rf $HOME/wgtArchives.sh',
               'sudo updatedb']

    for fetchmv in mvfetch:
        call(fetchmv, shell=True)


def extractMove():

    # create a list of commands to install the jdk,
    # and install the Oracle jdk7u21.

    oraLst = ['sudo mkdir -p -m0755 /usr/lib/jvm/jdk1.7.0',
              'tar xvf $HOME/jdk-7u21-linux-x64.tar.gz',
              'sudo updatedb',
              'sudo mv jdk1.7.0_21/* /usr/lib/jvm/jdk1.7.0/']

    # execute the commands in the list
    for ora in oraLst:
        call(ora, shell=True)

    print 'The jdk1.7.0 has been moved into the /usr/lib/jvm directory.\n'

def installJdk():

    # create variables to run update-alternatives
    ualts = 'sudo update-alternatives --install \"/usr/bin/'
    ualts1 = ' \"'
    ualts2 = ' \"/usr/lib/jvm/jdk1.7.0/bin/'
    ualts3 = ' 1'

    # a list for the individual jdk binaries,
    # each binary followed by a char slash double qoute
    # to encapsulate the in quotation marks
    jdora = ['java\"', 'javac\"', 'jar\"']

    # execute the comands to update the alternatives
    for ojdk in jdora:
        call(ualts + ojdk + ualts1 + ojdk + ualts2 + ojdk + ualts3, shell=True)

    # remove the extracted folder owned by root
    remjdk = 'sudo rm -rf jdk1.7.0_21'
    call(remjdk, shell=True)

def testJdk():

    orajdk = ['java', 'javac', 'jar', 'java -version']

    for dora in orajdk:
        call(dora, shell=True)

    print 'The Oracle 7u21 JDK has been installed and tested\ndone.'

def dTopEntry():

    # create the matlab.desktop file entry for
    # the /user/share/appications directory
    
    # create a list of strings for the .desktop file
    lstDtop = ['[Desktop Entry]', 'Type=Application',
               'Terminal=false', 'Exec=matlab -desktop','Name=MATLAB', 
               'Icon=/usr/share/icons/hicolor/48x48/apps/matlab.png', 
               'Categories=Development;IDE;Math; Science;',
               'StartupNotify=True'] 

    # output the list to the matlab.desktop file
    matlabopen = open('matlab.desktop', 'w')

    for matline1 in lstDtop:
        matlabopen.write(matline1 + "\n")
    matlabdopen.close()
   
    # move the file to the /usr/share/applications/ directory
    rmoldtop = 'sudo rm -rf /usr/share/applications/matlab.desktop'
    mvdtop = 'sudo mv matlab.desktop /usr/share/applications/'

    call(rmoldtop, shell=True)
    call(mvdtop, shell=True)
            
def main():
    
    pkgGet()

    remJdk()

    scriptGet()

    remScript()

    extractMove()

    installJdk()

    testJdk()
    
    dTopEntry()

main()
 
