%global srcname dephell

Name:           python-%{srcname}
Version:        0.8.3
Release:        1
Summary:        Manage packages: convert between formats, lock, install, resolve, isolate, test, build graph, show outdated, audit. 
Group:          Development/Python
License:        MIT
URL:            https://github.com/dephell/dephell
Source0:        https://files.pythonhosted.org/packages/source/d/dephell/dephell-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description
Python project management. Manage packages: convert between formats, lock, install, resolve, isolate, test, build graph, show outdated, audit. 
Manage venvs, build package, bump version.
%prep
%autosetup -n %{srcname}-%{version}


%build
%py_build

%install
%py_install

%files
%{_bindir}/dephell
%{python_sitelib}/dephell-%{version}-py*.*.egg-info/PKG-INFO
%{python_sitelib}/dephell-%{version}-py*.*.egg-info
%{python_sitelib}/dephell/
