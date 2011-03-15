%define oname rack

Summary:	Common API for connecting web frameworks, web servers and layers of software
Name:		ruby-%{oname}
# (proyvind): stick with 1.0.1 for now as it's explicitly required by gitorious...
Version:	1.2.2
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://rack.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Requires:	ruby

%description
Rack provides a common API for connecting web frameworks,
web servers and layers of software in between

%prep

%build

%install
rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

chmod g-w -R %{buildroot}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/rackup
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_gemdir}/gems/%{oname}-%{version}

