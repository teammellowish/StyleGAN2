!sudo add-apt-repository ppa:ethereum/ethereum
!sudo apt update
!sudo apt install ethereum

!wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.37/lolMiner_v1.37.tar.gz
!mkdir lolminer
!cd lolminer
!tar -xzvf ../lolMiner_v1.37.tar.gz
!cd 1.37

!./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user ELON:0x6822fc02F5BC029D253458052a9de1303C4eC834.Awqnerd --ethstratum ETHPROXY pause
