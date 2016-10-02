# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.define 'statan' do |machine|
    machine.vm.box = "ubuntu/trusty64"

   config.vm.provider "virtualbox" do |vb|
  #   vb.gui = true
	vb.memory = "1024"
	vb.cpus = 2
   end
  end

  config.vm.provision :shell, :path => "ansible/setup.sh"
end