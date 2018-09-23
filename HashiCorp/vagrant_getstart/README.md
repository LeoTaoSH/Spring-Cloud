# Vagrant get started
- quick start
```
vagrant init hashicorp/precise64
vagrant up
vagrant ssh
vagrant destroy
```

- empty Vagrantfile
```
mkdir vagrant_getting_started
cd vagrant_getting_started
vagrant init
vagrant box add hashicorp/precise64
```

- edit Vagrant file
```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.box_version = "1.1.0"
  #config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network :forwarded_port, guest: 80, host: 4567
end
```

- share and plugin install
```
vagrant plugin install vagrant-share
vagrant plugin install vagrant-aws
vagrant share
```

- providers
```
vagrant up --provider=vmware_fusion
vagrant up --provider=aws
```