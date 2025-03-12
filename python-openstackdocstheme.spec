#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# test target (not included in dist tarball?)

Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Name:		python-openstackdocstheme
# keep 1.x here for python2 support
Version:	1.31.2
Release:	8
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/openstackdocstheme/
Source0:	https://files.pythonhosted.org/packages/source/o/openstackdocstheme/openstackdocstheme-%{version}.tar.gz
# Source0-md5:	24ff0af7dd233e78e9f388e7e0876426
URL:		https://docs.openstack.org/openstackdocstheme/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.6.2
BuildRequires:	python-bindep
BuildRequires:	python-dulwich >= 0.15.0
BuildRequires:	python-hacking >= 1.1.0
BuildRequires:	python-hacking < 1.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.6.2
BuildRequires:	python3-bindep
BuildRequires:	python3-dulwich >= 0.15.0
BuildRequires:	python3-hacking >= 1.1.0
BuildRequires:	python3-hacking < 1.2.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-os-api-ref >= 1.4.0
BuildRequires:	python3-reno >= 2.5.0
BuildRequires:	sphinx-pdg-3 >= 1.6.6
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme and extension support for Sphinx documentation from the
OpenStack project.

%description -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

%package -n python3-openstackdocstheme
Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-openstackdocstheme
Theme and extension support for Sphinx documentation from the
OpenStack project.

%description -n python3-openstackdocstheme -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

%prep
%setup -q -n openstackdocstheme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc-build/html/doc
sphinx-build-3 -b html api-ref/source doc-build/html/api-ref
sphinx-build-3 -b html releasenotes/source doc-build/html/releasenotes
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

# too custom scripts
%{__rm} $RPM_BUILD_ROOT%{_bindir}/docstheme-{build-pdf,build-translated.sh,lang-display-name.py}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/openstackdocstheme
%{py_sitescriptdir}/openstackdocstheme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-openstackdocstheme
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/openstackdocstheme
%{py3_sitescriptdir}/openstackdocstheme-%{version}-py*.egg-info
%endif
