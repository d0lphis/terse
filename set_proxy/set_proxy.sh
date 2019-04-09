#!/bin/bash
# Support ubuntu 16.x, rhel 7.x

#PROXY_SERVER="9.21.53.14"
PROXY_SERVER="9.21.53.14"
PROXY_PORT="3128"

# Setup apt proxy
function setup_apt_proxy() {
    cat >>/etc/apt/apt.conf<<EOF
Acquire::http::Proxy "http://${PROXY_SERVER}:${PROXY_PORT}/";
Acquire::ftp::proxy "ftp://${PROXY_SERVER}:${PROXY_PORT}/";
Acquire::https::proxy "https://${PROXY_SERVER}:${PROXY_PORT}/";
EOF
    sudo apt-get update
}

# Setup yum proxy
function setup_yum_proxy() {
    [[ ! -f /etc/yum.conf ]] && touch /etc/yum.conf
    cat >>/etc/yum.conf<<EOF
proxy=http://${PROXY_SERVER}:${PROXY_PORT}
EOF
setup_yum_base_repo
}

# Setup yum base repo
function setup_yum_base_repo() {
    cat > /etc/yum.repos.d/platformlab.repo<<EOF
[platformlab]
name=rhel7.3
baseurl=http://9.111.249.112/install/rhels7.3/x86_64
gpgcheck=0
enabled=1
EOF
}

# Setup wget proxy
function setup_wget_proxy() {
    which wget
    if [[ "$?" != "0" ]]; then
        [[ "$ID" == "ubuntu" || "$ID" == "debian" ]] && apt install wget
        [[ "$ID" == "centos" || "$ID" == "rhel" ]] && yum install wget -y
    fi
    [[ ! -f /etc/wgetrc ]] && touch /etc/wgetrc
    cat >>/etc/wgetrc<<EOF
http_proxy=http://${PROXY_SERVER}:${PROXY_PORT}
https_proxy=https://${PROXY_SERVER}:${PROXY_PORT}
ftp_proxy=ftp://${PROXY_SERVER}:${PROXY_PORT}
EOF
}

# Install docker if not installed
function install_docker() {
    docker_version=$(dockerd --version 2>/dev/null)
    [[ "X$docker_version" != "X" ]] && return 0
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    export https_proxy=https://${PROXY_SERVER}:${PROXY_PORT}
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    unset https_proxy
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt-get update
    apt-get install -y docker-ce
}

# Setup docker proxy
function setup_docker_proxy() {
    install_docker
    DOCKER_SERVICE_D="/etc/systemd/system/docker.service.d"
    [[ ! -d ${DOCKER_SERVICE_D} ]] && mkdir -p ${DOCKER_SERVICE_D}
    cat >${DOCKER_SERVICE_D}/http-proxy.conf<<EOF
[Service]
Environment="HTTP_PROXY=http://${PROXY_SERVER}:${PROXY_PORT}/" "NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com"
EOF
    cat >${DOCKER_SERVICE_D}/https-proxy.conf<<EOF
[Service]
Environment="HTTPS_PROXY=http://${PROXY_SERVER}:${PROXY_PORT}/" "NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com"
EOF
    systemctl daemon-reload
    systemctl restart docker
}

# Setup git http/https proxy
function setup_git_proxy() {
    which git
    if [[ "$?" != "0" ]]; then
        [[ "$ID" == "ubuntu" || "$ID" == "debian" ]] && apt install git
        [[ "$ID" == "centos" || "$ID" == "rhel" ]] && yum install git -y
    fi
    git config --global http.proxy http://${PROXY_SERVER}:${PROXY_PORT}
    git config --global https.proxy https://${PROXY_SERVER}:${PROXY_PORT}
    # Setup git ssh proxy
    which connect-proxy
    if [[ "$?" != "0" ]]; then
        [[ "$ID" == "ubuntu" || "$ID" == "debian" ]] && apt install connect-proxy
        if [[ "$ID" == "centos" || "$ID" == "rhel" ]]; then
            cd /tmp;wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
            cd /tmp;rpm -ivh epel-release-latest-7.noarch.rpm
            yum install connect-proxy -y
        fi
    fi
    [[ ! -f ~/.ssh/id_rsa ]] && ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''
    [[ ! -f ~/.ssh/config ]] && touch ~/.ssh/config
    cat >>~/.ssh/config<<EOF
Host github.ibm.com
   ProxyCommand connect-proxy -H ${PROXY_SERVER}:${PROXY_PORT} %h %p
   IdentityFile ~/.ssh/id_rsa
   User git
EOF
}

# Setup hosts
function setup_hosts() {
    [[ "$ID" == "centos" || "$ID" == "rhel" ]] && echo "$(ifconfig  |grep inet | grep 9.111 |sed 's/^.*inet //g' | cut -d' ' -f1) $(hostname)" >> /etc/hosts
    [[ "$ID" == "ubuntu" || "$ID" == "debian" ]] && echo "$(ifconfig  |grep inet  |grep 9.111 |cut -d: -f2|awk '{print $1}') $(hostname)" >> /etc/hosts
}

# Generate proxy conf
function genetate_proxy_conf() {
    cat > /root/proxy.conf <<EOF
export http_proxy=http://${PROXY_SERVER}:${PROXY_PORT}
export https_proxy=https://${PROXY_SERVER}:${PROXY_PORT}
export ftp_proxy=ftp://${PROXY_SERVER}:${PROXY_PORT}
EOF
}

source /etc/os-release
# Common distributor ID: debian|ubuntu|devuan|centos|fedora|rhel
[[ "$ID" == "ubuntu" || "$ID" == "debian" ]] && setup_apt_proxy
[[ "$ID" == "centos" || "$ID" == "rhel" ]] && setup_yum_proxy
setup_wget_proxy
setup_docker_proxy
setup_git_proxy
genetate_proxy_conf
setup_hosts
