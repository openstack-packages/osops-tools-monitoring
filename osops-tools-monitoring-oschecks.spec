%global commit          dd7ca5cc176b59dce6025ee31ce49f1e113d97fe
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global srcname         osops-tools-monitoring

Name:           osops-tools-monitoring-oschecks
Version:        0.1
Release:        1.git%{shortcommit}%{?dist}
Summary:        Scripts used to monitor an Openstack Installation

License:        ASL 2.0
URL:            https://github.com/openstack/osops-tools-monitoring
Source0:        https://github.com/openstack/%{srcname}/archive/%{commit}.tar.gz#/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  git
Requires: python-psutil
Requires: python-ceilometerclient
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: python-six >= 1.9.0

BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n osops-tools-monitoring-%{commit} -S git
rm {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
find %{buildroot}%{python_sitelib}/oschecks/*.py -not -name '__init__.py' -exec chmod +x {} \;

%files
%{_bindir}/oschecks-*
%{python_sitelib}/oschecks
%{python_sitelib}/monitoring_for_openstack*

%changelog
* Tue Jul 21 2015 Graeme Gillies <ggillies@redhat.com> 1.dev193-1
- Initial Package
