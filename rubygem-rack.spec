# Generated from rack-1.2.2.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	rack

Summary:	A modular Ruby webserver interface
Name:		rubygem-%{rbname}

Version:	1.4.1
Release:	2
Group:		Development/Ruby
License:	MIT
URL:		http://rack.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Requires:	ruby-RubyGems
Requires:	rubygem(bacon)	
Requires:	rubygem(memcache-client)	
Requires:	rubygem(mongrel)	
BuildRequires:	ruby-RubyGems 
BuildRequires:	rubygem(bacon)
BuildRequires:	rubygem(mongrel)
BuildArch:	noarch
#rename		ruby-rack

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books 
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(contrib|example|test)/'

%install
%gem_install

%files
%{_bindir}/rackup
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rackup
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/contrib
%{ruby_gemdir}/gems/%{rbname}-%{version}/contrib/*.svg
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/KNOWN-ISSUES
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/example
%{ruby_gemdir}/gems/%{rbname}-%{version}/example/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/example/*.ru
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*


%changelog
* Thu Feb 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.1-2
+ Revision: 774723
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 1.4.1-1
+ Revision: 769667
- New release

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - revert %%rename
    - drop %%clean
    - %rename ruby-rack

* Sat Sep 10 2011 Alexander Barakin <abarakin@mandriva.org> 1.3.2-1
+ Revision: 699185
- imported package rubygem-rack

* Tue Mar 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.2-1
+ Revision: 645159
- bump version down to 1.1.2 for compatibility
- rename and regenerate spec with gem2rpm5
- new release: 1.2.2

* Tue Dec 14 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.0-3mdv2011.0
+ Revision: 621823
- rebuild for new rpm-mandriva-setup

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 614765
- the mass rebuild of 2010.1 packages

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 531331
- update to new version 1.1.0

* Mon Feb 01 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 499177
- fix summary
- import ruby-rack


* Mon Feb  1 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.1-1
- initial release
