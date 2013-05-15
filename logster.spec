Summary:	Parse log files, generate metrics for Graphite and Ganglia
Name:		logster
Version:	0.0.1
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://github.com/etsy/logster/archive/v%{version}.tar.gz
# Source0-md5:	7e1b92be0e83cd81880293e2bed44d88
URL:		https://github.com/etsy/logster
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	logcheck
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logster is a utility for reading log files and generating metrics in
Graphite or Ganglia. It is ideal for visualizing trends of events that
are occurring in your application/system/error logs.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/logster
%{py_sitescriptdir}/logster
%{py_sitescriptdir}/logster-%{version}-py*.egg-info
