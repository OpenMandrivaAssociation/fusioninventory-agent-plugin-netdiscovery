Name:		fusioninventory-agent-plugin-netdiscovery
Version:	1.5
Release:	3
Summary:	OCS Inventory Software deployment support for FusionInventory agent
License:	GPL
Group:		System/Servers
URL:		http://fusioninventory.org/wordpress/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FU/FUSINV/FusionInventory-Agent-Task-NetDiscovery-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl-devel

%description
With this module, FusionInventory can accept software deployment request from
an OCS Inventory server.

%prep
%setup -q -n FusionInventory-Agent-Task-NetDiscovery-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS Changes README LICENSE
%{perl_vendorlib}/FusionInventory
%{_mandir}/man3/FusionInventory::Agent::Task::NetDiscovery.3pm*



%changelog
* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2011.0
+ Revision: 685571
- update to new version 1.5

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1
+ Revision: 649133
- update to new version 1.3

* Mon Aug 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2011.0
+ Revision: 570309
- new version

* Mon Aug 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdv2011.0
+ Revision: 564982
- fix backportability

* Mon Aug 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2011.0
+ Revision: 564972
- new version

* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2011.0
+ Revision: 541798
- import fusioninventory-agent-plugin-netdiscovery


* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2010.1
- initial mdv release
