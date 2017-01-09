# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "bento/ubuntu-16.04"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  #config.vm.synced_folder "~/workspaces/public/go-extract.git", "/home/vagrant/src/github.com/pjdufour/go-extract", owner: "vagrant", group: "vagrant"
  #config.vm.synced_folder "~/workspaces/public/go-gypsy.git", "/home/vagrant/src/github.com/kylelemons/go-gypsy", owner: "vagrant", group: "vagrant"

  config.vm.provider "virtualbox" do |vb|\
      vb.gui = false
      vb.cpus = 2
      vb.memory = 4096
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/ubuntu_go.yml"
    ansible.host_key_checking = false
    ansible.verbose = "v"
    ansible.raw_arguments = []
  end

end
