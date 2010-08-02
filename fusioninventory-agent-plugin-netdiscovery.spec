Name:		fusioninventory-agent-plugin-netdiscovery
Version:	1.1
Release:	%mkrel 2
Summary:	OCS Inventory Software deployment support for FusionInventory agent
License:	GPL
Group:		System/Servers
URL:		http://fusioninventory.org/wordpress/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GONERI/FusionInventory-Agent-Task-NetDiscovery-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Module::CoreList)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
With this module, FusionInventory can accept software deployment request from
an OCS Inventory server.

%prep
%setup -q -n FusionInventory-Agent-Task-NetDiscovery-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf  %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes README LICENSE
%{perl_vendorlib}/FusionInventory
%{_mandir}/man3/FusionInventory::Agent::Task::NetDiscovery.3pm*

