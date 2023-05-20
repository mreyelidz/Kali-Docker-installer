import os

def install_docker():
    # Update the package list
    os.system("sudo apt-get update")

    # Install the necessary packages
    os.system("sudo apt-get -y install apt-transport-https ca-certificates curl gnupg lsb-release")

    # Add the Docker GPG key
    os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")

    # Add the Docker repository to APT sources
    os.system('echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')

    # Update the package list again
    os.system("sudo apt-get update")

    # Install Docker Engine
    os.system("sudo apt-get -y install docker-ce docker-ce-cli containerd.io")

    # Verify that Docker Engine is installed correctly
    os.system("sudo docker run hello-world")

if __name__ == '__main__':
    install_docker()
