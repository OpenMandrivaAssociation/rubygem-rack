# Generated from rack-1.2.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rack

Summary:	A modular Ruby webserver interface
Name:		rubygem-%{rbname}

Version:	1.2.2
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://rack.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
%rename		ruby-rack

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

%clean
rm -rf %{buildroot}

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
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/SPEC
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/example
%{ruby_gemdir}/gems/%{rbname}-%{version}/example/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/example/*.ru
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
