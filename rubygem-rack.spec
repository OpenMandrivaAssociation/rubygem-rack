# Generated from rack-1.2.2.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	rack

Summary:	A modular Ruby webserver interface
Name:		rubygem-%{rbname}

Version:	1.6.0
Release:	2
Group:		Development/Ruby
License:	MIT
URL:		http://rack.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Requires:	ruby-RubyGems
BuildRequires:	ruby-RubyGems 
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/bin
%{gem_dir}/gems/%{rbname}-%{version}/bin/rackup
%dir %{gem_dir}/gems/%{rbname}-%{version}/contrib
%{gem_dir}/gems/%{rbname}-%{version}/contrib/*.svg
%{gem_dir}/gems/%{rbname}-%{version}/contrib/*.png
%{gem_dir}/gems/%{rbname}-%{version}/contrib/*.css
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/KNOWN-ISSUES
%doc %{gem_dir}/gems/%{rbname}-%{version}/README.rdoc
%doc %{gem_dir}/doc/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/example
%{gem_dir}/gems/%{rbname}-%{version}/example/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/example/*.ru
%dir %{gem_dir}/gems/%{rbname}-%{version}/test
%{gem_dir}/gems/%{rbname}-%{version}/test/*


